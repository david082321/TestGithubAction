# -*-coding:utf8-*-
import os, requests, requests_toolbelt

UserAgent = os.environ["user_agent"]
Cookie = os.environ["cookie"]
bot_token = os.environ["bot_token"]
chat_id = os.environ["chat_id"]

url = os.environ["url_add"]
headers = {"User-Agent":UserAgent,"Cookie":Cookie,}
file_payload = {'subject':'1',
                'savealbumid':'0',
                'newalbum':'请输入相册名称',
                'file':'',
                'file':'',
                'message':'1',
                'classid':'0',
                'tag':'',
                'friend':'3',
                'password':'',
                'selectgroup':'',
                'target_names':'',
                'blogsubmit':'true',
                'formhash':'b9d7dccc',
                }
m = requests_toolbelt.MultipartEncoder(file_payload)
headers['Content-Type'] = m.content_type
requests.post(url=url, data=m, headers=headers)

url = os.environ["url_view"]
headers = {"User-Agent":UserAgent,"Cookie":Cookie}
response = requests.get(url=url, headers=headers).content.decode("utf8")
if '"blog_delete_' in response:
    blog_id = response.split('"blog_delete_')[1].split('"')[0]
    url = os.environ["url_delete"]+str(blog_id)
    args = {"deletesubmit":"true",
            "formhash":"b9d7dccc",
            "btnsubmit":"true",}
    requests.post(url=url, data=args, headers=headers)
else:
  requests.get(url="https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+chat_id+"&text=Cookie 出錯")
