# setleri birleştirir, set union

setA = {1,2,3,4,5}
setB = {1,3,5,6,7,8}

print(setA | setB) # alt gr + < işareti = |

print(setA.union(setB))

# set kesişimini verir, set intersection

print(setA & setB)
print(setA.intersection(setB))

# set farklılıklarını verir, set difference A/B A-B B/A B-A

print(setA - setB)
print(setA.difference(setB))

print(setB - setA)
print(setB.difference(setA))

# a-b U b-a, set symetric difference

print(setA ^ setB)
print(setA.symmetric_difference(setB))
