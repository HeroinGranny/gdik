def getListFromFile(fileName):
    return list(map(str.strip, list(open(fileName, "r").readlines())))
def sortL(l):
    l.sort()
    return l
def extendL(l1, l2):
    l1.extend(l2)
    return l1
print(sortL(getListFromFile("mas1.txt")))
print(sortL(getListFromFile("mas2.txt")))
print(sortL(extendL(sortL(getListFromFile("mas1.txt")),sortL(getListFromFile("mas2.txt")))))

