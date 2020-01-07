import string
import math

alphabet = open("Alphabet2.txt",encoding='utf-8')
alphabetData = alphabet.read()
textGeneral = open("Texy5.txt", encoding='utf-8')
textGeneralData = textGeneral.read()
textDataWithoutSpaces = textGeneralData.replace(' ','')
textGeneral1 = open("Text4.txt", encoding='utf-8')
textGeneralData1 = textGeneral1.read()
textDataWithoutSpaces1 = textGeneralData1.replace(' ','')

text = 'приветмирприветмирприветмирприветмирприветмир'

keys = ['по','рог','дома','моего','кабардинец','холостойход','грехопадение','узниказкабана',
        'слепойпровидец','неистоваягарпия','огоньнапоражение','понтийпилатииешуа',
        'невыносимостьбытия','бросатьслованаветер','внеземнаяцивилизация']

def Encrypt(alpha, key, text):
    a = ''
    i = 0
    for item in text:
        world = (alpha.index(item) + alpha.index(key[i % len(key)])) % len(alpha)
        a += alpha[world]
        i += 1
    return a

def Decrypt(alpha, key, text):
    a = ''
    i = 0
    for item in text:
        world = (alpha.index(item) - alpha.index(key[i % len(key)]) + len(alpha)) % len(alpha)
        a += alpha[world]
        i += 1
    return a

def Index(alpha, text):
    indexS = 0
    count = 0
    for i in range(len(alpha)):
        for elem in text:
            if elem == alpha[i]:
                count += 1
        indexS += count * (count-1)
        count = 0
    print(indexS/(len(text)*(len(text)-1)))
    
def IndexEncr(alpha, text):
    count = 0
    indexS = 0
    indexE = 0
    for r in range(2,31):
        indexE = 0
        for j in range(r):
            indexS = 0
            for i in range(len(alpha)):
                counter = 0
                count = 0
                n = 0
                while 1:
                    if text[n] == alpha[i]:
                        count += 1
                    n += r
                    counter += 1
                    if n >= len(text):
                        break
                indexS += count * (count-1)
                n += 1
            indexE += indexS/((counter)*(counter - 1))
        print(indexE/r)
        
def monogramDictCreate(alpha):
    return {item: 0 for item in alpha}
    
def monogramCount(text, alpha, key):
    monogramDict = monogramDictCreate(alpha)
    print(monogramDict)
    for i in range(key):
        for j in range(len(alpha)):
            count = 0
            elem = alpha[j]
            n = i
            while 1:
                if text[n] == alpha[j]:
                    count += 1
                n+=key
                if n >= len(text):
                    break
            monogramDict[elem]=count
        print(monogramDict)

def indexforkeys():
    Index(alphabetData, textDataWithoutSpaces)
    for key in keys:
        print(key)
        a = Encrypt(alphabetData, key, textDataWithoutSpaces)
        Index(alphabetData, a)
        print('--------------')

def mainfunc():
    Index(alphabetData, textDataWithoutSpaces1)
    IndexEncr(alphabetData, textDataWithoutSpaces1)
    print('Enter key len')
    keyLen = int(input())
    monogramCount(textDataWithoutSpaces, alphabetData, keyLen)

def DecryptPlainText():
    key = input()
    print(Decrypt(alphabetData, key, textDataWithoutSpaces1))
