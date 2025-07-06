print("Data Structures")
print("Add & Sort List:")

#Lists
x = [1,"Kirali",5.02,True]
y = [1,2,3,4,5]

# Modify x
w = list(x)
w.append("Iruni")
w.insert(5,9.29)

#Modify y
z = list(y)
z.insert(3,16)

#Sort z
s = list(z)
s.sort()

#Delete Something
t = list(s)
t.remove(3)

r = list(t)
r.pop(0)

#output Lists
print(x)
print(w)
print(y)
print(z)
print(s)
print(t)
print(r)
