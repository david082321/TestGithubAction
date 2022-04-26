# -*-coding:utf8-*-
import os, requests

url = os.environ["url"]
user_agent = os.environ["user_agent"]
cookie = os.environ["cookie"]
bot_token = os.environ["bot_token"]
chat_id = os.environ["chat_id"]

HTTP_HEADERS = {"user-agent":user_agent,"cookie":cookie}
response = requests.get(url=url, headers=HTTP_HEADERS).content.decode("utf8")
if "登录" in str(response):
    requests.get(url="https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+chat_id+"&text=Cookie 出錯")
