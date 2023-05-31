x = 10
y = 20

temp = x # solution 1
x = y
y = temp

x,y = y,x # solution 2

print("x =" + str(x))
print("y =" + str(y))