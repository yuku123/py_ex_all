import os
import urllib.request
import urllib

url = 'https://cdn.umowang.com/media/fgo/servant/card/xx.png'

def download(img_url,file_name,count):
    img_url = 'https://cdn.umowang.com/media/fgo/servant/card/263A.png'
    file_path = '/Users/zifang/Downloads/fate'
    try:
        # 是否有这个路径
        if not os.path.exists(file_path):
            # 创建路径
            os.makedirs(file_path)
            # 获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        print(file_suffix)
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        print(filename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filename=filename)
    except Exception as e:
        print(e)
        if count <= 3:
            count = count+1
            print(file_name+"错误：重新下载"+str(count))
            download(img_url,file_name,count)

for i in range(1,264):
    for j in range(ord("A"),ord('Z')):
        number = '000'+str(i)+str(chr(j))
        number = number[-4:]
        temp = url.replace("xx",number)
        # # 创建两个线程
        # try:
        #     thread.start_new_thread(download, (temp,number,0))
        # except:
        #     print
        #     "Error: unable to start thread"
        download(temp,number,0)

