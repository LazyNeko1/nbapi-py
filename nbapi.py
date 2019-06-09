import asyncio 
from random import randint
import urllib
#Note: Using this API you are going to be using a API that MAY (unlikely) But MAY send NSFW results.
#If that happens, DM my owner (LazyNeko#5644), or join the Neko Support Server from the website.

#Nothing much yet :3

#                   #-------------------------------------------------#
#                       To join: Copy the below link.  
#                       https://discord.gg/RauzUYK
#                   #--------------------------------------------------#

#You may edit this code to your needs. I dont mind ;3

class random():
    def anime():
        for line in urllib.request.urlopen('http://neko-bot.net/info/totalposts.txt'):
            animemax=line
            animemin=1
            total=randint(int(postmin).int(postmax))
    def neko():
        for line in urllib.request.urlopen('http://neko-bot.net/info/totalnekos.txt'):
                   
            nekomax=line

            nekomin=6
            total=randint(int(nekomin),int(nekomax))
                
            return 'http://neko-bot.net/nekos/neko'+str(total)+'.png'



class search():
    def neko(num):
        return 'http://neko-bot.net/nekos/neko'+str(num)+'.png'
    def anime(num):
        return 'http://neko-bot.net/posts/post'+str(num)+'.png'
