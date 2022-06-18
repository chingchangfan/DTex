#!/usr/bin/env python


import paramiko
import time
import sys


def copy_files(**kwargs):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connect to " + kwargs['remote_ip'])
    try:
        ssh.connect(kwargs['remote_ip'],
                    username=kwargs['remote_user'],
                    password=kwargs['remote_pass'],
                    port=22,
                    banner_timeout=120)
    except Exception as e:
        print("Can't access host {}: {}".format(kwargs['remote_ip'], str(e)))
        return
    ssh.exec_command("mkdir -p " + kwargs['folder'])
    channel = ssh.invoke_shell()
    channel.recv(9999)
    for file in ['~/.ssh/known_hosts', '~/.ssh/authorized_keys']:
        print("Copy {} from {} to {}".format(file, kwargs['local_ip'], kwargs['remote_ip']))
        channel.send('scp -o StrictHostKeyChecking=no {}@{}:{} {}/.\n'.format(
            kwargs['local_user'], kwargs['local_ip'], file, kwargs['folder']))
        while not channel.recv_ready():
            time.sleep(3)
        out = channel.recv(9999).decode("ascii")
        if 'password:' in out:
            print(out)
        else:
            print("Can't SCP from {} to {}: {}".format(kwargs['remote_ip'], kwargs['local_ip'], out))
            return
        channel.send(kwargs['local_pass'] + '\n')
        while not channel.recv_ready():
            time.sleep(3)
        out = channel.recv(9999).decode("ascii")
        if '100%' in out:
            print(out)
        else:
            print("Can't SCP from {} to {}: {}".format(kwargs['remote_ip'], kwargs['local_ip'], out))
            return
        channel.send('\n')
    ssh.close()


if __name__ == '__main__':
    usage = "\nUsage: python3 scp_files.py local_ip=10.1.1.1 local_user='root' local_pass='abc123' remote_ip=10.1.1.2 \
remote_user='root' remote_pass='abc123' folder='/tmp'\n"
    if len(sys.argv) == 1:
        print(usage)
        exit()
    kwargs = {}
    for x in sys.argv[1:]:
        key, value = x.split('=')
        kwargs[key] = value
    copy_files(**kwargs)
