#!/bin/bash

# Define the bastion server
BASTION_USER="cc"
BASTION_IP="129.114.27.250"  # Bastion IP
BASTION_KEY="/home/parallels/.ssh/F24_BASTION.pem"  # Ensure this path is correct

# Define the target server (VM4)
TARGET_USER="cc"
TARGET_IP="192.168.5.128"  # The correct internal IP for VM4
TARGET_KEY="/home/parallels/.ssh/Team2_Key.pem"  # Ensure this path is correct

# Execute the SSH connection using the bastion server as a proxy
ssh -o ProxyCommand="ssh -i $BASTION_KEY -W %h:%p $BASTION_USER@$BASTION_IP" -i $TARGET_KEY $TARGET_USER@$TARGET_IP
