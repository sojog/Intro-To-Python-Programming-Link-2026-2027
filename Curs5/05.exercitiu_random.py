import random

# calculatorul genereaza un numar random pana utilizatorul ghiceste
numar_utiliztor = int(input("Introduceti numarul: "))
numar_calculator = random.randint(1, 10)

nr_incercari= 0

# 
while nr_incercari < 3:

    nr_incercari += 1
    if numar_utiliztor == numar_calculator:
        print("Felicitari! Ati ghicit numarul.")
    elif numar_utiliztor < numar_calculator:
        print("Numarul introdus este mai mic decat numarul calculatorului.")
    elif numar_utiliztor > numar_calculator:
    
      print("Numarul introdus este mai mare decat numarul calculatorului.")
    numar_utiliztor = int(input("Introduceti numarul: "))
else:
    print("Numarul introdus nu este valid. Va rugam sa introduceti un numar intre 1 si 10.")
    # numarul de incercarimaxim = 3