import os

import cv2

video_path = "../videos/paddy.mp4"
save_path = "save_images/"

'''
定义保存图片函数
image: 要保存的图片名字
addr: 图片地址与相片名字的前部分
num: 图片名字的后缀
'''


def save_image(image, addr, num):
    address = addr + str(num) + '.png'
    cv2.imwrite(address, image)


# 读取视频文件 视频文件路径
videoCapture = cv2.VideoCapture(video_path)

# 读帧
success, frame = videoCapture.read()
i = 0
j = 0

# 设置每帧的时间间隔
frame_interval_ms = 1000

while success:
    i += 1
    save_image(frame, save_path, j)  # 保存当前帧
    print('save image:', i)
    j += 1

    # 等待指定的时间间隔
    key = cv2.waitKey(frame_interval_ms)  # 等待指定的毫秒数
    if key == 27:  # 按 'Esc' 键退出
        break

    success, frame = videoCapture.read()

# 释放视频捕获对象
videoCapture.release()
cv2.destroyAllWindows()
