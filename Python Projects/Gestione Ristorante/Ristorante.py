# Crea una classe ristorante con una lista di liste chiamata menu e una 
# lista chiamata ordinazione, 
# Nel menu ci devono essere X piatti composti ogniuno da una lista propria di ingredienti, 
# e la lista ordinazione invece e composta dalle singole ordinazioni del cleinte, 
# Servirà quindi una classe cliente 
# e ogni membro della cucina potrà servire solo un tipo di piatto

# EXTRA: aggiungi personale, budget e costi, Feedback piatti e chef

from PersonaleCucina import Chef, SousChef, CuocoLinea

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Ristorante:
    def __init__(self):
        self.menu = []
        self.ordinazione = []
        self.personale = []
        self.budget = 0
        self.costi = 0
        self.feedback_piatti = {}
        self.feedback_chef = {}

    def aggiungi_piatto(self, nome_piatto, ingredienti, costo):
        self.menu.append([nome_piatto, ingredienti, costo])

    def mostra_menu(self):
        print("Menu del Ristorante:")
        for piatto in self.menu:
            print(f"{piatto[0]}: {', '.join(piatto[1])} - Costo: {piatto[2]}€")

    def prendi_ordinazione(self, cliente, nome_piatto):
        for piatto in self.menu:
            if piatto[0] == nome_piatto:
                for membro in self.personale:
                    if membro.tipo_piatto == nome_piatto:
                        self.ordinazione.append((cliente, nome_piatto))
                        self.costi += piatto[2]
                        print(f"Ordinazione aggiunta: {cliente.nome} ha ordinato {nome_piatto}")
                        return
                print(f"Nessun membro della cucina può servire il piatto: {nome_piatto}")
                return
        print(f"Piatto {nome_piatto} non trovato nel menu.")

    def mostra_ordinazioni(self):
        print("Ordinazioni attuali:")
        for ordine in self.ordinazione:
            print(f"{ordine[0].nome} ha ordinato {ordine[1]}")

    def aggiungi_personale(self, membro):
        self.personale.append(membro)

    def aggiorna_budget(self, importo):
        self.budget += importo
        print(f"Budget aggiornato: {self.budget}€")

    def lascia_feedback_piatto(self, nome_piatto, feedback):
        if nome_piatto in self.feedback_piatti:
            self.feedback_piatti[nome_piatto].append(feedback)
        else:
            self.feedback_piatti[nome_piatto] = [feedback]
        print(f"Feedback per {nome_piatto} aggiunto.")

    def lascia_feedback_chef(self, nome_chef, feedback):
        if nome_chef in self.feedback_chef:
            self.feedback_chef[nome_chef].append(feedback)
        else:
            self.feedback_chef[nome_chef] = [feedback]
        print(f"Feedback per {nome_chef} aggiunto.")

    def mostra_feedback(self):
        print("Feedback sui piatti:")
        for piatto, feedbacks in self.feedback_piatti.items():
            print(f"{piatto}: {', '.join(feedbacks)}")

        print("\nFeedback sugli chef:")
        for chef, feedbacks in self.feedback_chef.items():
            print(f"{chef}: {', '.join(feedbacks)}")

def main():
    ristorante = Ristorante()

    # Aggiungi personale al ristorante
    while True:
        tipo_personale = input("Inserisci il tipo di personale (Chef/SousChef/CuocoLinea) o premi INVIO per terminare: ")
        if tipo_personale == "":
            break

        nome = input("Inserisci il nome del personale: ")
        eta = int(input("Inserisci l'età del personale: "))
        tipo_piatto = input("Inserisci il tipo di piatto che può cucinare: ")

        if tipo_personale.lower() == "chef":
            specialita = input("Inserisci la specialità dello chef: ")
            membro = Chef(nome, eta, specialita, tipo_piatto)
        elif tipo_personale.lower() == "souschef":
            membro = SousChef(nome, eta, tipo_piatto)
        elif tipo_personale.lower() == "cuocolinea":
            membro = CuocoLinea(nome, eta, tipo_piatto)
        else:
            print("Tipo di personale non valido.")
            continue

        ristorante.aggiungi_personale(membro)

    # Aggiungi piatti al menu
    while True:
        nome_piatto = input("Inserisci il nome del piatto o premi INVIO per terminare: ")
        if nome_piatto == "":
            break

        ingredienti = input("Inserisci gli ingredienti del piatto (separati da virgola): ").split(", ")
        costo = float(input("Inserisci il costo del piatto: "))
        ristorante.aggiungi_piatto(nome_piatto, ingredienti, costo)

    # Mostra il menu
    ristorante.mostra_menu()

    # Crea clienti e prendi ordinazioni
    while True:
        nome_cliente = input("Inserisci il nome del cliente o premi INVIO per terminare: ")
        if nome_cliente == "":
            break

        cliente = Cliente(nome_cliente)
        nome_piatto = input("Inserisci il nome del piatto da ordinare: ")
        ristorante.prendi_ordinazione(cliente, nome_piatto)

    # Mostra ordinazioni
    ristorante.mostra_ordinazioni()

    # Aggiorna budget
    importo = float(input("Inserisci l'importo da aggiungere al budget: "))
    ristorante.aggiorna_budget(importo)

    # Lascia feedback
    while True:
        tipo_feedback = input("Vuoi lasciare un feedback per un piatto o uno chef? (piatto/chef) o premi INVIO per terminare: ")
        if tipo_feedback == "":
            break

        if tipo_feedback.lower() == "piatto":
            nome_piatto = input("Inserisci il nome del piatto: ")
            feedback = input("Inserisci il feedback: ")
            ristorante.lascia_feedback_piatto(nome_piatto, feedback)
        elif tipo_feedback.lower() == "chef":
            nome_chef = input("Inserisci il nome dello chef: ")
            feedback = input("Inserisci il feedback: ")
            ristorante.lascia_feedback_chef(nome_chef, feedback)
        else:
            print("Tipo di feedback non valido.")

    # Mostra feedback
    ristorante.mostra_feedback()

# Avvia il programma
if __name__ == "__main__":
    main()
