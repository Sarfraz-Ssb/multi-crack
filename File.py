import os, time, platform, base64
os.system("cd $HOME/")
os.system("termux-setup-storage")
try:
       __import__("safu").like()
   except Exception as e:
       exit(str(e))
