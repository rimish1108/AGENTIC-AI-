a = [1, 2, 3]

b = a
c = a[:]

a.append([4, 5])
c.extend([6, 7])

print("a =", a)
print("b =", b)
print("c =", c)

print(id(a), id(b), id(c))