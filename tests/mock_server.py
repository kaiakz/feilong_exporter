from flask import Flask, Response
import os, json

app = Flask(__name__)


def build_filepath(name:str) -> str:
    templates_path = "./resource/api_templates/test_{}.tpl"
    return templates_path.format(name)

@app.route('/', methods=['GET'])
def version():
    with open(build_filepath('version')) as f:
        return Response(f.read(), mimetype='application/json')

@app.route('/host', methods=['GET'])
def host_info():
    with open(build_filepath('host_info')) as f:
        return Response(f.read(), mimetype='application/json')

@app.route('/guests', methods=['GET'])
def guests_list():
    with open(build_filepath('guests_list')) as f:
        return Response(f.read(), mimetype='application/json')    




app.run()