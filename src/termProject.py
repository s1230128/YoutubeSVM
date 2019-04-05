import pickle
import numpy as np
from doraemon import splitByRatio
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix


# tfidfデータの読み取り
with open('wiki/wiki.pickle', 'rb') as f:
    features, labels = pickle.load(f)

# シャッフル
labeled_features = list(zip(features, labels))
np.random.shuffle(labeled_features)
features = [f for f, _ in labeled_features]
labels   = [l for _, l in labeled_features]

# データをトレイニング用とテスト用に分割
train_features, test_features = splitByRatio(features, [0.7, 0.3])
train_labels  , test_labels   = splitByRatio(labels  , [0.7, 0.3])


# svmのトレーニング＆テスト
clf = svm.SVC()
clf.fit(train_features, train_labels)

predicts = clf.predict(test_features)

print(confusion_matrix(test_labels, predicts))
print(accuracy_score(test_labels, predicts))
