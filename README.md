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

### templates/host_vars/<devicename>.yml

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

### templates/template_<templatename>.tmpl

all attributes from device yml can be used for rendering (device_data.<attributename>) 
````
!config template for 1000v with serial {{ device_data.ztp_sn}}

int {{ device_data.ztp_interface}}
no shut
ip add {{ device_data.ztp_ip}} {{ device_data.ztp_mask}}

ip route 0.0.0.0 0.0.0.0 {{ device_data.ztp_gw}}

hostname router

ip domain-name lab.local

crypto key generate rsa mod 2048

aaa new-model
aaa authentication login default local
aaa authentication enable default none

username admin secret cisco

line vty 0 15
privilege level 15
```

### templates/template_<templatename>.tmpl
 
