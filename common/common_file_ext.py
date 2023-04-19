# -*- coding:utf-8 -*-
# __author__='ligang'

import enum

@enum.unique
class FileType(enum.Enum):
    NONE        = 0     # 无后缀
    VIDEO       = 1     # 视频
    IMAGE       = 2     # 静态图
    GIF         = 3     # 动态图
    AUDIO       = 4     # 音频文件
    ZIP         = 5     # 压缩文件
    DOC         = 6     # 包含内容文本文件
    DOCFILE     = 7     # 系统和应用的文本文件

    EXE         = 101   # 可执行文件
    HIDDEN      = 102  # 隐藏文件
    APP         = 103  # apk或app安装文件

    LINK        = 201     # URL地址
    HTML        = 202     # 网页

    FID         = 301     # 文件标识符描述符
    MEP         = 302    # 爱剪辑中间文件
    DOWNLOAD    = 303   # 下载使用文件
    LOG         = 304    # 日志文件
    CONFIG      = 305  # 配置文件

    BAK         = 401    # 备份文件

    UNKNOWN     = 999    # 未知

COMMON_FILE_EXTENSION_TYPE = {
        'zip': FileType.ZIP,
        'rar': FileType.ZIP,
        '7z': FileType.ZIP,

        'gif': FileType.GIF,

        'url': FileType.LINK,

        'chm': FileType.DOC,
        'txt': FileType.DOC,
        'xls': FileType.DOC,
        "xlsx": FileType.DOC,
        'pdf': FileType.DOC,
        'docx': FileType.DOC,
        'doc': FileType.DOC,
        'ppt': FileType.DOC,
        'pptx': FileType.DOC,
        'csv': FileType.DOC,

        'ass': FileType.DOCFILE,  # 字幕外挂文件
        'srt': FileType.DOCFILE,  # 字幕文件
        'sfv': FileType.DOCFILE,  # 简单文件验证
        'nfo': FileType.DOCFILE,
        'md5': FileType.DOCFILE,  # md5文件

        'ini': FileType.CONFIG,
        'config': FileType.CONFIG, # 通用配置文件
        'smpl': FileType.CONFIG,  # 暴风索引文件，播放列表
        'cfg': FileType.CONFIG,

        'xltd': FileType.DOWNLOAD,     # 没下完的迅雷文件
        'torrent': FileType.DOWNLOAD,  # 迅雷种子
        'downloading': FileType.DOWNLOAD,  # 百度云盘正在下载的文件
        'crdownload': FileType.DOWNLOAD,  # chrome浏览器下载缓存文件
        'td': FileType.DOWNLOAD,

        'htm': FileType.HTML,
        'mht': FileType.HTML,
        'html': FileType.HTML,

        'apk': FileType.APP,

        'mkv': FileType.VIDEO,
        'rmvb': FileType.VIDEO,
        'asf': FileType.VIDEO,
        'ts': FileType.VIDEO,
        'flv': FileType.VIDEO,
        'rm': FileType.VIDEO,
        'avi': FileType.VIDEO,
        'wmv': FileType.VIDEO,
        'mpg': FileType.VIDEO,
        'mov': FileType.VIDEO,
        'mp4': FileType.VIDEO,
        'm2ts': FileType.VIDEO,
        'm4a': FileType.VIDEO,
        'm4v': FileType.VIDEO,
        'mpeg': FileType.VIDEO,
        'vob': FileType.VIDEO,
        'divx': FileType.VIDEO,
        'mts': FileType.VIDEO,
        'amc': FileType.VIDEO,
        'asx': FileType.VIDEO,  # 微软流媒体格式的索引文件,
        'dat': FileType.VIDEO,  # DAT文件不是一种标准的文件类型,它是数据文件的一种,最常见的是VCD光盘、数字录音带中的数据存储文件
        'hlv': FileType.VIDEO,  # 在线视频文件格式，网页视频文件
        '3gp': FileType.VIDEO,
        'mod': FileType.VIDEO,
        'qt': FileType.VIDEO,
        'f4v': FileType.VIDEO,
        'swf': FileType.VIDEO,
        'xv': FileType.VIDEO,  # 用迅雷看看看视频或电影时的缓存文件
        'skm': FileType.VIDEO,
        '3g2': FileType.VIDEO,
        'h265-mp4': FileType.VIDEO,

        'jpeg': FileType.IMAGE,
        'jpg': FileType.IMAGE,
        'png': FileType.IMAGE,
        'bmp': FileType.IMAGE,
        'jfif': FileType.IMAGE,

        'mp3': FileType.AUDIO,
        'ac3': FileType.AUDIO,

        'fid': FileType.FID,

        'mep': FileType.MEP,    # 爱剪辑中间文件

        'ds_store': FileType.HIDDEN,  # 自定义属性的隐藏文件

        'log': FileType.LOG,
        'log1': FileType.LOG,  # 日志文件
        'log2': FileType.LOG,  # 日志文件

        'bak': FileType.BAK,   # 备份文件

        'mui': FileType.EXE,   # 多语言用户界面(MUI),表示 MUI 格式和文件类型
        'lnk': FileType.LINK,  # 快捷方式文件

        'exe': FileType.EXE,
        'db':  FileType.EXE,   # 数据库文件格式
        'ttf': FileType.EXE,   # 字体文件格式的文件
        'dll': FileType.EXE,
    }



