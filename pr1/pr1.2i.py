def getListFromFile(fileName):
    l = list()    
    file = open(fileName, "r")
    l= file.readlines()
    file.close()
    l = [x.strip() for x in l]
    l.sort()
    return l
print(getListFromFile("mas1.txt"))
print(getListFromFile("mas2.txt"))
l = list()
l.extend(getListFromFile("mas1.txt"))
l.extend(getListFromFile("mas2.txt"))
l.sort()
print(l)
