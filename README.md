
  # COLLEGE ERP

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

A Python based Django Application for enterprise to manage college records and reports.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
sudo apt-get install libmysqlclient-dev
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
pip install -r requirements.txt
```
change setting.py for mysqlserver 
```
python manage.py migrate 
python manage.py runserver
```

End with an example of getting some data out of the system or using it for a little demo.

to install mysql 
```
sudo apt install default-mysql-server default-mysql-client
```
after that create new user and password with database 
```
sudo mysql
mysql > CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
mysql > CREATE DATABASE erp_project;
mysql > GRANT ALL PRIVILEGES ON erp_project.* TO 'admin'@'localhost';
```

change creadentials in settings.py as
host = localhost
name / database = erp_project
user = admin
password =password


using Autostud.py
```
python3 Autostud.py <numberOfstudents>
```
## Usage <a name = "usage"></a>

Add notes about how to use the system.
<br>
![ERP_snapshot2](https://user-images.githubusercontent.com/59028345/115144907-c2338300-a06c-11eb-8ba8-b3106a1c0ed3.jpeg)
![ERP_snapshot1](https://user-images.githubusercontent.com/59028345/115144915-c6f83700-a06c-11eb-9724-ba3787620f9e.jpeg)
