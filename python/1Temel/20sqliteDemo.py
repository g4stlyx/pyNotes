# -*- coding: utf-8 -*-

import sqlite3
  
connection = sqlite3.connect("chinook.db")

# cursor = connection.execute("""
#                             select city,count(*) 
#                             from Customers group by city
#                             having count(*)>1
#                             order by count(*) desc
#                             """)

# for row in cursor:
#     print("City = " + str(row[0]))
#     print("Count = " + str(row[1]))
#     print("*************")

#Müşterilerin şehirlerini ve o şehirlerden kaç adet olduğunu çıkartır
#Sayıya göre büyükten küçüğe, 1'den büyükleri sıralar

# **********************************************************

# cursor = connection.execute("""
#                             select FirstName,LastName 
#                             from customers 
#                             where city='Prague' or city='Berlin'
#                             order by FirstName,LastName desc
#                             """)

# for row in cursor:
#     print("First Name = " + row[0])
#     print("Last Name = " + row[1])
#     print("*************")
    
# Müşterilerden Prag ve Berlinlilerin isim soyisimlerini çıkartır
# Firstname'e göre alfabetik olarak ters bir şekilde sırala
# row = satır ; cursor = gösterge,imleç

# **********************************************************

# cursor = connection.execute("""
#                             select FirstName,LastName 
#                             from customers 
#                             where FirstName like 'alex%'
#                             """)

# for row in cursor:
#     print("First Name = " + row[0])
#     print("Last Name = " + row[1])
#     print("*************")
    
# Müşterilerden ismi alex ile başlayanları gösterir.

# **********************************************************


def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       insert into customers 
                       (firstName,lastName,city,email)
                       values('Sefa','Ağardan','İstanbul',
                       'agardan.sefa@gmail.com')
                       """)
    connection.commit()
    connection.close()

#insertCustomer()

# ************************************************************

def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       update customers set city='Ankara'
                       where city='İstanbul'
                       """)
    connection.commit()
    connection.close()

#updateCustomer()

# *************************************************************

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       delete from customers where 
                       customerid=63
                       """)
    connection.commit()
    connection.close()
    
#deleteCustomer()



def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute("""
                                select albums.Title, artists.Name 
                                from artists inner join albums
                                on artists.ArtistId = albums.ArtistId
                                """)
    
    for row in cursor:
        print("Title = " + row[0] + " -- " + "Name =  " + row[1])
        

joinOperasyonlari()





