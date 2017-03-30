import pprint, pickle


pk1_file = open('data.pk1', 'rb')

data1 = pickle.load(pk1_file)

pprint.pprint(data1)

pk1_file.close()
