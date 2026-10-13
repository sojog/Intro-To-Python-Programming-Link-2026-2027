# Conversia intre int si float se face foarte usor
x = 10
print(x, type(x))

y = float(x)
print(y, type(y))

y = 78.59
print(y, type(y))

z = int(y)
print(z, type(z))


# Conversia catre string este foarte usoara
m = 100
n = str(m)
print(n, type(n))

m = 100.0
n = str(m)
print(n, type(n))

m = True
n = str(m)
print(n, type(n))

# Conversie de la string catre int, float, bool
p = "100"
q = int(p)
print(q, type(q))

# Conversia de la string la int nu va merge daca valorile nu sunt numerice
# p = "QWERTY"
# q = int(p)
# print(q, type(q))


# De tinut minte
# p = "True"
# q = int(p)
# print(q, type(q))

# p = "100.0"
# q = int(p)
# print(q, type(q))


p = "100.0"
q = float(p)
print(q, type(q))

p = "100.0"
q = int(float(p))
print(q, type(q))


p = "True"
q = int(bool(p))
print(q, type(q))