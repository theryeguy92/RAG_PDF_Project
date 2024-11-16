#!/bin/bash

# Define the server (Just plug in the IP)
BASTION_USER="cc"
BASTION_IP="129.114.27.250" # Bastion IP
BASTION_KEY="/home/parallels/.ssh/F24_BASTION.pem"

# Target server
TARGET_USER="cc"
TARGET_IP="192.168.5.133" # NOTE: Plug in the IP of the VM
TARGET_KEY="/home/parallels/.ssh/Team2_Key.pem"

# Define the file to upload and the destination path on the VM
LOCAL_FILE_PATH="/home/ryan/team_2_pdf_final_project/yaml_files_k8/zookeeper-deployment.yaml" # CHANGE THIS TO THE FILE YOU WANT
REMOTE_DESTINATION="/home/cc/zookeeper" # CHANGE THIS IF YOU WANT TO UPLOAD FILES

# Use scp with ProxyCommand to upload the file via the bastion server
scp -o ProxyCommand="ssh -i $BASTION_KEY -W %h:%p $BASTION_USER@$BASTION_IP" -i $TARGET_KEY $LOCAL_FILE_PATH $TARGET_USER@$TARGET_IP:$REMOTE_DESTINATION
