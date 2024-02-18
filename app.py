# from ffmpeg_streaming import Formats, Bitrate, Representation, Size
# import ffmpeg_streaming
# from flask import Flask, Response, render_template

# app = Flask(__name__)

# @app.route('/video')
# def stream_video():
#     video_path = './video/minion.mp4'
#     video = ffmpeg_streaming.input(video_path)
#     hls = video.hls(Formats.h264())
#     hls.auto_generate_representations()
#     return Response(hls.output('./hls.m3u8'), mimetype='application/x-mpegURL')

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)