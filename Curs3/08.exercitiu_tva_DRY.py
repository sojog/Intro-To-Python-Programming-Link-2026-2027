
valoare_fara_tva = input("Introduceti valoarea apartamentului \n ")
valoare_fara_tva = int(valoare_fara_tva)

# DON'T Repeate Yourself
if valoare_fara_tva < 140_000:
    procent = 5
else: # mai mare sau egal
    procent = 20

tva = procent * valoare_fara_tva / 100
valoarea_cu_tva = valoare_fara_tva + tva
print("Valoarea cu TVA este:", valoarea_cu_tva)