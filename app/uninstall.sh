#!/usr/bin/env bash
systemctl stop paranormal_app.service
systemctl disable paranormal_app.service
rm /etc/systemd/system/paranormal_app.service
rm -rf /opt/paranormal_app
systemctl daemon-reload