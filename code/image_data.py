#-*-coding:utf8-*-

from sklearn.model_selection import train_test_split
from keras.utils import np_utils
import random


class ImageData(object):

    def __init__():
        self.img_size = 128
        pass

    def reshape_data():

        # 获得指定的数据集
        x_train,y_train,x_test,y_test = train_test_split(imgs,labels,test_size=0.2,random_state=random.randint(0, 100))

        # 注意实现的后端差别，这是基于thano的
        x_train = x_train.reshape(x_train.shape[0], 1, self.img_size, self.img_size)/255.0
        x_test = x_train.reshape(x_test.shape[0], 1, self.img_size, self.img_size)/255.0

        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
