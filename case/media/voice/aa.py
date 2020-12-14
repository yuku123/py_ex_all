import matplotlib.pyplot as plt
import  wave
import struct

fig=plt.figure()
ax=fig.add_subplot(1,1,1)#如果参数是349的意思是：将画布分割成3行4列，图像画在从左到右从上到下的第9块
plt.ion()#使matplotlib的显示模式转换为交互（interactive）模式。即使在脚本中遇到plt.show()，代码还是会继续执行。
read_size=200#每次绘画的帧数
pass_f=0#跳过前pass的帧数
draw_channel=0
stay_time=1.0

file=wave.open("v1.wav","r")

frame_rate=file.getframerate()
frames = file.getnframes()#得到频率
channels=file.getnchannels()#得到声道数
draw_channel=draw_channel %channels
i=0
x_data=[x / read_size for x in range(read_size)]
fmt="h" * (read_size * channels)

while i<frames:
    fs=file.readframes(read_size)
    i+=read_size
    if pass_f > 0:
        pass_f-=1
        continue
    f_data = struct .unpack(fmt,fs)  # f_data中包含多个声道的声音
    y_data =[]
    for j in range(0,len(f_data)):
        if j%channels==draw_channel:
            y_data.append(f_data[j]/32768.0)
    lines = ax.plot(x_data, y_data, 'g-', lw=1)
    plt.pause(stay_time)
    ax.lines.remove(lines[0])
file.close()