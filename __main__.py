import os
import sys

def update():
    #os.remove('/data/data/com.termux/files/home/metasploit')
    os.system('rm -rf /data/data/com.termux/files/home/metasploit &&  git clone https://github.com/tamer200585/metasploit')

if sys.argv[1] == 'update': update()
