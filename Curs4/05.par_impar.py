
print(10 % 2)
print(11 % 2)


nr = int(input("Introduceti un numar\n"))

# Un IF clasic
if nr % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")

# Operator terner
print("Numarul este par") if nr % 2 == 0 else print("Numarul este impar")
print("Numarul este impar") if nr % 2 != 0 else print("Numarul este par")

print( "Numarul este impar"  if nr % 2 != 0 else "Numarul este par" )


print(f"Numarul este {"" if nr % 2 == 0 else "im"}par")


while True:
    nr = int(input("Introduceti un numar\n"))
    if nr % 2 == 0:
        print("Numarul este par")
    else:
        print("Numarul este impar")
