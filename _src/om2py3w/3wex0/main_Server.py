# -*- coding: utf-8 -*-

import socket
import sys,codecs
import datetime
from chat import *

reload(sys)
sys.setdefaultencoding('GB2312') #适用于win-cmd运行

UDP_IP = "127.0.0.1"
UDP_PORT = 9527


def ai_chat(data):
    chat = Chat()
<<<<<<< HEAD
    info = data
    chat.send(info)
    chat.init()
    chat.get()
    
    
=======
    chat.init()
    chat.send(data)
    AI_text = chat.send.text 
    return AI_text
>>>>>>> 6f468913b017a98f5585e0aec53196fc0a0f7b6b


    
def save(data,diary):
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") #参考第一周代码
    s = open(diary,'a')
    s.write(otherStyleTime+":"+data+ "\n")
    s.close()
    print "日志已保存至%s" %diary

#参考第一周代码    
def main():
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(('', UDP_PORT))        #''表示接收域内所以IP地址
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    diary =  addr[0] + ".txt"  #以IP地址.txt 格式保存,并将diary_txt作为全局变量
    print "*** %s的日记本--服务器端********\n" %addr[0]

    #if data == 'ai' or data == 'AI':
    ai_chat(data)
<<<<<<< HEAD
=======
    print AI_text
    sock.sendto(AI_text,addr)
>>>>>>> 6f468913b017a98f5585e0aec53196fc0a0f7b6b
'''    
    if data=='r' or data=='R':
        print "Loading..."
        #open_diary(diary)
        o = open(diary,'r')
        content = o.read()
        #print type(content)
        sock.sendto(content,addr)
        o.close()
        print  "日志已发送至%s" %addr[0]
    else:
        print "已读:", data, "来自-->", addr[0]
        save(data,diary)
        
'''        


while 1:
    main()



