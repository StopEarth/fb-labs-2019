indexlist_test = [0,0,1,0,0,0,0,1,0,0,0,0,0]
indexlist_1 = [1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1]
indexlist_2 = [0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1]
def createIndexListLRZ(indexlist):
    indexlist_LRZ = []
    for i in range(len(indexlist)-1):
        indexlist_LRZ.append(0)
    indexlist_LRZ.append(1)
    return indexlist_LRZ

def createLRZ(indexlist):
    LRZ = createIndexListLRZ(indexlist)
    forcheck = list(LRZ)
    counter = 0
    while 1:
        forcheck_2 = list(LRZ)
        counter += 1
        forswap = indexlist[-1]*LRZ[-1]
        for i in range(0,len(indexlist)-1):
            forswap += indexlist[i]*LRZ[i]
            LRZ[i] = forcheck_2[i+1]
        LRZ[i] = forswap % 2
        if LRZ == forcheck:
            break
    return counter
    
def createLRZforA(indexlist):
    LRZ = createIndexListLRZ(indexlist)
    forcheck = list(LRZ)
    counter = 0
    listforA = list(LRZ)
    while 1:
        forcheck_2 = list(LRZ)
        counter += 1
        forswap = indexlist[-1]*LRZ[-1]
        for i in range(len(indexlist)-1):
            forswap += indexlist[i]*LRZ[i]
            LRZ[i] = forcheck_2[i+1]
        LRZ[i] = forswap % 2
        listforA.append(forswap % 2)
        if LRZ == forcheck:
            break
    return listforA

def autoCor(indexlist):
    T = createLRZ(indexlist)
    listforA = createLRZforA(indexlist)
    for i in range(11):
        A = 0
        for j in range(T):
            A += (listforA[j] + listforA[(j+i)%T]) % 2
        print('A(',i,') = ',A)
        
def dictForK_grams(indexlist):
    n = len(indexlist)
    dictK = {}
    for i in range(4,int('1'*6,2) + 1):
        dictK[str(bin(i)[3:])] = 0
    return dictK

def bigramCount(indexlist):
    text = createLRZforA(indexlist)
    k_gramDict = dictForK_grams(indexlist)
    for position in range(0,len(text)-1,2):
        k_gramDict[str(text[position])+str(text[position+1])] += 1
    for position in range(0,len(text)-2,3):
        k_gramDict[str(text[position])+str(text[position+1])+str(text[position+2])] += 1
    for position in range(0,len(text)-3,4):
        k_gramDict[str(text[position])+str(text[position+1])+str(text[position+2])+str(text[position+3])] += 1
    for position in range(0,len(text)-4,5):
        k_gramDict[str(text[position])+str(text[position+1])+str(text[position+2])+str(text[position+3])+str(text[position+4])] += 1
    for elem in k_gramDict:
        k_gramDict[elem]/= len(text)//len(elem)
    print(k_gramDict)
шу
print('T for 1 = ',createLRZ(indexlist_1))
print('A for 1')
autoCor(indexlist_1)
print('k-grams for 1')
bigramCount(indexlist_1)
print('T for 2 = ',createLRZ(indexlist_2))
print('A for 2')
autoCor(indexlist_2)
print('k-grams for 2')
bigramCount(indexlist_2)
