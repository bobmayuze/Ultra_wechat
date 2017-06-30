from wxpy import *
import requests
import time

# Init the env, login

bot = Bot()
print("========INIT SUCCESSFULLY=====")
frs = bot.friends()
dummy = ''
# yuze = bot.friends().search('Yuze Ma 鱼哲')[0]
apiUrl = 'http://www.tuling123.com/openapi/api'
data = {
	"key": "c306b319ca4541d78a6413ccc16c8119",
	"info": "你好呀",
	"userid":"123"
}


@bot.register()
def just_print(msg):
    # 打印消息
    print(msg)


# @bot.register([yuze, Group], TEXT)
@bot.register(bot.friends(), TEXT)
def auto_reply(msg):
    # 如果是群聊，但没有被 @，则不回复
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        # 回复消息内容和类型
        time.sleep(5)
        print(msg.raw)
        data["info"] = msg.text
        try:
            res = requests.post(apiUrl, data = data).json()
            return res["text"]
        except:
            return "Connection lost"

@bot.register(Group, TEXT)
def auto_reply(msg):
    # 如果是群聊，但没有被 @，则不回复
    # if isinstance(msg.chat, Group) and not msg.is_at:
    #     data["info"] = msg.text
    #     try:
    #         res = requests.post(apiUrl, data = data).json()
    #         return res["text"]
    #     except:    
    #         return "其实我都记着呢！"
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        # 回复消息内容和类型
        data["info"] = msg.text
        try:
            res = requests.post(apiUrl, data = data).json()
            return res["text"]
        except:
            return "Connection lost"

@bot.register(bot.friends(), PICTURE)
def auto_reply(msg):
    # 如果是群聊，但没有被 @，则不回复
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        # 回复消息内容和类型
        print(msg.raw)
        return "我还看不懂这个图呢"

