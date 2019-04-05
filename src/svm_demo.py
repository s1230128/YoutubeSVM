import glob
from tfidf import docFreqDict, features
from docToWords import docToWords
from cosSimularity import cosSimularity
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix


# readTogather
# in  : 正規表現によるファイルの指定
# out : 文章のリスト
def readTogather(regularExpression):
    docs = []
    fPasses = glob.glob(regularExpression)

    for fPass in fPasses:
        f = open(fPass, 'r')
        docs.append(f.read())

    return docs


# データの取り込み
letters = readTogather('./masc_500k_texts/written/letters/*.txt')
emails  = readTogather('./masc_500k_texts/written/email/*.txt'  )

letters = [docToWords(doc) for doc in letters]
emails  = [docToWords(doc) for doc in emails ]

docs = letters + emails


# トレイニング＆テストデータ生成
trainRate = 0.8

n_train_letters = int(len(letters) * trainRate)
n_train_emails  = int(len(emails ) * trainRate)

train_docs = letters[:n_train_letters ] + emails[:n_train_emails ]
test_docs  = letters[ n_train_letters:] + emails[ n_train_emails:]

train_labels = ['letter'] * n_train_letters \
             + ['email' ] * n_train_emails
test_labels  = ['letter'] * (len(letters) - n_train_letters) \
             + ['email' ] * (len(emails ) - n_train_emails )


# tfidfをつかって特徴ベクトルに
dfDict = docFreqDict(docs)
train_features = features(train_docs, len(docs), dfDict)
test_features  = features(test_docs , len(docs), dfDict)


# svmのトレーニング＆テスト
clf = svm.SVC()
clf.fit(train_features, train_labels)

predicts = clf.predict(test_features)

print(confusion_matrix(test_labels, predicts))
print(accuracy_score(test_labels, predicts))
