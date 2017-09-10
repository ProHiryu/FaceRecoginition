# FaceRecoginition
利用 opencv+keras+python 实现人脸识别系统

### code structure

```
data retreiving -+
                 |
                 +cut_files.py        <-- 删除冗余的训练图片素材
                 |
                 +get_images.py       <-- 获取不同人名对应的图片，并将其保存
                 |
                 +get_names.py        <-- 获取当前女优排名的名字 list
                 |
                 +googl_api.py        <-- 通过 Google API 获取图片
                 |
                 +names.pickle        <-- 人名列表
                 |
                 +<other files>       <-- 额外的文件

data training   -+
                 |
                 +get_train_set.py    <-- 获取训练图片数据集
                 |
                 +image_data.py       <-- 定义训练数据集类 ImageData
                 |
                 +model.py            <-- 定义模型并训练保存
                 |
                 +test_camera.py      <-- 打开摄像头对模型进行测试
                 |
                 +test_file.py        <-- 打开文件对模型进行测试
                 |
                 +<other files>       <-- 额外的文件
```
### 说明

本项目只是简单的对keras + opencv进行实战，并没有真实用途，有疑问请联系作者
