import requests, random, sys, yaml, time

class Discord:
    
    def __init__(self, t):
        self.base = "https://discord.com/api/v9"
        self.auth = { 'authorization': t }
    
    def getMe (self):
        return requests.get(self.base + "/users/@me", headers=self.auth).json()
    
    def getMessage(self, cid, l):
        return requests.get(self.base + "/channels/" + str(cid) + "/messages?limit=" + str(l), headers=self.auth).json()
    
    def sendMessage(self, cid, txt):    
        return requests.post(self.base + "/channels/" + str(cid) + "/messages", headers=self.auth, json={ 'content': txt }).json()
    
    def replyMessage(self, cid, mid, txt):    
        return requests.post(self.base + "/channels/" + str(cid) + "/messages", headers=self.auth, json={ 'content': txt, 'message_reference': { 'message_id': str(mid) } }).json()
    
    def deleteMessage(self, cid, mid):
        return requests.delete(self.base + "/channels/" + str(cid) + "/messages/" + str(mid), headers=self.auth)

def quote():
    quote = requests.get("https://raw.githubusercontent.com/arisaripin/quote/master/packages/quote.json").json()
    return random.choice(list(quote))['quote']

def simsimi(lc, txt):
    simsimi = requests.post("https://api.simsimi.vn/v1/simtalk", data={ 'lc': lc, 'text': txt}).json()
    return simsimi['message']

def main():
    with open('config.yaml') as cfg:
        cfg = yaml.load(cfg, Loader=yaml.FullLoader)
    
    if not cfg['TOKEN']:
        print("[!] Please provide discord token at config.yaml!")
        sys.exit()
    
    if not cfg['CHANNEL']:
        print("[!] Please provide channel at config.yaml!")
        sys.exit()
    
    mode = cfg['MODE']
    lang = cfg['LANG']
    reply = cfg['REPLY']
    delete = cfg['DELETE']
    delay = cfg['DELAY']
    repost = cfg['REPOST']

    if not mode: 
        mode = "quote"
    
    if not lang: 
        lang = "en"
    
    if not repost: 
        repost = "100"
    
    while True:
        for token in cfg['TOKEN']:
            try:
                for channel in cfg['CHANNEL']:

                    discord = Discord(token)
                    me = discord.getMe()['username'] + "#" + discord.getMe()['discriminator']

                    if mode == "quote":
                        send = discord.sendMessage(channel, quote())
                        print("[{}][{}][QUOTE] {}".format(me, channel, quote()))
                        
                        if delete:
                            discord.deleteMessage(channel, send['id'])
                            print("[{}][DELETE] {}".format(me, send['id']))

                    elif mode == "reply":
                        res = discord.getMessage(channel, "1")
                        getlast = list(reversed(res))[0]
                        reply = random.choice(open("custom.txt").readlines())
                        send = discord.replyMessage(channel, getlast['id'], reply)
                        print("[{}][{}][REPLY] {}".format(me, channel, reply))
                        
                        if delete:
                            discord.deleteMessage(channel, send['id'])
                            print("[{}][DELETE] {}".format(me, send['id']))
                    
                    elif mode == "repost":
                        res = discord.getMessage(channel, random.randint(1,repost))
                        getlast = list(reversed(res))[0]
                        send = discord.sendMessage(channel, getlast['content'])
                        print("[{}][{}][REPOST] {}".format(me, channel, getlast['content']))
                        
                        if delete:
                            discord.deleteMessage(channel, send['id'])
                            print("[{}][DELETE] {}".format(me, send['id']))
                    
                    elif mode == "simsimi":
                        res = discord.getMessage(channel, "1")
                        getlast = list(reversed(res))[0]
                        simi = simsimi(lang, getlast['content'])

                        if  reply:
                            send = discord.replyMessage(channel, getlast['id'], simi)
                            print("[{}][{}][SIMSIMI] {}".format(me, channel, simi))
                        
                        else:
                            send = discord.sendMessage(channel, simi)
                            print("[{}][{}][SIMSIMI] {}".format(me, channel, simi))
                        
                        if delete:
                            discord.deleteMessage(channel, send['id'])
                            print("[{}][DELETE] {}".format(me, send['id']))
                    
                    elif mode == "custom":
                        custom = random.choice(open("custom.txt").readlines())
                        send = discord.sendMessage(channel, custom)
                        print("[{}][{}][CUSTOM] {}".format(me, channel, custom))
                        
                        if delete:
                            discord.deleteMessage(channel, send['id'])
                            print("[{}][{}] [DELETE]".format(me, send['id']))
            
            except:
                print(f"[Error] {token} : Token is invalid or kicked from server")
        
        print("-------------------- [ Delay for {} seconds ] --------------------".format(delay))
        time.sleep(delay)

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")