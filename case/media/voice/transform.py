from os import path
from pydub import AudioSegment

# files
src = "/Users/zifang/Music/网易云音乐/a.mp3"
dst = "/Users/zifang/Music/网易云音乐/a.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
