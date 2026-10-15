
x = 0

if x :
    print("Adevarat")
else:
    print("Fals")


x = ""

if bool(x):
    print("Adevarat")
else:
    print("Fals")


x = ""

if x:
    print("Adevarat")
else:
    print("Fals")


x = (1, 2, 3)
print(x, type(x))

if x:
    print("Adevarat")
else:
    print("Fals")

x = ()
print(x, type(x))

if x:
    print("Adevarat")
else:
    print("Fals")