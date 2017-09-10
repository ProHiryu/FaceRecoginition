#-*-coding:utf8-*-

import cv2
from model import load_model, predict
from get_train_set import read_name_list
import sys


def test_file():
    count = 1
    face_cascade = cv2.CascadeClassifier(
        '/usr/local/opt/opencv3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

    argvs = sys.argv
    for argv in argvs[1:]:
        img = cv2.imread(argv)

        if type(img) != str:
            try:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                print('convert succeed')
            except:
                print('can not convert to gray image')
                continue
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                f = cv2.resize(gray[y:(y + h), x:(x + w)], (128, 128))
                model = load_model('/Users/songheqi/model/model.h5')
                num, acc = predict(model, f, 128)
                name_list = read_name_list('/Users/songheqi/train_set/')
                print('The {} picture is '.format(count) +
                      name_list[num] + ' acc : ', acc)
                count += 1


if __name__ == "__main__":
    test_file()
