# 给好友发送天气情况
#coding=utf-8
import itchat
import weather

itchat.auto_login(hotReload=True)
friends_list = itchat.get_friends(update=True)
name = itchat.search_friends(name=u'阿樱')
Aying = name[0]["UserName"]


message_list = weather.main('广州') # 发送天气情况
itchat.send(message_list,Aying)










