#!/usr/bin/env bash
systemctl stop diabetes_bot.service
systemctl disable diabetes_bot.service
rm /etc/systemd/system/diabetes_bot.service
rm -rf /opt/diabetes_bot
systemctl daemon-reload