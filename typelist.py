Lt = [2, 'unicorn', 1, 'glitter', 4, 3.2]
for i in Lt:
    isinstance (i, (str))
    isinstance (i, (int, float))
    if isinstance(i, (str, int)) is True:
        print "The list you entered is of mixed type"
    elif isinstance(i, str) is True:
        print "The list you entered is of string type"
        print "String: {}".format(str)
    elif isinstance(i, (int, float)) is True:
        print "The list you entered is of integer type"
        print sum([i for i in Lt if isinstance(i, (int, float))])