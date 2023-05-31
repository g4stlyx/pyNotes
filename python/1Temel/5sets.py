# -*- coding: utf-8 -*-

# setler 
# değiştirilmiyor,sıra yok,2 tane aynı eleman yok,çok performanslı

studentsSet = {"Engin","Derin","Salih","Ahmet","Engin"}

for student in studentsSet:
    print(student)


if "Derin" in studentsSet:
    print("Listede var.")
    
studentsSet.add("Ali") # 1 eleman ekle
print(studentsSet)

studentsSet.update(["Mehmet","Merve","Mert"]) # 1+ eleman ekle
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Mert") # Mert'i sil, bulamazsan hata ver
print(len(studentsSet))

studentsSet.discard("Mert") # Mert'i sil bulamazsan hata verme
print(len(studentsSet))

x = studentsSet.pop() # rastgele bir eleman siler
print(studentsSet)

y = studentsSet.clear() # setin içini boşaltır
print(studentsSet)

# del studentsSet # seti siler
# print(studentsSet)


