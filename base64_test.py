import base64

str = "i am a handsome boy"
b64str = base64.b64encode(str)
print "base 64 encode str is: {}".format(b64str)

origin_str = base64.b64decode(b64str)
print "origin str is: {}".format(origin_str)
