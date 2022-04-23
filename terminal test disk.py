import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"𝙛𝙖𝙧𝙩@𝙪𝙗𝙪𝙣𝙩𝙪")

print(f"""
{b+Fore.WHITE}   
  terminal test thing
 {b+Fore.RED}                                 z-                                         
     {b+Fore.GREEN}                            d$                                          
          {b+Fore.BLUE}                     .$$F                                          
              {b+Fore.WHITE}                z$$$                             d$$b     .$$  
-                     {b+Fore.RED}       J$$$$                            d$. $$$$$$$$$  
  \                {b+Fore.BLUE}         4$$$$$                           z$$$$$$$$$$$$"  
   "c               {b+Fore.RED}        $$$$$$F                         d$$$*$$$$"       
    "$e.      .     {b+Fore.GREEN}       $$$$$$$$                       .$$$$$             
     3$$$$$$P"        {b+Fore.RED}     $$$$$$$$c                    .$$$$$$              
      $$$$$"          {b+Fore.BLUE}     $$$$$$$$$r                .e$$$$$$$F              
      *$$$b                $$$$$$$$$$c           .e$$$$$$$$$$P               
      '$P "$.              $$$$$$$$$$$b.    .ee$$$$$$$$$$$$$P                
       $   ^$$.             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F                 
       "     $$$$e..      .e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"                  
      4       "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P                    
                *$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P                      
                  "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*                        
                     "*$$$$$$$$$$$$$$$$$$$$$$$$$$$"                          
                         "*$$$$$$$$$$$$$$$$$$$$$"                            
                             *$$$$$$$$$$$$$$$"                               
                                  """"""""  
""")

token = input(f"{b+Fore.GREEN} fart@ubuntu:{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
if r.status_code == 201:
        pass
else:
        print(f"{b+Fore.WHITE} > fart@ubuntu failed, try again")
        token = input(f"{b+Fore.GREEN} fart@ubuntu:{Fore.RESET}: ")
        input()
        