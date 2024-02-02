import os,glob
from flask import *
import json
from jinja2 import Template

app = Flask(__name__)
@app.route("/") 

def web(): 
    data = []
    for filename in glob.glob(os.path.join("files/", "*")):
        with open(filename) as json_file:
                json_data = json.load(json_file)
        data.append(json_data)

    return render_template('web.html', data_list=data)