from flask import Flask, Response
import os, json

app = Flask(__name__)

def build_filepath(fileName:str) -> str:
    templates_path = "./resource/api_templates/test_{}.tpl"
    return templates_path.format(fileName)

def build_response(name: str) -> Response:
    templates_path = "./resource/api_templates/test_{}.tpl"
    with open(templates_path.format(name)) as f:
        return Response(f.read(), mimetype='application/json')

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

@app.route('/images', methods=['GET'])
def images_list():
    return build_response('image_query')

@app.route('/vswitches', methods=['GET'])
def vswitches_list():
    return build_response('vswitch_get')


@app.route('/vswitches/<name>', methods=['GET'])
def vswitch_query(name):
    return build_response('vswitch_query')



app.run()