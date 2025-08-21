#Tuple
t = (1, 'c', "lumbini", 9+7)
print(t)
print(type(t))
l= list(t)
print(l)
print(type(t))

l.append("string")
print(l)
t1=tuple(l)
print(t1)
t2=t1+(5,'ict',"campus")
print(t2)

