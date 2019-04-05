'''
tfidfは処理に時間がかかるので、
作った特徴ベクトルとそのラベルをpickle形式で保存し使い易くする
'''

from doraemon import readFiles, docToWords
from tfidf import features
import numpy as np
import pickle

# テキストの読み取り
docsA = readFiles('./wiki/game/*.txt')
docsB = readFiles('./wiki/movie/*.txt')

# tfidfで特徴ベクトルに変換
features = features(docsA + docsB)

# ラベルを作成
labels = [0] * len(docsA) + [1] * len(docsB)

# pickle形式でファイルに書き込み
with open('wiki/wiki.pickle', 'wb') as f:
    pickle.dump((features, labels), f)
