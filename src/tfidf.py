from collections import Counter
from math import log



# docToWords
# 文章を単語に分割する
# in  : 'Time is money!'
# out : ['time', 'is', 'money']
def docToWords(doc):
    # 小文字に変換し、スペースと改行で分割
    words = doc.lower().split()

    #単語の両端から記号を取り除く
    symbol = ',.!?()/-_&%$\'\";|@$%^&*[]`~#'
    words = [word.strip(symbol) for word in words]

    return words


# df
# 単語を含むリストの数を辞書型で返す
# in  : [['a', 'b', 'a'], ['a', 'b']]
# out : {'a' : 2, 'b' : 2}
def df(docs):
    l = []
    for words in docs: l.extend(set(words)) #文章内で重複する単語をなくす

    return Counter(l)


# tfidf
# TFIDFで文章のリストを文章の特徴ベクトルのリストに変換する
def tfidf(docs):
    docs = [docToWords(doc) for doc in docs]

    dfDict = df(docs) #dfは全文章で共通
    features = []

    for words in docs:

        tfDict = Counter(words)  #tfは文章内で共通
        feature = []

        for word in dfDict.keys():
            # tfidfの計算式（logの基数はe）
            tfidf = tfDict[word] * log(len(docs) / dfDict[word])

            feature.append(tfidf)
        features.append(feature)

    return list(dfDict.keys()), features



# main
if __name__ == '__main__':
    docs = ['I have a pen'   ,
            'I have an apple',
            'Apple pen'      ]

    wordList, features = tfidf(docs)
    print(wordList)
    for f in features: print(f)
