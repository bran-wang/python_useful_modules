import pickle

data1 = {
    'a' : [1,2,0,3,4+6j],
    'b' : {'string', u'Unicode string'},
    'c' : None
    }

ref_list = [1, 2, 3]

ref_list.append(data1)

output = open('data.pk1', 'wb')

#pickle.dump(data1, output)

pickle.dump(ref_list, output, pickle.HIGHEST_PROTOCOL)

output.close()


