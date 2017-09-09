#-*-coding:utf8-*-

import cv2
from model import load_model, predict
from get_train_set import read_name_list

img = cv2.imread()

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
