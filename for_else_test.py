def test():
    dc = [1, 2, 3, 4]
    for i in dc:
        print i
        if i == "5":
            break
    else:
        print i
        if i == "4":
            print "is 4"
        else:
            print "not 5"


if __name__ == "__main__":
    test()


#OUTPUT:
#1
#2
#3
#4
#4
#not 5

