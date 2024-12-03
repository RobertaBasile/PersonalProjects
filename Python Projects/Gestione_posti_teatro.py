# creare una classe base Posto che rappresenta un singolo posto nel teatro. Da questa, deriveranno
# diverse classi per tipi specifici di posti, come PostoVIP e PostoStandard. Sarà inoltre
# necessaria una classe Teatro per gestire tutti i posti e le prenotazioni.



# Classe Posto:
# Attributi privati:
# _numero (intero: numero del posto)
# _fila (stringa: fila in cui si trova il posto)
# _occupato (booleano: stato del posto, se è occupato o meno)
# Metodi:
# prenota(): prenota il posto se non è già occupato.
# libera(): libera il posto se è occupato.
# Getter per numero e fila, e uno stato che indica se il posto è occupato.
# Classi Derivate:
# PostoVIP:
# Aggiunge un attributo per servizi_extra (e.g., accesso al lounge, servizio in posto).
# Sovrascrive il metodo prenota() per includere la gestione dei servizi extra.
# PostoStandard:
# Potrebbe avere un costo aggiuntivo per la prenotazione online o altri servizi meno
# esclusivi.
# Classe Teatro:
# Attributi:
# _posti: lista di tutti i posti nel teatro.
# Metodi:
# prenota_posto(numero, fila): trova e prenota un posto specifico.
# stampa_posti_occupati(): mostra tutti i posti occupati.

class Posto:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato.")
        else:
            print(f"Posto {self._fila}{self._numero} è già occupato.")

    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} liberato.")
        else:
            print(f"Posto {self._fila}{self._numero} è già libero.")
            
           # @property - Viene usato per indicare che stiamo per definire una proprietà. 

    @property
    def numero(self):
        return self._numero

    @property
    def fila(self):
        return self._fila

    @property
    def occupato(self):
        return self._occupato

class PostoVIP(Posto):
#     super(): Questa funzione è usata per richiamare il costruttore della
# superclasse, permettendo alla sottoclasse di estendere o modificare il
# comportamento della superclasse. super() è usata anche per accedere a metodi
# della superclasse che sono stati sovrascritti nella sottoclasse.

    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto VIP {self._fila}{self._numero} prenotato con servizi extra: {self.servizi_extra}.")
        else:
            print(f"Posto VIP {self._fila}{self._numero} è già occupato.")

class PostoStandard(Posto):
    def __init__(self, numero, fila, costo_aggiuntivo):
        super().__init__(numero, fila)
        self.costo_aggiuntivo = costo_aggiuntivo
        

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto Standard {self._fila}{self._numero} prenotato con costo aggiuntivo: {self.costo_aggiuntivo}€.")
        else:
            print(f"Posto Standard {self._fila}{self._numero} è già occupato.")

class Teatro:
    def __init__(self):
        self._posti = []
        
    def aggiungi_posto(self, posto):
        self._posti.append(posto)

    def prenota_posto(self, numero, fila):
        for posto in self._posti:
            if posto.numero == numero and posto.fila == fila:
                posto.prenota()
                return
        print(f"Posto {fila}{numero} non trovato.")

    def stampa_posti_occupati(self):
        print("Posti occupati:")
        for posto in self._posti:
            if posto.occupato:
                print(f"Posto {posto.fila}{posto.numero}")

def main():
    teatro = Teatro()

    while True:
        tipo = input("Inserisci il tipo di posto (VIP/Standard) o premi INVIO per terminare: ")
        if tipo == "":
            break

        numero = int(input("Inserisci il numero del posto: "))
        fila = input("Inserisci la fila del posto: ")

        if tipo.lower() == "vip":
            servizi_extra = input("Inserisci i servizi extra: ")
            posto = PostoVIP(numero, fila, servizi_extra)
        elif tipo.lower() == "standard":
            costo_aggiuntivo = float(input("Inserisci il costo aggiuntivo: "))
            posto = PostoStandard(numero, fila, costo_aggiuntivo)
        else:
            print("Tipo di posto non valido.")
            continue

        teatro.aggiungi_posto(posto)
        
        teatro.prenota_posto(int(numero), fila)
       
        teatro.stampa_posti_occupati()

        continuare = input("Vuoi prenotare un altro posto? (s/n): ") 
        if continuare.lower() != 's': 
            break
# Avvia il programma

main()
