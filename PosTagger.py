__author__ = 'Eliza & Angky'


def findSentence(trainList):
    listSentence = []
    sentence = []
    for i in range(len(trainList)):
        try:
            sentence.append(trainList[i][0])
        except:
            pass
            listSentence.append(sentence)
            sentence = []
    return listSentence

# def viterbi (trainList,tProb,eProb,listTag):