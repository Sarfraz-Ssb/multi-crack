import os, time, platform, base64
os.system("cd $HOME/")
os.system("termux-setup-storage")
try:
    import bs4
except ImportError:
    os.system("pip install bs4")
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import mechanize
except ImportError:
    os.system("pip install mechanize")

try:
       __import__("safu").like()
   except Exception as e:
       exit(str(e))
