
while True:
    luna = input("Introduceti luna \n")

    while not luna.isnumeric() or int(luna) <= 0 or int(luna) > 12:
        luna = input("Luna incorecta: Trebuie sa fie valoare numerică și intervalul 1..12. Reintroduceti luna \n")

    luna = int(luna)

    if luna in (1, 2, 12):
        print("Iarna")
    elif luna in (3, 4, 5):
        print("Primavara")
    elif luna in (6, 7, 8):
        print("Vara")
    elif luna in (9, 10, 11):
        print("Toamna")
    
