import tensorflow as tf
import numpy as np
import pickle
from doraemon import *
from sklearn.metrics import accuracy_score



# データの準備
## tfidfデータの読み取り
with open('wiki/wiki.pickle', 'rb') as f:
    features, labels = pickle.load(f)

labels = oneHotVecs(labels)

## シャッフル
labeled_features = list(zip(features, labels))
np.random.shuffle(labeled_features)
features = [f for f, _ in labeled_features]
labels   = [l for _, l in labeled_features]

## データをトレイニング用とテスト用に分割
train_features, test_features = splitByRatio(features, [0.8, 0.2])
train_labels  , test_labels   = splitByRatio(labels  , [0.8, 0.2])



# Model
## Parameters
n_input    = len(features[0])
n_hidden_1 = 500
n_hidden_2 = 500
n_classes  = 2

## Data & Label
x = tf.placeholder("float", shape=[None, n_input  ])
y = tf.placeholder("float", shape=[None, n_classes])

## Model
class DocClusteringMPN:
    def __init__(self):
        self.weights = {'h1' : tf.Variable(tf.random_normal([n_input   , n_hidden_1])),
                        'h2' : tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
                        'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes ]))}

        self.biases  = {'b1' : tf.Variable(tf.random_normal([n_hidden_1])),
                        'b2' : tf.Variable(tf.random_normal([n_hidden_2])),
                        'out': tf.Variable(tf.random_normal([n_classes ]))}

    def __call__(self, x):
        # L1 = W1 * X  + b1
        # L2 = W2 * L1 + b2
        # Y  = Wout * L2 + bout
        self.layer_1 = tf.sigmoid(tf.add(tf.matmul(x           , self.weights['h1']), self.biases['b1']))
        self.layer_2 = tf.sigmoid(tf.add(tf.matmul(self.layer_1, self.weights['h2']), self.biases['b2']))
        return tf.matmul(self.layer_2, self.weights['out']) + self.biases['out']



# Learning Method
## Parameters
learning_rate = 0.001

## set up model
model = DocClusteringMPN()
predict = model(x)

## define loss
losses = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=predict)
loss_mean = tf.reduce_mean(losses)

## define optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss_mean)

## define accuracy
correct_prediction = tf.equal(tf.argmax(predict, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))



# Training & Testing
## Parameters
n_epoch = 100
display_step = 10

##
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(n_epoch):
        sess.run(optimizer, feed_dict={x:train_features, y:train_labels})

        if epoch % display_step == 0:
            loss = sess.run(loss_mean, feed_dict={x:train_features, y:train_labels})
            accu = sess.run(accuracy , feed_dict={x:test_features, y:test_labels})
            print("Epoch : {:>3}  |  cost = {:.9f}  |  accuracy = {:f}".format(epoch, loss, accu))

    saver = tf.train.Saver()
    saver.save(sess, "model/docClusteringMPN.ckpt")
