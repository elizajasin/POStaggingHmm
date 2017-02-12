__author__ = 'Eliza & Angky'

def readData(filename):
    f = open(filename, 'r')
    t = f.readlines()
    b = []
    for i in t:
        a = i.split()
        b.append(a)
    return b

def transition(b,listTag):
    c = {}
    for i,item in enumerate(b) :
        try:
            listTag.add(b[i][1])
        except :
            pass
    for item in listTag:
        c[item] = {}
        for item2 in listTag:
            c[item][item2] = 0
    for i, item in enumerate(b):
        try:
            c[item[1]][b[i + 1][1]] += 1
        except:
            pass
    for item in listTag:
        jum = 0
        for item2 in listTag:
            jum += c[item][item2]
        for item2 in listTag:
            if jum != 0:
                c[item][item2] = c[item][item2] / jum
            else:
                c[item][item2] = 0
    # print("Transition Probabilities")
    # for item in listTag:
    #     for item2 in listTag:
    #         if c[item][item2] != 0:
    #             print(item2 + " setelah " + item + ": " + str.format('{0:.15f}', c[item][item2]))
    return c

def emission(b,c,listTag):
    bagOfWords = set()
    for i,item in enumerate(b) :
        try:
            bagOfWords.add(b[i][0])
        except :
            pass
    e = {}
    for item in listTag :
        e[item] = {}
        for item2 in bagOfWords :
            e[item][item2] = 0
    for i, item in enumerate(b):
        try:
            e[item[1]][b[i][0]] += 1
        except:
            pass
    for item in listTag:
        jum = 0
        for item2 in bagOfWords:
            jum += e[item][item2]
        for item2 in bagOfWords:
            if jum != 0:
                e[item][item2] = e[item][item2] / jum
            else:
                c[item][item2] = 0
    # print("Emission Probabilities")
    # for item in listTag:
    #     for item2 in bagOfWords:
    #         if e[item][item2] != 0:
    #             print(item + " pada kata " + item2 + " : " + str.format('{0:.15f}', e[item][item2]))
    return e