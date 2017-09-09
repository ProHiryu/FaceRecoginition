# -*-coding:utf8-*-

import os
import cv2
import numpy as np
import time


def get_train_set(path):
    img_list = []
    label_list = []
    counter = 0
    img_size = 128

    for child_dir in os.listdir(path):
        child_path = os.path.join(path, child_dir)
        if '.' in child_path:
            continue  # except '.DS_Store'

        for dir_image in os.listdir(child_path):
            img = cv2.imread(os.path.join(child_path, dir_image))
            resized_img = cv2.resize(img, (img_size, img_size))
            recolored_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
            img_list.append(recolored_img)
            label_list.append(counter)

        counter += 1

    img_list = np.array(img_list)

    return img_list, label_list, counter


def read_name_list(path):
    name_list = []

    for child_dir in os.listdir(path):
        name_list.append(child_dir)

    return name_list


def read_data(path):
    try:
        s = os.listdir(path)
        resultArray = []
        fileName = os.path.basename(path)  # "/foo/bar/" --> "bar"
        resultArray.append(fileName)

        for i in s:
            document = os.path.join(path, i)
            img = cv2.imread(document)
            resultArray.append(img)

    except IOError:
        print ("Error")

    else:
        print("Read success")
        return resultArray


def get_face(image_path, face_path):
    for child_path in os.listdir(image_path):
        if '.' in child_path:
            continue  # except '.DS_Store'

        try:
            resultArray = read_data(os.path.join(image_path,child_path))

            count = 1
            face_cascade = cv2.CascadeClassifier(
                '/usr/local/opt/opencv3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
            for i in resultArray:
                if type(i) != str:
                    try:
                        gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
                    except:
                        continue
                    faces = face_cascade.detectMultiScale(gray,1.3,5)
                    for (x, y, w, h) in faces:
                        listStr = [str(int(time.time())), str(count)]  #以时间戳和读取的排序作为文件名称
                        fileName = ''.join(listStr)

                        f = cv2.resize(gray[y:(y + h), x:(x + w)], (200, 200))
                        path = face_path+os.sep + child_path + os.sep
                        if not os.path.exists(path):
                            os.mkdir(path)
                        cv2.imwrite((path + fileName + '.jpg'), f)
                        count += 1

        except IOError:
            print ("Error")

        else:
            print ('Already read '+str(count-1)+' Faces to Destination '+face_path)

if __name__ == "__main__":
    get_face('/Users/songheqi/image/',r'/Users/songheqi/train_set')
