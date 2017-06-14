import re


res = re.match('com', 'jcomwww')
if res is not None:
    print res.group()


res = re.search(r".*", 'jcomwww')
if res is not None:
    print "search ", res.group()

#escape = re.escape("bran-share")
#escape = re.escape("datastore(7)")
#print escape
#res = re.compile(escape)
res = re.compile("bran-share|datastore\(7\)")
ok = res.match("bran-sharejjj")
if ok is not None:
    print "ok is ", ok.group()

ok = res.match("datastore(7)777")
if ok is not None:
    print "ok is ", ok.group()
