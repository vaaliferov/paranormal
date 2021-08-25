#!/usr/bin/env bash

if [ "$#" -eq 0 ]; then exit 1; fi

systemctl stop melanoma_bot.service
systemctl disable melanoma_bot.service
rm /etc/systemd/system/melanoma_bot.service
rm -rf /opt/melanoma_bot

USER=$1

sed -i "s/<user>/$USER/g" bot.service

mkdir /opt/melanoma_bot
chown $USER /opt/melanoma_bot
chmod 755 /opt/melanoma_bot
cp -r . /opt/melanoma_bot

cp bot.service /etc/systemd/system/melanoma_bot.service

pip3 install gdown
gdown --id 1KNeRnzxYF4X-DhvFfL_mrMDabWnTrPmg -O /opt/melanoma_bot/model.onnx

apt install $(cat apt.txt)
apt install python3-venv
pip3 install virtualenv
python3 -m venv /opt/melanoma_bot/env
source /opt/melanoma_bot/env/bin/activate
pip3 install -r requirements.txt
deactivate

systemctl daemon-reload
systemctl start melanoma_bot.service
systemctl enable melanoma_bot.service