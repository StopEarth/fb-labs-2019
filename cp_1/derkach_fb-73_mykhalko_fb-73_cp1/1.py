import string
import re
import math

def monogramDictCreate(alpha):
    return {item: 0 for item in alpha}
    
def monogramCount(text, alpha):
    monogramDict = monogramDictCreate(alpha)
    for elem in text:
        monogramDict[elem]+=1
    for elem in monogramDict:
        monogramDict[elem]/=len(text)
    return monogramDict

def bigramDictCreate(alpha):
    return {item1+item2: 0 for item1 in alpha for item2 in alpha}

def bigramCount(text, alpha):
    bigramDict = bigramDictCreate(alpha)
    for position in range(len(text)-1):
        bigramDict[text[position]+text[position+1]] += 1
    for elem in bigramDict:
        bigramDict[elem]/= len(text)-1
    return bigramDict

def bigramCountWithSpace(text, alpha):
    bigramDict = bigramDictCreate(alpha)
    for position in range(0,len(text)-1,2):
        bigramDict[text[position]+text[position+1]] += 1
    for elem in bigramDict:
        bigramDict[elem]/= len(text)//2
    return bigramDict

def entropyMono(Dict):
    entropyData = 0
    for elem in Dict:
        if Dict[elem] != 0:
            entropyData -= Dict[elem]*math.log(Dict[elem],2)
    return entropyData

def entropyBi(Dict):
    entropyData = 0
    for elem in Dict:
        if Dict[elem] != 0:
            entropyData -= Dict[elem]*math.log(Dict[elem],4)
    return entropyData

def residual(entropy, alpha):
    return 1 - (entropy / (math.log(len(alpha), 2)))


alphabet = open("Alphabet.txt",encoding='utf-8')
alphabetData = alphabet.read()
textGeneral = open("Text6.txt", encoding='utf-8')
textGeneralData = textGeneral.read()
textGeneralDataFiltred = re.sub(r'[^а-яА-Я ]+', '', textGeneralData)
textGeneralDataFiltred = textGeneralDataFiltred.lower()
print(monogramCount(textGeneralDataFiltred, alphabetData + ' '))
textGeneralDataFiltred = re.sub(r'\s+', ' ', textGeneralDataFiltred)
textGeneralDataFiltred = re.sub('ъ', 'ь', textGeneralDataFiltred)
textGeneralDataFiltred = re.sub('ё', 'е', textGeneralDataFiltred)
with open("Text2.txt", "w") as textFiltred:
    textFiltred.write(textGeneralDataFiltred)
textDataWithoutSpaces = textGeneralDataFiltred.replace(' ','')
with open("Text3.txt", "w") as textWithoutSpaces:
    textWithoutSpaces.write(textDataWithoutSpaces)
print('Энтропия: монограммы без пробелов')
print(entropyMono(monogramCount(textDataWithoutSpaces, alphabetData)))
print('Энтропия: биграммы без пробелов')
print(entropyBi(bigramCount(textDataWithoutSpaces, alphabetData)))
print('Энтропия: биграммы без пробелов с шагом')
print(entropyBi(bigramCountWithSpace(textDataWithoutSpaces, alphabetData)))
print('Энтропия: монограммы c пробелами')
print(entropyMono(monogramCount(textGeneralDataFiltred, alphabetData + ' ')))
print('Энтропия: биграммы с пробелами')
print(entropyBi(bigramCount(textGeneralDataFiltred, alphabetData + ' ')))
print('Энтропия: биграммы с пробелами с шагом')
print(entropyBi(bigramCountWithSpace(textGeneralDataFiltred, alphabetData + ' ')))
print('Остаточность монограмм без пробелов')
print(residual(entropyMono(monogramCount(textDataWithoutSpaces, alphabetData)), alphabetData))
print('Остаточность биграмм без пробелов')
print(residual(entropyBi(bigramCount(textDataWithoutSpaces, alphabetData)), alphabetData))
print('Остаточность биграмм без пробелов с шагом')
print(residual(entropyBi(bigramCountWithSpace(textDataWithoutSpaces, alphabetData)), alphabetData))
print('Остаточность монограмм с пробелами')
print(residual(entropyMono(monogramCount(textGeneralDataFiltred, alphabetData + ' ')), alphabetData + ' '))
print('Остаточность биграмм с пробелами')
print(residual(entropyBi(bigramCount(textGeneralDataFiltred, alphabetData + ' ')), alphabetData + ' '))
print('Остаточность биграмм с пробелами с шагом')
print(residual(entropyBi(bigramCountWithSpace(textGeneralDataFiltred, alphabetData + ' ')), alphabetData + ' '))
print(monogramCount(textDataWithoutSpaces, alphabetData))
print(bigramCount(textDataWithoutSpaces, alphabetData))
print(bigramCountWithSpace(textDataWithoutSpaces, alphabetData))
print(monogramCount(textGeneralDataFiltred, alphabetData + ' '))
print(bigramCount(textGeneralDataFiltred, alphabetData + ' '))
print(bigramCountWithSpace(textGeneralDataFiltred, alphabetData + ' '))


