# -*- coding: utf-8 -*-

import glob
import os

#通过模式匹配来搜索文件, 当前目录下的
files = glob.glob("*.py")

print files

for filename in files:
    realpath = os.path.realpath(filename)
    print realpath



files = glob.glob("/Users/branw/Documents/*.txt")
print files



files = glob.iglob("*.py")
print files #<generator object iglob at 0x1083a9f00>

for filename in files:
    print filename

