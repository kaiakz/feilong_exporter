from flask import Flask, Response, request, make_response, jsonify
import os, json

app = Flask(__name__)

# Build the path for file that is requested
def build_filepath(fileName:str) -> str:
    templates_path = "./resource/api_templates/test_{}.tpl"
    return templates_path.format(fileName)

# Build a simple reponse by the template file
def build_response(name: str) -> Response:
    templates_path = "./resource/api_templates/test_{}.tpl"
    with open(templates_path.format(name)) as f:
        return Response(f.read(), mimetype='application/json')

# zvm-sdk's REST API mocking
# https://cloudlib4zvm.readthedocs.io/en/latest/restapi.html


@app.route('/token', methods=['POST'])
def token():
    # request.header.get('X-Admin-Token')
    response = make_response()
    response.headers['X-Auth-Token'] = 'ThisIsFakeToken'
    return response

@app.route('/', methods=['GET'])
def version():
    return build_response('version')

@app.route('/host', methods=['GET'])
def host_info():
    return build_response('host_info')

@app.route('/host/diskpool', methods=['GET'])
def host_disk_info():
    return build_response('host_disk_info')

@app.route('/guests', methods=['GET'])
def guests_list():
    return build_response('guests_list')  

@app.route('/guests/<userid>/info', methods=['GET'])
def guest_info(userid):
    return build_response('guest_get_info')  

@app.route('/images', methods=['GET'])
def images_list():
    return build_response('image_query')

@app.route('/vswitches', methods=['GET'])
def vswitches_list():
    return build_response('vswitch_get')


@app.route('/vswitches/<name>', methods=['GET'])
def vswitch_query(name):
    with open(build_filepath('vswitch_query')) as f:
        info = json.load(f)
        info['output']['switch_name'] = name    # Set switch_name to the parameter called name
        return jsonify(info)


app.run(port=8909)