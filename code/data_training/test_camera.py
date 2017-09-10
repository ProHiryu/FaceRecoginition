#-*-coding:utf8-*-

import cv2
from model import load_model, predict
from get_train_set import read_name_list

def test_camera():
    face_patterns = cv2.CascadeClassifier(
        '/usr/local/opt/opencv3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

    cameraCapture = cv2.VideoCapture(0)
    success, frame = cameraCapture.read()

    while True:
        success, frame = cameraCapture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 图像灰化
        faces = face_patterns.detectMultiScale(gray, 1.3, 5)  # 识别人脸
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(
                frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 在人脸区域画一个正方形出来
            f = cv2.resize(gray[y:(y + h), x:(x + w)], (128, 128))
            model = load_model('/Users/songheqi/model/model.h5')
            num,acc = predict(model,f,128)
            name_list = read_name_list('/Users/songheqi/train_set/')
            print('You are ' + name_list[num] + ' acc : ',acc)
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1)&0xFF == ord('q'):  #按‘q’键退出
            break

    cameraCapture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_camera()
