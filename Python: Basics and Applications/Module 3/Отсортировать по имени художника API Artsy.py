import requests
import json


client_id = 'db311cfe37ec4bc74a61'
client_secret = 'ba1d22427d386b0b79ce4403c063b2ec'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
names = {}
with open('test.txt') as f:
    for req_id in f.read().splitlines():
        res = requests.get(f"https://api.artsy.net/api/artists/{req_id}", headers=headers)
        res.encoding = 'utf-8'
        data = json.loads(res.text)
        names[data['sortable_name']] = int(data['birthday'])
        names = dict(sorted(names.items(), key=lambda item: (item[1], item[0])))
    print(*names, sep='\n')
