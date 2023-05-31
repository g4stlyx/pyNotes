# -*- coding: utf-8 -*-

data = '{"qwe":"ewq","asd":"dsa"}'

import json 

y = json.loads(data)

print(y["qwe"])
print(y["asd"])
      
customer = {
    "firstName":"engin",
    "lastName":"demiroğ",
    }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Engin"))