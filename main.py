from flask import Flask, request
from flask import render_template
import yaml
import os

# This is the directory where a yaml file for every device should be located.
ansible_host_dir = "./host_vars"

app = Flask('__name__')

@app.route('/')
def hello():
    return 'Info coming soon'

@app.route('/get-config')
def get_config():

   device = request.args.get('device')

   if device is None:
       return "No device input given" 
   else:
       data = device.split(',') 

       for filename in os.listdir(ansible_host_dir):
           with open(os.path.join(ansible_host_dir, filename), 'r') as file: 
               device = yaml.load(file, Loader=yaml.FullLoader)

           if device['ztp_sn'] == data[1][3:]:
               return render_template("template_" + device['ztp_template']+".tmpl",device_data=device)

       return "err_no_config"

@app.route('/ztp.py')
def ztp():
    return render_template('template_ztp_script.tmpl',server=request.host)

@app.route('/ztp3.py')
def ztp3():
    return render_template('template_ztp_script_3.tmpl',server=request.host)
