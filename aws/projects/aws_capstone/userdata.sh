#!/bin/bash
apt-get update -y
apt-get install git -y
apt-get install python3 -y
cd /home/ubuntu/
TOKEN="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"
git clone https://$TOKEN@github.com/maximkim-create/aws_capstone.git
cd /home/ubuntu/aws_capstone
apt install python3-pip -y
apt-get install python3.7-dev libmysqlclient-dev -y
pip3 install -r requirements.txt
cd /home/ubuntu/aws_capstone/src
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:80