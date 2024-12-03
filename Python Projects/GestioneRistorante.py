class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}

    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} offre cucina {self.tipo_cucina}.")

    def stato_apertura(self):
        if self.aperto:
            print(f"Il ristorante {self.nome} è aperto.")
        else:
            print(f"Il ristorante {self.nome} è chiuso.")

    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante {self.nome} è ora aperto.")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante {self.nome} è ora chiuso.")

    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo
        print(f"Piatto {piatto} aggiunto al menu con prezzo {prezzo}€.")

    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"Piatto {piatto} rimosso dal menu.")
        else:
            print(f"Piatto {piatto} non trovato nel menu.")

    def stampa_menu(self):
        if self.menu:
            print("Menu del ristorante:")
            for piatto, prezzo in self.menu.items():
                print(f"{piatto}: {prezzo}€")
        else:
            print("Il menu è vuoto.")

def main():
    nome = input("Inserisci il nome del ristorante: ")
    tipo_cucina = input("Inserisci il tipo di cucina offerta: ")
    ristorante = Ristorante(nome, tipo_cucina)

    while True:
        print("\n1. Descrivi ristorante")
        print("2. Stato apertura")
        print("3. Apri ristorante")
        print("4. Chiudi ristorante")
        print("5. Aggiungi piatto al menu")
        print("6. Togli piatto dal menu")
        print("7. Stampa menu")
        print("8. Esci")
        scelta = input("Scegli un'opzione: ").strip()

        if scelta == '1':
            ristorante.descrivi_ristorante()
        elif scelta == '2':
            ristorante.stato_apertura()
        elif scelta == '3':
            ristorante.apri_ristorante()
        elif scelta == '4':
            ristorante.chiudi_ristorante()
        elif scelta == '5':
            piatto = input("Inserisci il nome del piatto: ")
            prezzo = float(input("Inserisci il prezzo del piatto: "))
            ristorante.aggiungi_al_menu(piatto, prezzo)
        elif scelta == '6':
            piatto = input("Inserisci il nome del piatto da rimuovere: ")
            ristorante.togli_dal_menu(piatto)
        elif scelta == '7':
            ristorante.stampa_menu()
        elif scelta == '8':
            break
        else:
            print("Opzione non valida. Riprova.")

# Avvia il programma
main()
