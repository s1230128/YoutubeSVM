from doraemon import *

docsA = readFiles('data/wiki/game/*' , 20)
docsB = readFiles('data/wiki/movie/*', 20)

docsA = [d.replace('\n', ' ') + '\n' for d in docsA]
docsB = [d.replace('\n', ' ') + '\n' for d in docsB]

docs = docsA + docsB

with open('data.txt', 'w+') as f:
    f.writelines(docsA + docsB)
