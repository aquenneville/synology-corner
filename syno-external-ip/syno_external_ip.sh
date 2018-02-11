#!#/bin/bash
EMAIL=$1
PORT=$2
IP=$(wget http://ipinfo.io/ip -qO -)
echo "external ip: https://${IP}:${PORT}" | /opt/bin/nail -s "Synology external ip" ${EMAIL}
