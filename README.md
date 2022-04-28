# ztp_server

A small ztp_Server written in python with flask that allows to onboard IOS-XE devices

![Image of ztp process](https://ibb.co/9n4nd9J)



## Requirements
netmiko==3.2.0

paramiko==2.7.1

prettytable==0.7.2

pyaml==20.4.0

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


## Flask

export FLASK_APP=main
export FLASK_ENV=development
flask run --host=0.0.0.0
