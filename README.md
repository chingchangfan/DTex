# DTex
Usage: python3 scp_files.py local_ip=10.1.1.1 local_user='root' local_pass='abc123' remote_ip=10.1.1.2 \
remote_user='root' remote_pass='abc123' folder='/tmp'

python script to copy ~ /.ssh/known_hosts and ~/.ssh/authorized_keys files from your local Linux machine to a remote Linux machine. Your script should prompt the user to input the following or can be passed along as script parameters:
local machine IP
local machine username
local machine password
remote machine IP
remote machine username
remote machine password
folder location to place these files on the remote machine (if the directory doesn't exist, create one)
