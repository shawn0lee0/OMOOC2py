# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('GB2312') #在CMD中运行编码为GB2312，在Python中应修改为UTF-8

UDP_IP = "127.0.0.1"
UDP_PORT = 9527
ip_address = (UDP_IP,UDP_PORT)


<<<<<<< HEAD
=======

>>>>>>> 6f468913b017a98f5585e0aec53196fc0a0f7b6b
def main():

    print '''
    --欢迎来到*** %s的日记本--
    --输入‘r’---载入历史记录
    --输入‘AI’ or ‘ai’---开启人工智能聊天模式
    '''%UDP_IP
    sock = socket.socket(socket.AF_INET, # Internet地址族
                     socket.SOCK_DGRAM) # UDP协议
                     
<<<<<<< HEAD
    print '''
    欢迎来到*** %s的日记本--********
    输入‘r’---载入历史记录
    输入‘AI’ or ‘ai’---开启人工智能聊天模式
    
    '''%UDP_IP
    MESSAGE =  raw_input("写点什么呢:") #一次只能一行内容
    
=======

    MESSAGE =  raw_input("我:") #一次只能一行内容
    sock.sendto(MESSAGE,ip_address)
    print "AI:",sock.recv(1024)

'''
>>>>>>> 6f468913b017a98f5585e0aec53196fc0a0f7b6b
    if MESSAGE == 'r':
        print "正在打开日志……" 
        sock.sendto(MESSAGE,ip_address)
        print sock.recv(1024)
   
    else:
     sock.sendto(MESSAGE,ip_address)
     print "UDP target IP:", UDP_IP
     print "UDP target port:", UDP_PORT
     print "已发送信息:", MESSAGE
'''
while 1:
    main()