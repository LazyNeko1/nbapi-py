import asyncio,requests
from random import randint

#Note: Using this API you are going to be using a API that MAY (unlikely) But MAY send NSFW results.
#If that happens, DM my owner (LazyNeko#5644), or join the Neko Support Server from the website.

#Nothing much yet :3

#                   #-------------------------------------------------#
#                       To join: Copy the below link.  
#                       https://discord.gg/RauzUYK
#                   #--------------------------------------------------#

#You may edit this code to your needs. I dont mind ;3
#TODO: make requests smaller (DONE)
class random():
    def anime():
        return f"http://neko-bot.net/anime/anime{str(randint(int(1),int(str(requests.get('http://neko-bot.net/info/totalanime.txt').text))))}"
    def neko():

                
            return f"http://neko-bot.net/nekos/neko{str(randint(int(1),int(str(requests.get('http://neko-bot.net/info/totalnekos.txt').text))))}"
    def pat():
        return f"http://neko-bot.net/pats/{str(randint(int(1),int(str(requests.get('http://neko-bot.net/info/totalpats.txt').text))))}"


class search():
    def neko(num):
        return 'http://neko-bot.net/nekos/neko'+str(num)+'.png'
    def anime(num):
        return 'http://neko-bot.net/posts/post'+str(num)+'.png'
#print(random.pat() + random.neko() + random.anime())   #DEBUG
