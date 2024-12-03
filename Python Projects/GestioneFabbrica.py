# In questo aggiornamento del codice, é stato introdotto il concetto di polimorfismo per gestire 
# in modo flessibile i prodotti di tipo Elettronica e Abbigliamento. 
# é stato aggiunto un metodo descrivi alla classe base Prodotto, 
# che fornisce una descrizione generica del prodotto. 
# Questo metodo è stato poi sovrascritto nelle classi derivate Elettronica e Abbigliamento 
# per includere informazioni specifiche come la garanzia per i prodotti elettronici e il materiale 
# per i prodotti di abbigliamento.

# Inoltre, é stata aggiornata la classe Fabbrica per includere un nuovo metodo descrivi_prodotti, 
# che utilizza il metodo descrivi in modo polimorfico per descrivere tutti i prodotti presenti 
# nell'inventario. 
# Questo permette di ottenere descrizioni dettagliate e specifiche per ciascun tipo di prodotto, 
# migliorando la gestione e la visualizzazione delle informazioni relative ai prodotti.

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto

    def descrivi(self):
        return f"Prodotto: {self.nome}, Costo di Produzione: {self.costo_produzione}€, Prezzo di Vendita: {self.prezzo_vendita}€"

class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia

    def descrivi(self):
        return f"Elettronica: {self.nome}, Costo di Produzione: {self.costo_produzione}€, Prezzo di Vendita: {self.prezzo_vendita}€, Garanzia: {self.garanzia} anni"

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

    def descrivi(self):
        return f"Abbigliamento: {self.nome}, Costo di Produzione: {self.costo_produzione}€, Prezzo di Vendita: {self.prezzo_vendita}€, Materiale: {self.materiale}"

class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita
        print(f"Aggiunti {quantita} {prodotto.nome} all'inventario.")

    def stampa_inventario(self):
        if self.inventario:
            print("Inventario della fabbrica:")
            for nome, quantita in self.inventario.items():
                print(f"{nome}: {quantita}")
        else:
            print("L'inventario è vuoto.")

    def descrivi_prodotti(self):
        if self.inventario:
            print("Descrizione dei prodotti in inventario:")
            for nome, quantita in self.inventario.items():
                print(f"{nome} (Quantità: {quantita})")
                for _ in range(quantita):
                    print(self.inventario[nome].descrivi())
        else:
            print("L'inventario è vuoto.")

def main():
    nome = input("Inserisci il nome del prodotto: ")
    prezzo_vendita = float(input("Inserisci il prezzo di vendita: "))
    costo_produzione = float(input("Inserisci il costo di produzione: "))
    tipo = input("Inserisci il tipo di prodotto (Elettronica/Abbigliamento): ")

    if tipo.lower() == "elettronica":
        garanzia = int(input("Inserisci la durata in anni della garanzia: "))
        prodotto = Elettronica(nome, costo_produzione, prezzo_vendita, garanzia)
    elif tipo.lower() == "abbigliamento":
        materiale = input("Inserisci il materiale: ")
        prodotto = Abbigliamento(nome, costo_produzione, prezzo_vendita, materiale)
    else:
        print("Tipo di prodotto non valido.")
        return

    risultato = prodotto.calcola_profitto()
    print(f"Il profitto per il prodotto {nome} è: {risultato}")

    fabbrica = Fabbrica()
    quantita = int(input("Inserisci la quantità del prodotto da aggiungere all'inventario: "))
    fabbrica.aggiungi_prodotto(prodotto, quantita)
    fabbrica.stampa_inventario()
    fabbrica.descrivi_prodotti()

# Avvia il programma
main()
