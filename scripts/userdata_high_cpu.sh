#!/bin/bash

#Update system packages
yum update -y
#Install Git, Apache and mod_wsgi
yum install -y git
#Clone a repository
git clone https://github.com/cloudacademy/lab-utils.git
#Enter in the high_cpu folder - This is the folder where the app lives
cd lab-utils/apps/high_cpu
# Install requirements from requirements.txt
pip install -r requirements.txt
# Launch application
python cyclone.py
