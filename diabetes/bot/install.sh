#!/usr/bin/env bash

USAGE='usage: sudo ./install.sh <name> <user> <token> <owner>'
if [ $# != 4 ]; then echo $USAGE; exit 1; fi

NAME=$1; USER=$2; TOKEN=$3; OWNER=$4

DIR="/opt/${NAME}_bot"

BOT_SERVICE="${NAME}_bot.service"
BOT_SERVICE_PATH=/etc/systemd/system/$BOT_SERVICE

systemctl stop $BOT_SERVICE
systemctl disable $BOT_SERVICE

rm -rf $DIR
rm $BOT_SERVICE_PATH

mkdir $DIR
cp -r . $DIR

cp bot.service $BOT_SERVICE_PATH
sed -i "s/<name>/$NAME/g" $BOT_SERVICE_PATH
sed -i "s/<user>/$USER/g" $BOT_SERVICE_PATH
sed -i "s/<owner>/$OWNER/g" $BOT_SERVICE_PATH
sed -i "s/<token>/$TOKEN/g" $BOT_SERVICE_PATH

apt install $(cat apt.txt)
apt install python3-venv
pip3 install virtualenv
python3 -m venv $DIR/env
source $DIR/env/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
deactivate

chown -R $USER:$USER $DIR
chmod 755 $DIR

systemctl daemon-reload

systemctl start $BOT_SERVICE
systemctl enable $BOT_SERVICE