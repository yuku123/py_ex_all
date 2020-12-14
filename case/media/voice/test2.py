from pylab import*
from scipy.io import wavfile

sampFreq, snd = wavfile.read('/Users/zifang/Music/网易云音乐/b.wav')


timeArray = arange(0, 5060.0, 1)   #[0s, 1s], 5060个点
timeArray = timeArray / sampFreq   #[0s, 0.114s]
timeArray = timeArray * 1000       #[0ms, 114ms]

s1 = snd[:, 0]

plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')

n = len(s1)
p = fft(s1)

nUniquePts = ceil((n+1)/2.0)
p = p[0:nUniquePts]
p = abs[p]

p = p / float(n)    #除以采样点数，去除幅度对信号长度或采样频率的依赖
p = p**2            #求平方得到能量

#乘2（详见技术手册）
#奇nfft排除奈奎斯特点
if n % 2 > 0:       #fft点数为奇
    p[1:len(p)] = p[1:len(p)]*2
else:               #fft点数为偶
    p[1:len(p)-1] = p[1:len(p)-1] * 2

freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n)
plot(freqArray/1000, 10*log10(p), color='k')
xlabel('Freqency (kHz)')
ylabel('Power (dB)')