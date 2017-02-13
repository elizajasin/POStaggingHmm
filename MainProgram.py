from __future__ import division
__author__ = 'Eliza & Angky'

import os
import LearnParam as Lp
import PosTagger as Pt

os.system('cls')
wordList = Lp.readData('pos.train.txt')
listTag = Lp.makeTagList(wordList)
tProb = Lp.transition(wordList,listTag)
eProb = Lp.emission(wordList,tProb,listTag)
listS = Pt.findSentence(wordList)
Pt.viterbi(listS,tProb,eProb,listTag)
# print(str.format('{0:.15f}', eProb['NN'][listS[0][0][0]]))