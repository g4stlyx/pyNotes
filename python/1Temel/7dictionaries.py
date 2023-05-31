sozluk = {
    "book": "kitap",
    "pencil": "kalem",
    }

sozluk2 = dict(kitap="book",masa="table")

sozluk["book"] = "kitap 1"
sozluk["table"] = "masa"

print(sozluk["book"])
print(sozluk)
print(sozluk2)

del(sozluk["book"])
print(sozluk)

print(len(sozluk))














