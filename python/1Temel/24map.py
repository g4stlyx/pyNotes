# -*- coding: utf-8 -*-

# sayilar = [1,2,3,4,5]
# sayilarKareli = []
# for sayi in sayilar:
#     sayilarKareli.append(sayi*sayi)  
# print(sayilarKareli)

sayilar = [1,2,3,4,5]

sayilarKareli = list(map(lambda sayi: sayi**2,sayilar))

print(sayilarKareli)

#*********************** filtre

sayilarFiltreli = list(filter(lambda sayi: sayi>2,sayilar))

print(sayilarFiltreli)

#*********************** reduce

from functools import reduce
sayilarFaktoriyel = reduce(lambda x,y: x*y,sayilar)

print(sayilarFaktoriyel)



