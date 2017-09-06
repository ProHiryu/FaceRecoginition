import os

for child_dir in os.listdir("/Users/songheqi/image/"):
    if '.' in child_dir:
        continue
    child_path = os.path.join("/Users/songheqi/image/",child_dir)
    for image in os.listdir(child_path):
        if image.split('.')[0] == '':
            continue
        number = int(image.split(".")[0])
        final_path = os.path.join(child_path,image)
        if (number > 60):
            try:
                os.remove(final_path)
            except:
                print("error")
