#-*-coding:utf8-*-

import os
import cv2

def get_labels(path):
    labels = []
    for dirs in os.listdir(path):
        labels.append(dirs)
        # print (dirs)

def get_train_set(path):
    for dir_name in os.listdir(path):
        for image_name in os.listdir(os.path.join(path,dir_name))

if __name__ == '__main__':
    get_labels('/Users/songheqi/work/FaceRecoginition/code')
