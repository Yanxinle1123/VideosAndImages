import cv2


def save_image(image, addr, name, suffix='.png'):
    address = addr + str(name) + suffix
    cv2.imwrite(address, image)


class VideosToImages:
    def __init__(self, video_path, save_path, suffix='.png'):
        self._video_path = video_path
        self._save_path = save_path
        self._suffix = suffix

    def convert(self, frame_interval_ms=1000):
        video_capture = cv2.VideoCapture(self._video_path)

        # 获取视频的帧率
        fps = int(video_capture.get(cv2.CAP_PROP_FPS))

        # 计算每隔 frame_interval_ms 毫秒应该跳过的帧数
        skip_frames = fps * frame_interval_ms // 1000

        # 截图
        i = 0
        j = 1
        while video_capture.isOpened():
            success, frame = video_capture.read()
            if not success:
                break

            if i % skip_frames == 0:
                save_image(frame, self._save_path, j, self._suffix)
                j += 1
            i += 1

        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    vti = VideosToImages('../videos/paddy.mp4', 'save_images/paddy_images/')
    vti.convert(frame_interval_ms=1000)
