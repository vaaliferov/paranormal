#!/usr/bin/env bash

if [ "$#" -eq 0 ]; then exit 1; fi

USER=$1

sed -i "s/<user>/$USER/g" app.service

mkdir /opt/paranormal_app
chown $USER /opt/paranormal_app
chmod 755 /opt/paranormal_app
cp . /opt/paranormal_app

cp app.service /etc/systemd/system/paranormal_app.serivce

apt install python3-venv
pip3 install virtualenv
python3 -m venv /opt/paranormal_app/env
source /opt/paranormal_app/env/bin/activate
pip3 install -r requirements.txt
deactivate

systemctl daemon-reload
systemctl start paranormal_app.service
systemctl enable paranormal_app.service