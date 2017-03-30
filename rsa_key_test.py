from Crypto.PublicKey import RSA

def generate_keys():
    key = RSA.generate(4096)
    encoded_private_key = key.exportKey('PEM')
    public_key = key.publickey()
    encoded_public_key = public_key.exportKey('OpenSSH')
    return encoded_private_key, encoded_public_key


private_key, public_key = generate_keys()

print private_key
print public_key
