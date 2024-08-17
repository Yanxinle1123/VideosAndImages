import cv2


def save_image(image, addr, name, suffix='.png'):
    address = addr + str(name) + suffix
    cv2.imwrite(address, image)


class VideosToImages:
    def __init__(self, video_source, save_path, type_='video', suffix='.png'):
        self._video_source = video_source
        self._save_path = save_path
        self._type = type_
        self._suffix = suffix

    def convert(self, frame_interval_ms=1000):
        video_capture = None
        if self._type == 'streaming':
            video_capture = cv2.VideoCapture(int(self._video_source))
        elif self._type == 'video':
            video_capture = cv2.VideoCapture(self._video_source)

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
    video_path = '../videos/paddy.mp4'
    save_path = 'save_images/paddy_images/'

    vti = VideosToImages(video_source=video_path, save_path=save_path, type_='video', suffix='.png')
    vti.convert(frame_interval_ms=1000)
