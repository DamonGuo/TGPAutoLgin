#-*- coding: utf-8 -*-
import win32api,win32gui, win32con
import os
import time
#os.startfile('D:\\Program Files\\Tencent\\TGP\\tgp_daemon.exe')
#time.sleep(5)
label = u"腾讯游戏平台"
#根据窗口名获取窗口句柄，
h = win32gui.FindWindow('Edit','')
#Ex = win32gui.FindWindowEx(h,None,None,None)
#print(h)
#print(Ex)
win32gui.SetForegroundWindow(h)
#根据窗口句柄使窗口位于焦点位置
time.sleep(3)
UserNum = "your id"
PassWord = "your password"

lowercase = dict(zip(range(97,123),[[x,0] for x in range(65,91)]))
#小写字母对应的ascii码为97~122，对应的键盘值为65~90
uppercase = dict(zip(range(65,91),[[x,1] for x in range(65,91)]))
#大写字母对应的ascii码为65~91，对应的键盘值为小写字母的键盘值加shit
number = dict(zip(range(48,58), [[x,0] for x in range(48,58)]))
#print number
#0~9数字对应的asicc编码为48~57， 对应的键盘值为48~58
symbol01 = {32: [32, 0], 33: [49, 1], 34: [222, 1], 35: [51, 1], 36: [52, 1], 37: [53, 1], 38: [55, 1], 39: [222, 0], 40: [57, 1], 41: [48, 1], 42: [56, 1], 43: [187, 1], 44: [188, 0], 45: [189, 0], 46: [190, 0], 47: [191, 0]}
symbol02 = {64: [50, 1], 58: [186, 1], 59: [186, 0], 60: [188, 1], 61: [187, 0], 62: [190, 1], 63: [191, 1]}
symbol03 = {96: [192, 0], 91: [219, 0], 92: [220, 1], 93: [221, 0], 94: [54, 1], 95: [189, 1]}
symbol04 = {123: [219, 1], 124: [220, 1], 125: [221, 1], 126: [192, 1]}
#print symbol04
passworddict = {}
passworddict = dict(lowercase.items()+uppercase.items()+number.items()+symbol01.items()+symbol02.items()+symbol03.items()+symbol04.items())
#print passworddict

for i in range(0,1):#模拟输入tab键，选中账号输入框
    win32api.keybd_event(9,0,0,0)      
    win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.2)
time.sleep(0.5)


for i in range(0,12):#删除输入框中的字符
    win32api.keybd_event(8,0,0,0)
    win32api.keybd_event(8,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.2)

  
for i in range(0,len(UserNum)):
    key = ord(UserNum[i])
    skey = int(passworddict[key][0])
    if  passworddict[key][1] == 1:
        win32api.keybd_event(16,0,0,0) 
        #获取账号中对应字符中的对应ascii编码
        win32api.keybd_event(skey,0,0,0)
        win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(skey,0,win32con.KEYEVENTF_KEYUP,0)
    else:
        #win32api.keybd_event(16,0,0,0) 
        #获取账号中对应字符中的对应ascii编码
        win32api.keybd_event(skey,0,0,0)
        #win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(skey,0,win32con.KEYEVENTF_KEYUP,0)

    time.sleep(0.2)
    #模拟账号中每个字符的输入，每次输入后睡眠0.2s
time.sleep(0.5)
win32api.keybd_event(9,0,0,0)
win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)
#再次模拟tab键输入，选中密码输入框
time.sleep(0.5)
for i in range(0,len(PassWord)):
    key = ord(PassWord[i])
    skey = int(passworddict[key][0])
    if passworddict[key][1] == 1:
        win32api.keybd_event(16,0,0,0)
        #获取账号中对应字符中的对应ascii编码
        win32api.keybd_event(skey,0,0,0)
        win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(skey,0,win32con.KEYEVENTF_KEYUP,0)
    else:
        #win32api.keybd_event(16,0,0,0)
        #获取账号中对应字符中的对应ascii编码
        win32api.keybd_event(skey,0,0,0)
        #win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(skey,0,win32con.KEYEVENTF_KEYUP,0)
        
    time.sleep(0.2)

    '''
    if ord(PassWord[i])>=97 and ord(PassWord[i])<=122:
        key = ord(PassWord[i])-32
    elif ord(PassWord[i]) == 64:
        win32api.keybd_event(16,0,0,0)
        win32api.keybd_event(50,0,0,0)
        win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)
        continue
    else:
        key = ord(PassWord[i])
    win32api.keybd_event(key,0,0,0)
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.2)
    '''
   
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP)
#模拟输入enter键，确认登陆

