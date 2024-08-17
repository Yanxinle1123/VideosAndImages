import cv2
from tqdm import tqdm

video_path = "../videos/paddy.mp4"
save_path = "save_images/"


def save_image(image, addr, name, suffix='.png'):
    address = addr + str(name) + suffix
    cv2.imwrite(address, image)


videoCapture = cv2.VideoCapture(video_path)

# 获取视频的帧率
fps = int(videoCapture.get(cv2.CAP_PROP_FPS))

# 设置帧间隔
frame_interval_ms = 1000

# 计算每隔 frame_interval_ms 毫秒应该跳过的帧数
skip_frames = fps * frame_interval_ms // 1000

i = 0
j = 1

# 计算视频的总帧数
total_frames = int(videoCapture.get(cv2.CAP_PROP_FRAME_COUNT))

# 使用 tqdm 创建进度条
with tqdm(total=total_frames, ascii=True, ncols=100,
          bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{remaining}]') as progress_bar:
    while videoCapture.isOpened():
        success, frame = videoCapture.read()
        if not success:
            break

        if i % skip_frames == 0:
            save_image(frame, save_path, j)
            j += 1

        progress_bar.update(1)
        i += 1

videoCapture.release()
cv2.destroyAllWindows()
