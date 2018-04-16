import fnmatch 

rules=list()
with open('vikl.txt') as l:
    rules = l.readlines()
    l.close()
rules = [x.strip() for x in rules]

inp = open('text.txt','r')
srcText =''.join(inp.read())
inp.close()
sl = srcText.split(". ")
resList1 = srcText.split(". ")
resList2 = list()
for i in sl:
    modi = ''.join(i)
    lmodi = modi.split(" ")    
    print(i)
    for j in rules:        
        modj = ''.join(j)        
        print(modj)
        if(fnmatch.filter(lmodi, modj)):
            print("POPAVS")
            resList1.remove(i)            
            break
print("------------")       
for i in sl:
    modi = ''.join(i)
    lmodi = modi.split(" ")    
    print(lmodi)
    for j in rules:
        modj = ''.join(j)        
        print(modj)
        for s in fnmatch.filter(lmodi, modj):
            lmodi.remove(s)
    #print(lmodi)     
    res2 = ' '.join(lmodi)
    #print(res2) 
    resList2.append(res2)

#print(resList2)    
resText1 ='. '.join(resList1)
resText2 ='. '.join(resList2)
print("------------rules: ")    
print(rules)
print("------------res w/o sentences: ")   
print(resText1)
print("------------res w/o words: ")   
print(resText2)      
file1 = open("res1.txt", "w")
file1.write(resText1)
file1.close()

file2 = open("res2.txt", "w")
file2.write(resText2)
file2.close()
