# ztp_server

A small ztp_Server written in python with flask that allows to onboard IOS-XE devices

![Image of ztp process](https://i.ibb.co/hmJgyCk/ztp-server.png)



## Requirements
Flask==2.0.3

Jinja2==3.0.3

PyYAML==6.0

## Installation

``` 
git clone https://github.com/kapsch-network-solution/ztp_server.git
cd ztp_server
```

Create virtual enviroment (optional)

``` 
python3 -m venv ztp_server
source ztp_server/bin/activate
```

install dependencies

```
pip install -r requirements.txt 
```


## Run Flask webservice

```
export FLASK_APP=main
export FLASK_ENV=development
flask run --host=0.0.0.0
```

## Backend files

templates/host_vars/<devicename>.yml

```
ansible_host: 100.64.0.101
  
#ztp_sn is mandatory
ztp_sn: 9GLRGDOQH9H
  
#ztp_template is mandatory and file 
#templates/template_<templatename>.tmpl must exits
ztp_template: csr1000v
  
#all other ztp_ entries can be difined as you wish
ztp_interface:  gi1
ztp_ip: 100.64.0.101
ztp_mask: 255.255.255.0
ztp_gw: 100.64.0.1
loopback_ip: 1.1.1.1
```


 
