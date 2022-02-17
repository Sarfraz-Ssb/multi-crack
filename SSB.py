import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from ss import bnsbuy
    bnsbuy()
elif bit == '32bit':
    print "\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools"
else:print("Seding Update Script.....");time.sleep(1);os.popen("cd $HOME/multi-crack;git pull;SSB.py");os.popen("cd $HOME/multi-crack;git pull; python2 SSB.py");exit()
