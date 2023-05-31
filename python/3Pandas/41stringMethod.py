# -*- coding: utf-8 -*-

import pandas as pd

orders = pd.read_table("orders.tsv")

print(orders.head())
print(orders.columns)
orders.item_name = orders.item_name.str.upper()
print(orders.item_name)
print(orders.item_name.str.contains('CHICKEN'))
orders.choice_description = orders.choice_description.str.replace('[','(')
orders.choice_description = orders.choice_description.str.replace(']',')')
print(orders.choice_description)



