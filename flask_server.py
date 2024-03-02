import requests
import flask
from flask import Flask
import json 

app = Flask(__name__)

# api-endpoint
URL = "https://1xappospsd.execute-api.us-east-2.amazonaws.com/dev"
 


@app.route("/sayHello", methods=['GET'])
def get_random_number():
    name = flask.request.args.get('name')

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'name': name}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
     
    # extracting data in json format
    data = r.json()
    return data


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

