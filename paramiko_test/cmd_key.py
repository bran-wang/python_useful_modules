import paramiko

private_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.160.134.103', 22, 'root', key)

stdin, stdout, stderr = ssh.exec_command('df')
print stdout.read()
ssh.close()
