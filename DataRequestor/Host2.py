import os,glob
from flask import *
import json
from jinja2 import Template

app = Flask(__name__)
@app.route("/") 

def hello_world(): 
    data = []
    for filename in glob.glob(os.path.join("Data/", "*")):
        with open(filename) as json_file:
                json_data = json.load(json_file)
        data.append(json_data)

    return render_template('index1.html', data_list=data)