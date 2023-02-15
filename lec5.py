import this

#whitespace is ignored inside () and [] 

print(1+2+
3232)

a = [1, 2, 3]
b = [1,2,3,]
#objects do not have the same ID
#show id
print(id(a))
print(id(b))
print(id([1, 2, 3]))
#refering to value
print(a==b)
#check if id is the same or not
print(a is b)
c=1
d=1
print(c is d)
#only none can be none
x = None

print(id(x))
print(id(None))

print(x is None)
print(x == None)

y = ""
print(y is None)

print(True and False)