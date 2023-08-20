#----------------------------------------------------#
#   将单张图片预测、摄像头检测和FPS测试功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
#----------------------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image


#
from deeplab import DeeplabV3

def shibiepic2(pic):

    deeplab = DeeplabV3()
    image = Image.open(str(pic))
    r_image = deeplab.detect_image(image)
    return r_image


def shibiepic(pic):

    deeplab = DeeplabV3()
    image = Image.open(str(pic))
    r_image = deeplab.detect_image(image)
    r_image.show()

def shibievideo(kk):
    deeplab = DeeplabV3()
    video_path = kk
    video_save_path = "outvideo.mp4"
    video_fps = 25.0
    test_interval = 100
    capture = cv2.VideoCapture(video_path)
    #笔记本摄像头接1
    if kk == "1":
        capture = cv2.VideoCapture(1)
    if video_save_path != "":
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        out = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)

        ref, frame = capture.read()
    if not ref:
        raise ValueError("未能正确读取摄像头（视频），请注意是否正确安装摄像头（是否正确填写视频路径）。")

    fps = 0.0
    while (True):
        t1 = time.time()
        # 读取某一帧
        ref, frame = capture.read()
        if not ref:
            break
        # 格式转变，BGRtoRGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 转变成Image
        frame = Image.fromarray(np.uint8(frame))
        # 进行检测
        frame = np.array(deeplab.detect_image(frame))
        # RGBtoBGR满足opencv显示格式
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        fps = (fps + (1. / (time.time() - t1))) / 2
        x1 = "fps= %.2f" % (fps)
        #print(x1)

        frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("video", frame)
        c = cv2.waitKey(1) & 0xff
        if video_save_path != "":
            out.write(frame)

        if c == 27:
            capture.release()
            break
    print("Video Detection Done!")
#
    capture.release()
    if video_save_path != "":
        print("Save processed video to the path :" + video_save_path)
        out.release()
    cv2.destroyAllWindows()


def shibiedir(dd):
    import os
    from tqdm import tqdm

    deeplab = DeeplabV3()
    dir_origin_path = dd
    dir_save_path = "outtest/"
    img_names = os.listdir(dir_origin_path)
    for img_name in tqdm(img_names):
        if img_name.lower().endswith(
                ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            image_path = os.path.join(dir_origin_path, img_name)
            image = Image.open(image_path)
            r_image = deeplab.detect_image(image)
            if not os.path.exists(dir_save_path):
                os.makedirs(dir_save_path)
            r_image.save(os.path.join(dir_save_path, img_name))
    print("dir finshed")






