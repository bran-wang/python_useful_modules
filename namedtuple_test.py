from collections import namedtuple


BranInfo = namedtuple('BranInfo', ['url', 'sex', 'girl'])

bi = BranInfo("www.serven-kingdom.com", "man", "Searcy")

print bi
print bi.url
print bi.sex
print bi.girl


def who_love_john():
    who = namedtuple("who", ["first_name", "last_name", "words"])
    return who("John", "Snow", "You know nothing")

a_women = who_love_john()
print a_women
print "-----------------------------------"
print a_women.first_name, a_women.last_name, ", ",  a_women.words
print "-----------------------------------"
