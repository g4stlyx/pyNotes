# -*- coding: utf-8 -*-

#iterasyon: bir listenin elemanlarını tek tek dolaşma eg. for loop

sehirler = ["Ankara","İstanbul","İzmir"]

iteratorum = iter(sehirler)

print(next(iteratorum)) # Ankara
print(next(iteratorum)) # İstanbul
print(next(iteratorum)) # İzmir
# print(next(iteratorum)) # Hata verir,liste bitti.

for sehir in sehirler:
    print(sehir)

# çok kullanılmaz!!!!