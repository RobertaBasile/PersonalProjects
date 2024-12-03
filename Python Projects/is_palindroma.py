def is_palindrome(stringa):
    # Rimuove gli spazi e converte la stringa in minuscolo
    stringa = stringa.replace(" ", "").lower()
    # Confronta la stringa con la sua versione invertita
    return stringa == stringa[::-1]

def main():
    ripetere = "sì"
    while ripetere == "sì":
        # Chiedi all'utente di inserire una parola
        stringa = input("Inserisci una parola: ")

        # Verifica se la parola è palindroma
        if is_palindrome(stringa):
            print("La parola è palindroma.")
        else:
            print("La parola non è palindroma.")

        # Chiedi all'utente se vuole riprovare con un'altra parola o uscire dal gioco
        ripetere = input("Vuoi riprovare con un'altra parola o vuoi uscire dal gioco? (riprovare/uscire): ").strip().lower()
        if ripetere == 'uscire':
            break

# Avvia il programma
main()
