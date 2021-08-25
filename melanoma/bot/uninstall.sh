#!/usr/bin/env bash
systemctl stop melanoma_bot.service
systemctl disable melanoma_bot.service
rm /etc/systemd/system/melanoma_bot.service
rm -rf /opt/melanoma_bot
systemctl daemon-reload