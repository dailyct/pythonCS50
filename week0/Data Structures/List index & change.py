print("Data Structures")
print("Index & Change List:")

#Lists
x = [1,"Kirali",5.02,True]
y = [1,2,3,4,5]

#Modify x
w = list(x)
w.append("Iruni")
w.insert(5,9.29)

#Change Something
r = list(w)
r[0] = "Enchan"
r.insert(1,10.01)

#Modify y
z = list(y)
z.insert(3,16)

#Sort z
s = list(z)
s.sort()

#Change Something
t = list(z)
t[0:3] = ["<3", "Alice", 13]

#output Lists
print(x)
print(w)
print(r)
print(y)
print(z)
print(s)
print(t)
