import ffmpeg_streaming

from ffmpeg_streaming import Formats, Bitrate, Representation, Size
from os import path
import os



def videoConverter(file):
    # cwd = os.getcwd()
    # cwd+='/videos/minion.mp4'
    # print(cwd)
    
    video = ffmpeg_streaming.input(file)
    hls = video.hls(Formats.hevc())
    
    # _480p  = Representation(Size(854, 480), Bitrate(1500,True, 320 * 1024))
    _720p  = Representation(Size(1280, 720), Bitrate(1280 * 720, True,320 * 1024))
    hls = video.hls(Formats.h264())
    hls.representations( _720p)
    hls.output('./videos/minion.m3u8')
    
    # dash = video.dash(Formats.h264())
    # dash.representations(_480p, _720p)
    # dash.output('./videos/minion.mpd')

