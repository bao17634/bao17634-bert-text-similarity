from similarity import BertSim
import tensorflow as tf

sim = BertSim()
sim.set_mode(tf.estimator.ModeKeys.PREDICT)
while True:
    sentence1 = input('sentence1: ')
    sentence2 = input('sentence2: ')
    predict = sim.predict(sentence1, sentence2)
    print(f'similarity：{predict[0][1]}')