#-*- coding:utf-8 -*-

import itchat
import math
import os
import PIL.Image as Image

# 开启热登录，短时间内退出，再次进入可以不用扫码登录
itchat.auto_login(hotReload=False)
friends = itchat.get_friends(update=True)

# 下载所有好友的头像图片
num = 0
imgPath = './headImg/'
if not os.path.exists(imgPath):
    os.mkdir(imgPath)

for i in friends:
    img = itchat.get_head_img(i["UserName"])
    with open(imgPath + str(num) + ".jpg", 'wb') as f:
        f.write(img)
        f.close()
        num += 1

length = len(os.listdir(imgPath))
# 根据总面积求每一个的大小
each_size = int(math.sqrt(float(810 * 810) / length))
# 每一行可以放多少个
lines = int(810 / each_size)
# 生成一张空白大图片
image = Image.new('RGBA', (810, 810), 'white')
x = 0
y = 0

#把每张头像依次粘贴到大图上
for i in range(0, length):
    try:
        img = Image.open(imgPath + str(i) + ".jpg")
    except IOError:
        print(i)
        print("image open error")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image.save(imgPath + "myFriends.jpg")
# 通过文件传输助手发送到自己微信中
itchat.send_image(imgPath + "myFriends.jpg", 'filehelper')
image.show()