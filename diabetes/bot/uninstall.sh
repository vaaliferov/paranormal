#!/usr/bin/env bash

APP=diabetes_bot
DIR=/opt/$APP
SERVICE=$APP.service

systemctl stop $SERVICE
systemctl disable $SERVICE
rm /etc/systemd/system/$SERVICE
systemctl daemon-reload
rm -rf $DIR