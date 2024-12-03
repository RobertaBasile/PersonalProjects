# 5 numeri casuali e li salva all'interno di un file
#      il programma legge il file e l'utente deve indovinare almeno 2 numeri

import random

# Genera 5 numeri casuali e salva in un file
def genera_numeri_casuali():
    numeri_casuali = [random.randint(1, 100) for _ in range(5)]
    with open("numeri_casuali.txt", "w") as file:
        for numero in numeri_casuali:
            file.write(f"{numero}\n")
    print("Numeri casuali generati e salvati in 'numeri_casuali.txt'")

# Legge i numeri dal file
def leggi_numeri_da_file():
    numeri = []
    with open("numeri_casuali.txt", "r") as file:
        for riga in file:
            numeri.append(int(riga.strip()))
    return numeri

# Permette all'utente di indovinare i numeri
def indovina_numeri(numeri_casuali):
    tentativi = 5
    indovinati = 0
    print("Indovina i numeri (hai 5 tentativi):")
    for _ in range(tentativi):
        numero = int(input("Inserisci un numero: "))
        if numero in numeri_casuali:
            indovinati += 1
            print("Hai indovinato!")
        else:
            print("Numero sbagliato.")
    return indovinati

def main():
    genera_numeri_casuali()
    numeri_casuali = leggi_numeri_da_file()
    indovinati = indovina_numeri(numeri_casuali)
    if indovinati == 0:
        print("non hai indovinato nessun numero")
    elif indovinati >= 2:
        print(f"Hai indovinato {indovinati} numeri! Complimenti!")
    else:
        print(f"Hai indovinato solo {indovinati} numeri. Riprova!")

# Avvia il programma

    main()
