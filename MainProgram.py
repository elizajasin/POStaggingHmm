from __future__ import division
__author__ = 'Eliza & Angky'

import os
import LearnParam as Lp
import PosTagger as Pt

os.system('cls')
wordList = Lp.readData('pos.train.txt')
listTag = set()
tProb = Lp.transition(wordList,listTag)
eProb = Lp.emission(wordList,tProb,listTag)
Pt.viterbi(wordList,tProb,eProb,listTag)