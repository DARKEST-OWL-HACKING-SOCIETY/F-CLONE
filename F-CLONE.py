import os, sys, platform,time
os.system('rm -rf /downloads/h.py')
os.system('rm -rf /sdcard/h.py')
os.system('rm -rf h.py')
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import i
else:
    exit()
