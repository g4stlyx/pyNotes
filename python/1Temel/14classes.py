# fonksiyonları sınıflandırır

#%% basics
class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2
    
matematik = Matematik() # instance - örnek

print("Toplam = " + str(matematik.topla(2,78)))

#%% property,özellik

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Sefa","Ağardan","18")

print(person1.age)
print(person1.firstName)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self,ccNumber):
        self.ccNumber = ccNumber
        
ahmet = Worker(3000)
ahmet.age = 15

mehmet = Customer(111111111111)

print(ahmet.age)

