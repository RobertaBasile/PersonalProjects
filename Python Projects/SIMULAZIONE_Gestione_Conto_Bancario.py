# creare una classe ContoBancario che incapsula le informazioni di un conto e
# fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare
# l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al
# saldo del conto.

# Classe ContoBancario:
# Attributi privati:
# __titolare (stringa che rappresenta il nome del titolare del conto)
# __saldo (decimale che rappresenta il saldo del conto)
# Metodi pubblici:
# deposita(importo): aggiunge un importo al saldo solo se l'importo è
# positivo.
# preleva(importo): sottrae un importo dal saldo solo se ci sono fondi
# sufficienti e l'importo è positivo.
# visualizza_saldo(): restituisce il saldo corrente senza permettere la sua
# modifica diretta.
# Gestione dei Metodi e Sicurezza:
# I metodi deposita e preleva devono controllare che gli importi siano validi
# (e.g., non negativi).
# Aggiungere metodi "getter" e "setter" per gli attributi come _titolare,
# applicando validazioni appropriate (e.g., il titolare deve essere una stringa
# non vuota).

class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):
        self.__titolare = titolare
        self.__saldo = saldo_iniziale

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo}€ effettuato. Nuovo saldo: {self.__saldo}€.")
        else:
            print("L'importo del deposito deve essere positivo.")

    def preleva(self, importo):
        if importo > 0:
            if self.__saldo >= importo:
                self.__saldo -= importo
                print(f"Prelievo di {importo}€ effettuato. Nuovo saldo: {self.__saldo}€.")
            else:
                print("Fondi insufficienti per il prelievo.")
        else:
            print("L'importo del prelievo deve essere positivo.")

    def visualizza_saldo(self):
        return self.__saldo

    # Getter e Setter per il titolare
    # @property trasforma il metodo titolare in un getter per l'attributo privato __titolare.
    # @titolare.setter: Trasforma un metodo in un setter per un attributo
    # La funzione Python isinstance() restituisce True se l'oggetto 
    # è del tipo specificato, e se non corrisponde restituisce False
    @property
    def titolare(self):
        return self.__titolare

    @titolare.setter
    def titolare(self, nuovo_titolare):
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip():
            self.__titolare = nuovo_titolare
        else:
            print("Il nome del titolare deve essere una stringa non vuota.")

def main():
    titolare = input("Inserisci il nome del titolare del conto: ")
    saldo_iniziale = float(input("Inserisci il saldo iniziale del conto: "))
    conto = ContoBancario(titolare, saldo_iniziale)

    while True:
        print("\n1. Deposita")
        print("2. Preleva")
        print("3. Visualizza saldo")
        print("4. Esci")
        scelta = input("Scegli un'opzione: ").strip()

        if scelta == '1':
            importo = float(input("Inserisci l'importo da depositare: "))
            conto.deposita(importo)
        elif scelta == '2':
            importo = float(input("Inserisci l'importo da prelevare: "))
            conto.preleva(importo)
        elif scelta == '3':
            saldo = conto.visualizza_saldo()
            print(f"Saldo corrente: {saldo}€")
        elif scelta == '4':
            break
        else:
            print("Opzione non valida. Riprova.")

# Avvia il programma
main()
