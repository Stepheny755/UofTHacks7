import json,requests
from flask import Flask,request

app = Flask('main')

@app.route('/')
def main():
    temp = {'id':123456789,'name':'CarePath','value':'test'}
    return json.dumps(temp)
    #return 'hello world'

@app.route('/getmethod')
def post_json():
    temp = {'id':123456789,'name':'CarePath','value':'test'}
    return json.dumps(temp)

Flask.run(app,host="167.99.186.154")
