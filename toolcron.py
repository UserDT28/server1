import requests
import os
import time
os.system('clear')
cpr=("\033[39m•  \033[1;37mYoutuber : \033[33mD T I Z E N 2\n\033[39m•  Zalo : \033[36m0338743623\n\033[39m•  \033[31mRANDOM : \033[35mRANDOM\033[36mDTIZEN2\033[37m.SITE")
print(cpr)
momo=input('\033[1;37mLink Cron Momo \n=>\033[33m')
bank= input('\033[1;37mLink Cron Bank\n=>\033[33m')
tsr= input('\033[1;37mLink Cron TSR\n\033[33m')
kgh= int(input('Bao Nhiêu Job Thì Dừng\n ○Job :'))
delay=int(input('Delay : '))
os.system('clear')
count = 0
bd = 0
while (count <= kgh):
 # tạo requests :
 rq1 = requests.get(momo).text
 rq2 = requests.get(bank).text
 rq3 = requests.get(tsr).text
 kgh = kgh + 1
 bd = bd + 1
 count = count + 1
 # viết ra requests
 print (f'[{count}] Cron "{momo} " Thành Công ! ')
 print (f'[{count}] Cron "{bank}" Thành Công ! ')
 print (f'[{count}] Cron "{tsr} " Thành Công ! ')
 time.sleep(delay) # Sleep for 10 seconds
 if (25 <= bd):
   os.system('clear')
   bd = bd - 25
   print(cpr)


   