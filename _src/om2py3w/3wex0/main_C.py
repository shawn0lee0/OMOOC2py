# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('GB2312') #��CMD�����б���ΪGB2312����Python��Ӧ�޸�ΪUTF-8

UDP_IP = "127.0.0.1"
UDP_PORT = 9527
ip_address = (UDP_IP,UDP_PORT)


<<<<<<< HEAD
=======

>>>>>>> 6f468913b017a98f5585e0aec53196fc0a0f7b6b
def main():

    print '''
    --��ӭ����*** %s���ռǱ�--
    --���롮r��---������ʷ��¼
    --���롮AI�� or ��ai��---�����˹���������ģʽ
    '''%UDP_IP
    sock = socket.socket(socket.AF_INET, # Internet��ַ��
                     socket.SOCK_DGRAM) # UDPЭ��
                     
<<<<<<< HEAD
    print '''
    ��ӭ����*** %s���ռǱ�--********
    ���롮r��---������ʷ��¼
    ���롮AI�� or ��ai��---�����˹���������ģʽ
    
    '''%UDP_IP
    MESSAGE =  raw_input("д��ʲô��:") #һ��ֻ��һ������
    
=======

    MESSAGE =  raw_input("��:") #һ��ֻ��һ������
    sock.sendto(MESSAGE,ip_address)
    print "AI:",sock.recv(1024)

'''
>>>>>>> 6f468913b017a98f5585e0aec53196fc0a0f7b6b
    if MESSAGE == 'r':
        print "���ڴ���־����" 
        sock.sendto(MESSAGE,ip_address)
        print sock.recv(1024)
   
    else:
     sock.sendto(MESSAGE,ip_address)
     print "UDP target IP:", UDP_IP
     print "UDP target port:", UDP_PORT
     print "�ѷ�����Ϣ:", MESSAGE
'''
while 1:
    main()