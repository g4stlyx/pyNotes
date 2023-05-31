# -*- coding: utf-8 -*-

#substring, parçalama

message = "Hello World"
print(message[2]) # 3. harfi gösterir, 0'dan başlıyor
print(message[2:5]) # 2'den 5'e kadar gösterir, 5 dahil değil

newMessage = message[2:] # 2'den sonrası full
print(newMessage)

newMessage2 = message[:2] # baştan 2'ye kadar
print(newMessage2)

# len function --------------------------------------


print(len(message)) # metnin kaç harfli olduğunu veriyor

newMessage3 = message[len(message) -1:len(message)] # son harfi gösterir
# bir üstteki yerine kaç harfli olduğunu öğrenip 10:11 yapılabilir
print(newMessage3)

# lower and upper functions --------------------------------------

print(message.upper()) # full büyük harf yazar
print(message.lower()) # full küçük harf yazar

# replace function --------------------------------------

print(message.replace("ü","u")) # ü'yü u ile değiştirip yazdırır

# split strip functions --------------------------------------

bilgi = "Sefa Ağardan 18 İstanbul ".strip()
print(bilgi.split(" ")) # kelime kelime ayırır
# default olarak boşluk görürse ayırır, baştaki ve sondaki boşlukları yok sayar
# strip baştaki ve sondaki boşlukları atar
# splitin parantezine ne konulduğunda ayırması gerektiğini yazabilirsin; for ex ";"

print(bilgi.split()[2]) # ayırıp 2. elemanı verir

# input function --------------------------------------

ad = input("Adınız?") # kullanıcıdan bilgi alma
sayi1 = input("Sayi1?")
sayi2 = input("Sayi2?")

print(int(sayi1) + int(sayi2))

#









































