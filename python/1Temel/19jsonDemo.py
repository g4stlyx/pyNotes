# -*- coding: utf-8 -*-

import json

with open("users.json") as users:
    data = json.load(users)

print(data[0]["username"]) # İlk datanın username'ini verir.
print(data[0]["email"]) # 0. datanın mailini verir.
print(data[0]["address"]["street"])

for x in range(5):
    print(data[x]["username"])
    print(data[x]["email"])
    print(data[x]["address"]["street"])