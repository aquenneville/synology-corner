#!/bin/bash

DESTINATION_PATH='/volume1/photo'
MOBILE_IP='192.168.1.54';
export SOURCE_PATH_1='/storage/503D-6F41/WhatsApp\ Images'
export SOURCE_PATH_2='/storage/503D-6F41/Camera'
export SOURCE_PATH_3='/storage/503D-6F41/DCIM/Camera'

#1. Download, install & start sshhelper on your mobile (port 2222)
echo "Copying your photos on your mobile to your synology DSM into ${DESTINATION_PATH}";
echo "Currently your mobile ip is: ${MOBILE_IP}";

# TODO update the mobile ip

cd ${DESTINATION_PATH} || exit;
scp -P 2222 user1@${MOBILE_IP}:"${SOURCE_PATH_1}/*" .
scp -P 2222 user1@${MOBILE_IP}:"${SOURCE_PATH_2}/*" .
scp -P 2222 user1@${MOBILE_IP}:"${SOURCE_PATH_3}/*" .

#remove pictures older than 3 months
#ssh -p 2222 user1@${MOBILE_IP} `find '${SOURCE_PATH_1}' \( -name "\*.jpg" -o -name "\*.png" \) -type f -mtime 90 -delete`
#ssh -p 2222 user1@${MOBILE_IP} `find '${SOURCE_PATH_2}' \( -name "\*.jpg" -o -name "\*.png" \) -type f -mtime 90 -delete`
#ssh -p 2222 user1@${MOBILE_IP} `find '${SOURCE_PATH_3}' \( -name "\*.jpg" -o -name "\*.png" \) -type f -mtime 90 -delete`