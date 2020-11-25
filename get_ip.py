#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 先讀取文件裡面的ip
# try 能不能連線
# catch 如果不能連線 
#           連API 取得IP
#           寫入文件


# In[3]:


import requests
from bs4 import BeautifulSoup
import time
import os


# In[ ]:

try:
    f = open( 'ip.chyu', 'r' )
    previous = f.read()
    f.close()
    print(previous)
except:
    f = open('ip.chyu' , 'w')
    print(os.popen('dir').read())
    print("AAAAAA")
    f.write('')
    f.close
    previous = ''

# In[ ]:


try:
    response = requests.get(previous ,timeout = 3)
    soup = BeautifulSoup(response.text, "html.parser")
    print("Current ip : " + response.text)
except:
    #print(response.text)
    ip = requests.get('https://tool.magiclen.org/ip/')
    print("NO conect so new ip = " + ip.text)
    newIP = ip.text
    to_file = "http://" + newIP + "/test.php" 
    print(to_file)
    f = open( 'ip.chyu', 'w' )
    f.write(to_file)
    f.close()
    f = open( "D:/0987/Documents/GitHub/yuwaylan.github.io/ip.html", 'w' )
    f.write(newIP)
    f.close()
    current_Time = time.ctime()
    print("previous:[" + previous + "], Time:[" + current_Time + "]")
    to_log = "previous:[" + previous + "], Time:[" + current_Time + "]\n"
    f = open( 'ip_log.chyu', 'a' )
    f.write(to_log)
    f.close()
    e=os.system("toip.cmd")
    print(e)
# 


# In[9]:


e= os.system('D:/0987/Documents/GitHub/yuwaylan.github.io/togit.bat')
print(e)


# 
