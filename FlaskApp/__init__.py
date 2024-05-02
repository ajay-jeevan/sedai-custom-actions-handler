from flask import Flask, jsonify, request
import json
import os
import requests
import logging

app = Flask(__name__)

workflow_auto_url = os.getenv('URL', default="https://wms-stackstorm-dev.runops.ohlogistics.com/api/v1/executions")

@app.route("/performAction", methods=['POST'])
def performAction():

    request_json = request.json
    action_name = request_json.get('proposedAction').get('actionName')
    host_name = request_json.get('resourceActionDetails').get('instanceDetails').get('instanceId')

    headers = {
        "Content-Type": "application/json",
        "St2-Api-Key": os.getenv("KEY")
    }

    if action_name == 'REBOOT':

        payload = {
            "action": "sedaitest.sedaitest",
            "parameters": {
            "hostvalue": host_name
            }
        }

        response = requests.post(workflow_auto_url, json=payload, headers=headers)

        if response.status_code == 200:
            processed_data = response.json()
            return jsonify({'processed_data': processed_data}), 200
        else:
            return jsonify({'Error': 'Failed to fetch data from the workflow auto service'}), response.status_code



@app.route("/statusCheck", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

if __name__ == "__main__":
    app.run()