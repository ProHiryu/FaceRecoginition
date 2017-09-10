#-*-coding:utf8-*-

import numpy as np
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import SGD
from image_data import ImageData


# 参考官网中VGG网络实现部分
def build_model():
    model = Sequential()
    # input shape = [num,32,128,128],num of tensors with shape 128x128
    model.add(
        Convolution2D(
            filters=32,
            kernel_size=(5, 5),
            padding='same',
            dim_ordering='th',
            input_shape=dataset.x_train.shape[1:]
        )
    )

    model.add(Activation('relu'))
    model.add(
        MaxPooling2D(
            pool_size=(2, 2),
            strides=(2, 2),
            padding='same'
        )
    )
    model.add(Dropout(0.25))

    model.add(Convolution2D(filters=64, kernel_size=(5, 5), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2),
                           strides=(2, 2), padding='same'))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(dataset.num_classes))
    model.add(Activation('softmax'))
    model.summary()

    return model


def train_model(model, x_train, y_train):
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

    model.compile(
        optimizer=sgd,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(x_train, y_train, batch_size=32, epochs=35)
    return model


def evaluate_model(model, x_test, y_test):
    print('\nTesting--------------------------')
    loss, accuracy = model.evaluate(x_test, y_test, batch_size=32)

    print('test loss: ', loss)
    print('test accuracy: ', accuracy)


def save(model, path):
    try:
        model.save(path)
        print('Model saved')
    except:
        print('save failed')


def load(path):
    try:
        model = load_model(path)
        print('Model loaded')
    except:
        print('load failed')


def predict(model, img, img_size):
    img = img.reshape((1, 1, img_size, img_size))
    img = img.astype('float32')
    img = img / 255.0

    result = model.predict_proba(img)
    max_index = np.argmax(result)

    return max_index, result[0][max_index]


if __name__ == '__main__':
    # set dataset
    dataset = ImageData('/Users/songheqi/train_set/')
    model = build_model()
    model = train_model(model, dataset.x_train, dataset.y_train)
    evaluate_model(model, dataset.x_test, dataset.y_test)
    save(model, '/Users/songheqi/model/model2.h5')
