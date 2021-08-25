#!/usr/bin/env bash

systemctl stop paranormal_app.service
systemctl disable paranormal_app.service

rm -rf /opt/paranormal_app
rm /etc/systemd/system/paranormal_app.service

systemctl daemon-reload