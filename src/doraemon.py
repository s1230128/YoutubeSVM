'''
便利な関数いろいろ
'''

import glob



# readFiles
# 正規表現で指定したファイルをリストで返す
def readFiles(regularExpression, n=None):
    docs = []
    fPasses = glob.glob(regularExpression)

    if n == None:
        n = len(fPasses)

    for (fPass, _) in zip(fPasses, range(n)):
        f = open(fPass, 'r')
        docs.append(f.read())

    return docs



# docToWords
# 文章を単語のリストに
# in  : 'Time is money!'
# out : ['time', 'is', 'money']
def docToWords(doc):
    # スペースと改行で分割
    words = doc.split()
    # 単語の両端から記号を取り除き、小文字に
    symbol = ',.!?()/-_&%$\'\";|@$%^&*[]`~#'
    words = [word.strip(symbol).lower() for word in words]

    return words



# splitByRatio
# 比率でデータを分割する
# in : [1, 2, 3, 4], [1.0, 3.0]
# out: [[1], [2, 3, 4]]
def splitByRatio(datas, ratios):
    # ratiosの合計がデータ数と同じになるように変換
    ratios = [round(r*len(datas)/sum(ratios)) for r in ratios]

    splitted = []
    prev = 0
    for r in ratios:
        splitted.append(datas[prev:prev + r])
        prev = prev + r

    return splitted



# oneHotVec
def oneHotVecs(vecs):
    # 順序を保持したままsetに
    classes = sorted(set(vecs), key=vecs.index)

    oneHotVecs = []
    for vec in vecs:
        oneHotVec = []
        for cl in classes:
            if vec == cl:
                oneHotVec.append(1)
            else:
                oneHotVec.append(0)
        oneHotVecs.append(oneHotVec)

    return oneHotVecs



def extractJapanese(str):
    str_ja = ''
    for ch in str:
        if 'ぁ' <= ch <= 'ん' or \
           'ァ' <= ch <= 'ン' or \
           '亜' <= ch <= '腕' or \
           ch in '、。「」『」！？ー\n':
           str_ja += ch

    return str_ja



if __name__ == '__main__':
    str = 'あ亜わsdsjkdインテリア？・＜＞「」、。'
    print(str)
    print(extractJapanese(str))
