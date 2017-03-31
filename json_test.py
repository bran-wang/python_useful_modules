import json

data = { "spam" : "foo", "numbers" : 1.2, "none" : None, "tuple" : (1,2,3), "True" : True }

in_json = json.dumps(data)

print "-------json.dumps--------"
print "json object from python is: ", in_json
print "-------------------------\n"

str_from_json = json.loads(in_json)

print "------json.loads----------"
print "Python object from json is: ", str_from_json
print "-------------------------"

with open('output.json', 'w') as fp:
    json.dump(data, fp)

with open('output.json', 'r') as fp:
    out_from_file = json.load(fp)
    print "-------------------------"
    print "out from file is: ", out_from_file
