import itchat
import datetime
import time
import yulu
import random
# 登录微信
itchat.auto_login(hotReload=False)
# 获取朋有列表
friends_list = itchat.get_friends(update=True)
name = itchat.search_friends(name=u'阿樱')
Aying = name[0]["UserName"]
#获取时间
while True:
    now= datetime.datetime.now()
    if now.hour == 6 and now.minute == 00:
        itchat.send('早安',Aying)
        itchat.send(yulu.qinghua[random.randint(0,50)],Aying)
    elif now.hour == 22 and now.minute == 00:
        itchat.send('晚安',Aying)
        itchat.send(yulu.qinghua[random.randint(0,50)],Aying)
    time.sleep(30)
    
