__author__ = 'branw'

import os
import base64
import tempfile

from openstack import connection

import wsme
from wsme.rest import json as wsme_json


class Base(wsme.types.Base):

    def to_dict(self):
        return wsme_json.tojson(self.__class__, self)

    @classmethod
    def to_obj(cls, values):
        # wsme_json.fromjson cannot be used here because it doesn't work
        # correctly with read-only attributes (wsme raises exception that
        # read-only property is violated when fromjson is used).
        wsme_dict = {}
        for attribute in wsme.types.list_attributes(cls):
            value = values.get(attribute.name, wsme.types.Unset)
            if value and wsme.types.iscomplex(attribute.datatype):
                value = attribute.datatype(**value)
            wsme_dict[attribute.name] = value
        return cls(**wsme_dict)

    @classmethod
    def to_wsme_model(cls, obj):
        wsme_dict = {}
        for attribute in wsme.types.list_attributes(cls):
            value = getattr(obj, attribute.name, None)
            wsme_dict[attribute.name] = value
        return cls(**wsme_dict)

class Credentials(Base):
    auth_url = wsme.wsattr(str, mandatory=True)
    username = wsme.wsattr(str, mandatory=True)
    password = wsme.wsattr(str, mandatory=True)
    project = wsme.wsattr(str, mandatory=True)
    insecure = wsme.wsattr(bool, mandatory=True)
    domain = wsme.wsattr(str, mandatory=False)
    cacert = wsme.wsattr(str, mandatory=False)



def get_cafile(cacert, prefix_str):
    cafile = None
    if cacert:
        cert_content = base64.b64decode(cacert)
        fd, cafile = tempfile.mkstemp(dir="/Users/branw/Documents/onesafe/pystudy", prefix=prefix_str)
        os.write(fd, cert_content)
        os.close(fd)
    return cafile


def create_conn(credentials):
    cafile = get_cafile(credentials.cacert, "openstack_cert")
    try:
        print credentials
        conn = connection.Connection(auth_url=credentials.auth_url,
                                     username=credentials.username,
                                     password=credentials.password,
                                     project_name=credentials.project,
                                     verify= "/Users/branw/Documents/onesafe/pystudy/vio.crt",
                                     #verify= True,
                                     #verify= False if credentials.insecure else cafile,
                                     #cert=cafile,
                                     user_domain_name=credentials.domain,
                                     project_domain_name=credentials.domain)
    except Exception as e:
        raise e
    # finally:
    #     if cafile is not None:
    #         os.remove(cafile)
    return conn

credentials = Credentials()
credentials.auth_url = "http://10.111.88.103:35357/v3"
credentials.username = "admin"
credentials.password = "admin"
credentials.project = "admin"
credentials.insecure = False
credentials.cacert = "MIIDojCCAoqgAwIBAgIJAN+BgmWpSPTYMA0GCSqGSIb3DQEBCwUAMGYxCzAJBgNV\
BAYTAlVTMQswCQYDVQQIDAJDQTESMBAGA1UEBwwJUGFsbyBBbHRvMQ8wDQYDVQQK\
DAZWTXdhcmUxDDAKBgNVBAsMA1ZJTzEXMBUGA1UEAwwOMTAuMTExLjEwNi4xOTEw\
HhcNMTcwNDEyMDg1ODUyWhcNMjcwNDEwMDg1ODUyWjBmMQswCQYDVQQGEwJVUzEL\
MAkGA1UECAwCQ0ExEjAQBgNVBAcMCVBhbG8gQWx0bzEPMA0GA1UECgwGVk13YXJl\
MQwwCgYDVQQLDANWSU8xFzAVBgNVBAMMDjEwLjExMS4xMDYuMTkxMIIBIjANBgkq\
hkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwvs4OU+OUFt1cflgTQEWkSBwsmgiTB21\
h+qOiFtOGpA6StLHvss/hBlc8XDIWE+3OxLyMNSv9I5SYDnND37dzMfKpU3NHMIN\
+F2ud0AELt2o/pALZySV6cU7rFFRPdYCpFf0V5Vn+qeJOQoXN7zdH8LDAuWVaCdf\
LQXeGay+J7NMneYpLPww3xiMfiVNTYxTGMZPvOklgt1Vk/4PnL7P/Juh7SgYaphC\
HptceFVTMYltBl+vFmJrzq+SHkkgk99YeF8YckJaTpTWvHFDLpECYh8s7u6B1fnB\
VN/09/bULSHHIwgF2MImPuFnkZrAcwjlWt3ksC8tx1Veoig+yb1bvwIDAQABo1Mw\
UTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBSQI0kKb0GtlzaEVWGKMe32NoPFHDAV\
BgNVHREEDjAMhwQKb2q/hwQKb1hnMAsGA1UdDwQEAwICjDANBgkqhkiG9w0BAQsF\
AAOCAQEAd7FGlOJ0hsT9TsqwJjkLVTefSmReDkc3nUf4it3up/PdxjXvdWPilbUT\
d75SdVZw3zQm++vv2BwWl3QZEX2AleHOgXKVdWBhXNrZYtw11MYzZ+Kb6ZSEyIfV\
FtE6krmz8CsB04cs1xwwJ1cUyku2fOLkFYeLAWCeIVEVHpk0QVj2E9NJC3ZLPpPf\
tvWHFDhnrPNhYQIS9zChHi4ggU/P4G6PvFgNUwvOXMerI6W4xyuEXtxjKsWGocZx\
7570mTN31VPrC9/vuJC2f0YKigmfM7316pt4bN31I4z4i+fLPdRmVtmzTd4ONabG\
oGnptHcbIUIsY0qACJ26G3VNUhXQyQ=="


def authenticate():
    conn = create_conn(credentials)
    conn.authorize()
    token = conn.session.get_token()
    project_id = conn.session.get_project_id()
    print token
    print project_id
    print [img.name for img in conn.image.images()]


authenticate()