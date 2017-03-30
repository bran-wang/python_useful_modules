import pwd
import logging

LOG = logging.getLogger(__name__)

def get_uid_and_gid(username):
    uid = -1
    gid = -1
    try:
        pwdun = pwd.getpwnam(username)
        uid = pwdun.pw_uid
        gid = pwdun.pw_gid
    except KeyError:
        LOG.debug("User '%s' does not exist!" % username)
    return uid, gid



b_uid, b_gid = get_uid_and_gid("wyp")
print b_uid, b_gid
