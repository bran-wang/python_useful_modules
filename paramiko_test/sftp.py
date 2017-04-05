import os,sys
import paramiko

t = paramiko.Transport(('10.160.134.103',22))
t.connect(username='root',password='123')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test.py','/tmp/test.py') 
t.close()



t = paramiko.Transport(('10.160.134.103',22))
t.connect(username='root',password='123')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test.py','/tmp/test2.py')
t.close()
