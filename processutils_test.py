from oslo_concurrency import processutils as putils

# you need copy id_rsa.pub to remote host
# you create file test_processutils on  remote host
# simple try cmd on remote host

private_key = '/home/wyp/.ssh/id_rsa'
remote_user = 'root'
remote_ip = '10.117.170.20'

stdout, stderr = putils.trycmd(
        'ssh', '-i', private_key,
        '%s@%s' % (remote_user, remote_ip),
        "touch /root/test_processutils",
        log_errors=putils.LOG_ALL_ERRORS,
        env_variables=None
    )

if stderr:
    print("Error, %s", stderr)

