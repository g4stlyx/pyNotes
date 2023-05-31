

cities = ["Ankara","İstanbul","İzmir"]

#%% For intro 1
for city in cities:                      
    if city == "İstanbul":
        break # Şehir İst. olunca döngüyü kırar.
    print("the code for the chosen city =" + city[0:3])
    print("******************")
    

#%% For intro 2
for city in cities:                      
    if city == "İstanbul":
        continue # Şehir İst. olunca bir sonraki şehire geçer.
    print("the code for the chosen city =" + city[0:3])
    print("******************")


#%% For range 1
for x in range(1,11):
    print(x)

#%% For range 2
for x in range(100):
    print(x + 1)

#%% For range 3
for x in range(2,100,2):
    print(x)

 