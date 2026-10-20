
# Varianta 1
for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        print("BOLTZ", end=" ")
    else:
        print(i, end="  ")

print(" \n\n ")

# Varianta 2
for i in range(1, 101):
    conditie = i % 7 == 0 or "7" in str(i)
    print( "BOLTZ" if conditie  else i, end="  ")
