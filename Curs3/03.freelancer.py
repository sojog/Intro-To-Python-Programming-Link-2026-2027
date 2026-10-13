
suma_totala = input("Introdu suma totala pe care o factureaza freelancer-ul\n")
suma_totala = int(suma_totala)

nr_saptamani = input("Introdu numărul de săptămâni pe care îl lucrează freelancer-ul\n")
nr_saptamani = int(nr_saptamani)

rata_per_saptamana = suma_totala / nr_saptamani
rata_per_zi = rata_per_saptamana / 5
rata_per_ora = rata_per_zi / 8

print(f"Rata per sapt: { rata_per_saptamana:.2f} \nRata per zi: {rata_per_zi:.1f} \nRata per ora: {rata_per_ora:.3f}")