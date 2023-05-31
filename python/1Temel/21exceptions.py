# hata ayıklama

try: # hatasızsa bu çalışır
    sayi = int(input("Sayı giriniz"))
except ValueError: 
    print("Tip uyuşmazlığı: Lütfen sayı giriniz.")
except ZeroDivisionError: 
    print("Payda sıfır olamaz.")
except: # yukarıdakiler harici error verirse bu çalışır
    print("Bir hata oluştu")

print("Bitti")

