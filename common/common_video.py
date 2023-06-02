# -*- coding:utf-8 -*-
# __author__='LiGang'

import cv2


def get_video_duration(video_path):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    # 获取视频帧率
    fps = video.get(cv2.CAP_PROP_FPS)
    if fps < 1e-6:
        return {
        "fps": 0,
        "frame_count": 0,
        "duration_ms": 0,
    }
    #print("fps:", fps)
    # 获取视频总帧数
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # 计算视频总时长（毫秒）
    duration_ms = int(frame_count * 1000 / fps)
    # 释放视频对象
    video.release()
    return {
        "fps": fps,
        "frame_count": frame_count,
        "duration_ms": duration_ms,
    }

