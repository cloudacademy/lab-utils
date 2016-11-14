#!/bin/bash

#Update system packages
yum update -y
#Install Git
yum install -y git
#Clone a repository
git clone https://github.com/cloudacademy/lab-utils.git
#Enter in the cats folder - This is the folder where the app lives
cd lab-utils/apps/puppies/cats
# Install requirements from requirements.txt
pip install -r requirements.txt
# Launch application
python cyclone.py
