__author__ = 'Eliza & Angky'

def readData(filename):
    with open(filename,'r') as ins:
        wordlist = []
        taglist = []
        for line in ins:
            if line!='\n':
                word = line.split(' ')
                wordlist.append(str(word[0]))
                taglist.append(str(word[1].replace('\n','')))
    return taglist,wordlist