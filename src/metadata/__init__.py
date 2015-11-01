from metadata._base import BaseFormat, NotWritable, NotReadable
import os

from metadata import mp3

formats = {
    'mp3': mp3.MP3Format,
}


def get_format(loc):
    try:
        loc = loc.decode('utf-8')
    except UnicodeDecodeError:
        pass

    ext = os.path.splitext(loc)[1][1:]  # get file extension
    ext = ext.lower()
    try:
        formatclass = formats[ext]
    except KeyError:
        return None  # not supported

    if formatclass is None:
        formatclass = BaseFormat

    try:
        return formatclass(loc)
    except NotReadable:
        return None
