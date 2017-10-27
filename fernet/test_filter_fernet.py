__author__ = 'branw'

import binascii
import codecs

from ansible import errors
from cryptography.fernet import Fernet

key = Fernet.generate_key()

def fernet_encrypt(value, key):
    fernet = Fernet(key.encode())
    encoded = 'fernet' + fernet.encrypt(value.encode())

    try:
        return codecs.encode(encoded, 'base64').replace('\n', '')
    except binascii.Error:
        raise errors.AnsibleFilterError('base64 encoding error: %s' % str(e))

print key
print fernet_encrypt("come on", key)
