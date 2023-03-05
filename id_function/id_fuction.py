a = 10
b = 10
c = 10

print(a)
print(b)
print(c)

print(id(a))
print(id(b))
print(id(c))

a = 20
print()
print(id(a))
print(id(b))
print(id(c))
print()

x = y = z = [1,2,3]

x.append(4)
print(x)
print(id(x))
print(id(y))
print(id(z))

print()
n = 10
m = 10
print(id(n))
print(id(m))

s = "abcd"
s2 = "abcde"
print(s2[:4])

print(s is s2[:4])
print(s == s2[:4])
