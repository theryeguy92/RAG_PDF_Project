#!/bin/bash

# Define variables for bastion and target servers
BASTION_USER="cc"
BASTION_IP="129.114.27.250" # Bastion IP
BASTION_KEY="~/.ssh/F24_BASTION.pem"

TARGET_USER="cc"
TARGET_IP="192.168.5.133" # Target VM IP
TARGET_KEY="~/.ssh/key_team2.pem"

# Define the source and destination directories
SOURCE_DIR="/home/cc/"
DEST_DIR="/home/ryan/not_git"

# Run scp command with ProxyCommand option
scp -r -o ProxyCommand="ssh -i $BASTION_KEY -W %h:%p $BASTION_USER@$BASTION_IP" -i $TARGET_KEY ${TARGET_USER}@${TARGET_IP}:${SOURCE_DIR} ${DEST_DIR}
