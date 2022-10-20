def testRead():
    fp = open('testReadMethod.txt', "r")
    print(fp.read())
    fp.close()

def testReadline():
    fp = open("testReadMethod.txt", "r")
    print(fp.readline())
    fp.close()

def testReadlines():
    fp = open("testReadMethod.txt", "r")
    print(fp.readlines())
    fp.close()

testRead()
testReadline()
testReadlines()