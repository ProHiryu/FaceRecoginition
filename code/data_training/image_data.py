#-*-coding:utf8-*-

from sklearn.model_selection import train_test_split
from keras.utils import np_utils
import random


class ImageData(object):

    def __init__():
        self.img_size = 128
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.num_classes = None
        pass

    def reshape_data(self,counter,x_train,y_train,x_test,y_test):

        # 获得指定的数据集
        x_train,y_train,x_test,y_test = train_test_split(imgs,labels,test_size=0.2,random_state=random.randint(0, 100))

        # 注意实现的后端差别，这是基于thano的
        x_train = x_train.reshape(x_train.shape[0], 1, self.img_size, self.img_size)/255.0
        x_test = x_train.reshape(x_test.shape[0], 1, self.img_size, self.img_size)/255.0

        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')

        #将labels转成 binary class matrices
        y_train = np_utils.to_categorical(y_train, num_classes=counter)
        y_test = np_utils.to_categorical(y_test, num_classes=counter)

        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test
        self.num_classes = counter

    def check(self):
       print('num of dim:', self.x_test.ndim)
       print('shape:', self.x_test.shape)
       print('size:', self.x_test.size)

       print('num of dim:', self.x_train.ndim)
       print('shape:', self.x_train.shape)
       print('size:', self.x_train.size)
