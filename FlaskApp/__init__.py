from flask import Flask, jsonify, request
import requests
import logging

app = Flask(__name__)

@app.route("/performAction", methods=['POST'])
def performAction():

    workflow_auto_url = 'https://rngnbyyii56mqwsffdwlnkwawq0zxjfd.lambda-url.us-east-1.on.aws/'

    response = requests.post(workflow_auto_url, json=request.json)


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