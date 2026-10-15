
luna = input("Introduceti luna \n")

while not luna.isnumeric():
    luna = input("Luna incorecta. Reintroduceti luna \n")

luna = int(luna)

if luna <= 0:
    print("Luna incorecta")
elif luna > 12:
    print("Luna incorecta")
elif luna < 3:
    print("Iarna")
elif luna < 6:
    print("Primavara")
elif luna < 9:
    print("Vara")
elif luna < 12:
    print("Toamna")
elif luna == 12:
    print("Iarna")
