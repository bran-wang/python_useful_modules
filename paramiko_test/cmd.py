#!/usr/bin/env python
#coding: utf-8


import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.160.134.103', 22, 'root', 'you guess')
stdin, stdout, stderr = ssh.exec_command('df')

print stdout.read()
ssh.close()
