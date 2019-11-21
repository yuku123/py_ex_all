import wave
import math
import struct
f=wave.open("/Users/zifang/Music/网易云音乐/b.wav","w")
f.setframerate(8000)#声音频率
f.setnchannels(1)#声道数
f.setsampwidth(2)#声音宽度
t=0#时间
v=0.5#音量
dt=1/8000.0#录入声音的时间

while t<5:
    s=math.sin(t*math.pi*2*800)*v*32768#设置声音频率为-32768到32768，并且为正弦变化曲线
    s=int(s)
    fd=struct.pack("h",s)#二进制写入
    f.writeframes(fd)
    t+=dt
f.close()