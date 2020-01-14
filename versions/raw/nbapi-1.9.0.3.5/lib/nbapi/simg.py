import requests,json
class search():
    def neko(num, source=False):
        if source is True:
            sources = json.loads(requests.get('http://neko-bot.net/info/nekos.json').text)
            return {'url': 'http://neko-bot.net/nekos/' + str(num) + '.png', 'source': sources[str(num)],
                    'ID': str(num)}
        if source is not True:
            return 'http://neko-bot.net/nekos/' + str(num) + '.png'

    def anime(num, source=False):
        if source is not True:
            return 'http://neko-bot.net/anime/' + str(num) + '.png'
        if source is True:
            sources = json.loads(requests.get('http://neko-bot.net/info/anime.json').text)
            return {'url': 'http://neko-bot.net/anime/' + str(num) + '.png', 'source': sources[str(num)],
                    'ID': str(num)}
        # print(random.pat.animated() + random.neko() + random.anime())   #DEBUG 1
