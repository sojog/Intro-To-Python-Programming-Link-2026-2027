
an_nastere = int(input("Introduceti anul nasterii\n"))

AN_CURENT = 2026
LUNA_CURENTA = 10
ZI_CURENTA = 13

MESAJ_ACCES = "Bine ai venit pe site-ul nostru"
MESAJ_KEEP_OUT = "Nu ai varsta legala sa accesezi acest site"

# Refactorizare folosind - if elif
if AN_CURENT - an_nastere < 18:
    print(MESAJ_KEEP_OUT)

elif AN_CURENT - an_nastere > 18:
        print(MESAJ_ACCES)

else:
    luna_nastere = int(input("Introduceti LUNA nasterii\n"))
    if luna_nastere < LUNA_CURENTA:
        print(MESAJ_ACCES)
    elif luna_nastere > LUNA_CURENTA:
        print(MESAJ_KEEP_OUT)
    else:
        zi_nastere = int(input("Introduceti ZIUA nasterii\n"))

        if zi_nastere <= ZI_CURENTA:
            print(MESAJ_ACCES)
        else:
            print(MESAJ_KEEP_OUT)