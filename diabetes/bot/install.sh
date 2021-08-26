#!/usr/bin/env bash

if [ "$#" -eq 0 ]; then exit 1; fi

USER=$1
APP=diabetes_bot
DIR=/opt/$APP
SERVICE=$APP.service

systemctl stop $SERVICE
systemctl disable $SERVICE
rm /etc/systemd/system/$SERVICE
rm -rf $DIR

sed -i "s/<user>/$USER/g" bot.service

mkdir $DIR
chown $USER $DIR
chmod 755 $DIR
cp -r . $DIR

cp bot.service /etc/systemd/system/$SERVICE

apt install $(cat apt.txt)
apt install python3-venv
pip3 install virtualenv
python3 -m venv $DIR/env
source $DIR/env/bin/activate
pip3 install -r requirements.txt
deactivate

systemctl daemon-reload
systemctl start $SERVICE
systemctl enable $SERVICE