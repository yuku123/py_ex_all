from fiction.threadbean import threadbean


url='http://www.biquge.com.tw/17_17506/'

for i in range(1):
    for j in range(10):
        number = i*1000 + j
        strs = str('http://www.biquge.com.tw/#_?/').replace('#', str(i)).replace("?",str(number))
        url = strs
        print(strs)
        threads = threadbean(url)
        threads.start()



# threads = threadbean(url)
# threads.start()