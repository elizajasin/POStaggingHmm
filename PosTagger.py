__author__ = 'Eliza & Angky'

import numpy as np

def findSentence(trainList):
    listOfSentence1 = []
    listOfSentence2 = []
    sentenceWord = []
    sentenceTag = []
    for i in range(len(trainList)):
        try:
            sentenceWord.append(trainList[i][0])
            sentenceTag.append(trainList[i][1])
        except:
            pass
            listOfSentence1.append(sentenceWord)
            sentenceWord = []
            listOfSentence2.append(sentenceTag)
            sentenceTag = []
    listOfSentence = np.array([listOfSentence1,listOfSentence2])
    return listOfSentence

def viterbi (listOfSentence,tProb,eProb,listTag):
    # per kalimat
    wordTagList = []
    for i in range(len(listOfSentence)):
        # per kata
        listProb = []
        nMax = 0
        wordTag = []
        for j in range(len(listOfSentence[i])):
            arrayProb = []
            a = []
            b = []
            if j == 0:
                for k in listTag:
                    prob = tProb[listOfSentence[1][i][0]]['.']*eProb[k][listOfSentence[0][i][0]]
                    a.append(k)
                    b.append(prob)
                    # print(listOfSentence[0][0][0]+' pada '+k+' dan . ke '+listOfSentence[1][0][0]+' '+str.format('{0:.15f}',prob))
                # print(arrayProb[1])
            else:
                for k in listTag:
                    prob = nMax*tProb[listOfSentence[1][i][0]]['.']*eProb[k][listOfSentence[0][i][0]]
                    a.append(k)
                    b.append(prob)
            arrayProb = np.array([a,b])
            nMax = nMax + np.amax(b)
            wordTag.append(arrayProb[0][b.index(np.amax(b))])
        wordTagList.append(wordTag)
    print(wordTagList)