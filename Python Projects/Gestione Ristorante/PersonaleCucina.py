# creare una classe base PersonaleCucina e diverse classi derivate che rappresentano differenti ruoli all'interno della cucina di un ristorante. L'obiettivo è di utilizzare l'ereditarietà per condividere alcune caratteristiche comuni mentre si distinguono le responsabilità e le azioni specifiche di ogni ruolo.

# Classe PersonaleCucina:
# Attributi:
# nome (stringa)
# età (intero)
# Metodi:
# lavora() (metodo generico che può essere sovrascritto per specificare il tipo di lavoro svolto)
# Classi Derivate:
# Chef:
# Attributi aggiuntivi come specialità (tipo di cucina in cui è specializzato)
# Metodi come prepara_menu() che dettaglia come lo chef crea nuovi piatti e menu
# SousChef:
# Metodi come gestisci_inventario() per gestire l'inventario della cucina e assistere lo chef
# CuocoLinea:
# Metodi come cucina_piatto(nome_piatto) che specifica la preparazione di un piatto specifico nella linea di produzione

class PersonaleCucina:
    def __init__(self, nome, eta, tipo_piatto):
        self.__nome = nome
        self.__eta = eta
        self.__tipo_piatto = tipo_piatto

    def lavora(self):
        print(f"{self.__nome} sta lavorando in cucina.")

    # Getter per nome
    @property
    def nome(self):
        return self.__nome

    # Getter per eta
    @property
    def eta(self):
        return self.__eta

    # Getter per tipo_piatto
    @property
    def tipo_piatto(self):
        return self.__tipo_piatto

class Chef(PersonaleCucina):
    def __init__(self, nome, eta, specialita, tipo_piatto):
        super().__init__(nome, eta, tipo_piatto)
        self.__specialita = specialita

    def lavora(self):
        print(f"{self.nome}, lo chef specializzato in {self.__specialita}, sta creando nuovi piatti e menu.")

    def prepara_menu(self):
        print(f"{self.nome} sta preparando un nuovo menu specializzato in {self.__specialita}.")

    # Getter per specialita
    @property
    def specialita(self):
        return self.__specialita

class SousChef(PersonaleCucina):
    def __init__(self, nome, eta, tipo_piatto):
        super().__init__(nome, eta, tipo_piatto)

    def lavora(self):
        print(f"{self.nome}, il sous chef, sta assistendo lo chef e gestendo l'inventario.")

    def gestisci_inventario(self):
        print(f"{self.nome} sta gestendo l'inventario della cucina.")

class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, eta, tipo_piatto):
        super().__init__(nome, eta, tipo_piatto)

    def lavora(self):
        print(f"{self.nome}, il cuoco di linea, sta preparando i piatti.")

    def cucina_piatto(self, nome_piatto):
        print(f"{self.nome} sta cucinando il piatto: {nome_piatto}.")

