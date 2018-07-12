from flask import Flask
import requests
import json
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
  url = os.environ['MSI_ENDPOINT'] + "/?resource=https://vault.azure.net&api-version=2017-09-01"
  # return await client.GetAsync(String.Format("{0}/?resource={1}&api-version={2}", Environment.GetEnvironmentVariable("MSI_ENDPOINT"), resource, apiversion));
  response = requests.get('http://google.com',  headers={"Secret":os.environ("MSI_SECRET")})
  json_data = json.loads(response.text)
  return json_data

if __name__ == '__main__':
  app.run()
