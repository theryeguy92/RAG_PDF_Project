#!/bin/bash

# Define the server (Just plug in the IP)
BASTION_USER="cc"
BASTION_IP="129.114.27.250" # Bastion IP
BASTION_KEY="/home/parallels/.ssh/F24_BASTION.pem"

# Target server
TARGET_USER="cc"
TARGET_IP="192.168.5.140" # NOTE: Plug in the IP of the VM
TARGET_KEY="/home/parallels/.ssh/key_team2.pem"

# Execute the SSH connection
ssh -o ProxyCommand="ssh -i $BASTION_KEY -W %h:%p $BASTION_USER@$BASTION_IP" -i $TARGET_KEY $TARGET_USER@$TARGET_IP