import tempfile
import os

fd, os_path = tempfile.mkstemp(prefix="os_test")

os.write(fd, "test tempfile over")
os.close(fd)


print "os_path is: {}".format(os_path)

with open(os_path) as fd:
    print(fd.read())
