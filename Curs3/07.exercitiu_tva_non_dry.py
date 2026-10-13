
valoare_fara_tva = input("Introduceti valoarea apartamentului \n ")
valoare_fara_tva = int(valoare_fara_tva)

# Write Everything Twice

if valoare_fara_tva < 140_000:
    procent = 5
    tva = procent * valoare_fara_tva / 100
    valoarea_cu_tva = valoare_fara_tva + tva
    print("Valoarea cu TVA este:", valoarea_cu_tva)
else: # mai mare sau egal
    procent = 20
    tva = procent * valoare_fara_tva / 100
    valoarea_cu_tva = valoare_fara_tva + tva
    print("Valoarea cu TVA este:", valoarea_cu_tva)

