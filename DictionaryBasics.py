AboutMe = {
    'name': 'Youngmee',
    'age': '32',
    'birth Country': 'United States of America',
    'favorite language': 'Python'
}
def readDict():
    for key, val in AboutMe.iteritems():
        print "My {} is {}".format(key, val)

readDict()