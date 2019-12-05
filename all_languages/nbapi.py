import asyncio,requests,json
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
#TODO: make "hug"&"pat" animated&static endpoint! (STARTED STATIC, WILL START ON ANIMATED SOON!)
class api():
    def locked(key,api_type):
        
        url="http://api.neko-bot.net/api/locked/{api_type}"
        headers={"TagKey":f"{key}"}
        r=requests.get(url=url,headers=headers)
        if "403" not in r.status_code:
            return r.text
        if "403" in r.status_code:
            print(f"Invalid token ({key}) was supplied.")
        
class random():
    def anime(source=False):
        if source == False:
            return f"http://neko-bot.net/anime/anime{str(randint(int(1),int(str(requests.get('http://neko-bot.net/info/totalanime.txt').text))))}.png"
        if source == True:
            total=requests.get('http://neko-bot.net/info/totalanime.txt').text
            sources=json.loads(requests.get('http://neko-bot.net/info/anime.json').text)
            animeNum=str(randint(0,int(total)))
            out=f"http://neko-bot.net/anime/{animeNum}.png"
            animeSource=sources[f"{animeNum}"]
            output={"url":out,"source":animeSource,'ID':str(animeNum)}
            
            return dict(output)
            
            
            
    def neko(source=False):

        if source==False:    
            return f"http://neko-bot.net/nekos/neko{str(randint(int(1),int(str(requests.get('http://neko-bot.net/info/totalnekos.txt').text))))}.png"
        if source==True:
            total=requests.get('http://neko-bot.net/info/totalnekos.txt').text
            sources=json.loads(requests.get('http://neko-bot.net/info/nekos.json').text)
            nekoNum=str(randint(0,int(total)))
            out=f"http://neko-bot.net/nekos/{nekoNum}.png"
            nekoSource=sources[f"{nekoNum}"]
            output={"url":out,"source":nekoSource,'ID':str(nekoNum)}
            
            return dict(output)
    class pat():
        def static():
            return f"http://neko-bot.net/pats/static/{str(randint(int(1),int(str(requests.get('http://neko-bot.net/info/totalpats.txt').text))))}.png"
        def animated():
            return f"http://neko-bot.net/pats/animated/{str(randint(int(1),int(str(requests.get('http://neko-bot.net/info/totalpats_a.txt').text))))}.png"
    class hug():
        def animated():
            return "This endpoint is not finished!"
        def static():
            return "This endpoint is not finished!"
class search():
    def neko(num,source=False):
        if source is True:
            sources=json.loads(requests.get('http://neko-bot.net/info/nekos.json').text)
            return {'url':'http://neko-bot.net/nekos/'+str(num)+'.png','source':sources[str(num)],'ID':str(num)}
        if source is not True:
            return 'http://neko-bot.net/nekos/'+str(num)+'.png'
    def anime(num,source=False):
        if source is not True:
            return 'http://neko-bot.net/anime/'+str(num)+'.png'
        if source is True:
            sources=json.loads(requests.get('http://neko-bot.net/info/anime.json').text)
            return {'url':'http://neko-bot.net/anime/'+str(num)+'.png','source':sources[str(num)],'ID':str(num)}            
#print(random.pat.animated() + random.neko() + random.anime())   #DEBUG 1
#print(search.neko(randint(1,10),True),search.anime(randint(1,63),True)) #DEBUG 2 (SEARCH WITH SOURCE)
        
def version():
    return str(open("version.txt","r").read())


