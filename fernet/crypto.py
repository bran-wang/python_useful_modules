#!/usr/bin/env python
# encoding: utf-8
import os
import codecs
import binascii

from cryptography.fernet import Fernet

def get_fernet_key():
  if not os.path.isfile("test.fernet"):
    with open("test.fernet", "w") as f:
      f.write(Fernet.generate_key())
  with open("test.fernet") as f:
    read_data = f.read()
  return read_data

def encrypt(raw_data):
  key = get_fernet_key()
  fernet = Fernet(key.encode())
  encoded = 'fernet ' + fernet.encrypt(raw_data.encode())
  try:
    return codecs.encode(encoded, 'base64').replace('\n', '')
  except binascii.Error as e:
    raise exceptions.Invalid("base64 encoding error: {}".format(str(e)))

def decrypt(encrypted_data):
  try:
    decoded = codecs.decode(encrypted_data.encode(), 'base64')
  except binascii.Error as e:
    raise exceptions.Invalid("base64 decoding error: %s" % str(e))

  key = get_fernet_key()
  (encoding, data) = tuple(decoded.split())
  if encoding == 'fernet':
    fernet = Fernet(key.encode())
    return fernet.decrypt(data)
  else:
    raise exceptions.Invalid("invalid encoding: %s" % encoding)


data = encrypt("hello branw")
print data

data = decrypt("ZmVybmV0IGdBQUFBQUJhb0thSXBLVUs0OHFFMUZUdDJ2eWIyREFScTlhdVRhelBJUVpWQm9xN0dOWTRYVnh0aU9qT3JnTmNyeXgtVHF0Z0NkNno1VFBLVno0NUhPMk9HbUtYeTNaR1VRPT0=")
print data
