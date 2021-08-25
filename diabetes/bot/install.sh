#!/usr/bin/env bash

if [ "$#" -eq 0 ]; then exit 1; fi

systemctl stop diabetes_bot.service
systemctl disable diabetes_bot.service
rm /etc/systemd/system/diabetes_bot.service
rm -rf /opt/diabetes_bot

USER=$1

sed -i "s/<user>/$USER/g" bot.service

mkdir /opt/diabetes_bot
chown $USER /opt/diabetes_bot
chmod 755 /opt/diabetes_bot
cp -r . /opt/diabetes_bot

cp bot.service /etc/systemd/system/diabetes_bot.service

apt install $(cat apt.txt)
apt install python3-venv
pip3 install virtualenv
python3 -m venv /opt/diabetes_bot/env
source /opt/diabetes_bot/env/bin/activate
pip3 install -r requirements.txt
deactivate

systemctl daemon-reload
systemctl start diabetes_bot.service
systemctl enable diabetes_bot.service