
raza = input("Introdu raza cercului \n")
raza = float(raza)

PI = 3.14

if raza >=0:
    aria = PI * raza ** 2
    print("Aria cercului", aria)
    print(f"Aria cercului {aria}" )
else:
    print("Raza nu poate fi mai mica de 0")