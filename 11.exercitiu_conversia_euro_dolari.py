eur = 5.34
usd = 4.78

suma_in_lei = input("Introdu valoare in lei: \n")
suma_in_lei = float(suma_in_lei)

suma_in_euro = round(suma_in_lei / eur)
suma_in_usd  = round(suma_in_lei / usd)

print("Suma in euro:", suma_in_euro)
print("Suma in usd:", suma_in_usd)