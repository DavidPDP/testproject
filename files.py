from flask import Flask, abort, request
import json

from files_commands import get_all_files, add_file, remove_file, get_recently_files

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/files',methods=['POST'])
def create_file():
  contentJson = request.get_json(silent=True)
  filename = contentJson['filename']
  content  = contentJson['content']
  if not filename or not content:
    return "empty username or content", 400
  if add_file(filename,content):
    return "HTTP 201 CREATE", 201
  else:
    return "error while creating file", 400

@app.route(api_url+'/files',methods=['GET'])
def read_file():
  list = {}
  list["files"] = get_all_files()
  return json.dumps(list), 200

@app.route(api_url+'/files',methods=['PUT'])
def update_file():
  return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/files',methods=['DELETE'])
def delete_file():
  error = False
  error = remove_file()
  if error:
    return 'HTTP 200 OK', 200
  else:
    return 'HTTP 400 error', 400

@app.route(api_url+'/files/recently_created',methods=['GET'])
def read_recent_file():
  list = {}
  list["files"] = get_recently_files()
  return json.dumps(list), 200

@app.route(api_url+'/files/recently_created',methods=['POST'])
def create_recent_file():
  return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/files/recently_created',methods=['PUT'])
def update_recent_file():
  return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/files/recently_created',methods=['DELETE'])
def delete_recent_files():
  return "HTTP 404 NOT FOUND", 404


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
