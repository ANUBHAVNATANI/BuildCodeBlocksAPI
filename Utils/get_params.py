"""
This file get the params and set it for the model and then use all the other properties to make the python file compile
"""
import requests
resp = requests.get("URL")
if resp.status_code != 200:
    print("Error")
for things in resp.json():
    print('{} {}'.format(things['modelName'], things['params']))
