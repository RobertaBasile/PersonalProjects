# Crea una classe biblioteca che permetta di creare un libro e stamparlo 
# Extra: permetti di creare quanti libri vuole l’utente
class Libro:
    def __init__(self, titolo, autore, anno,genere):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere 

    # Il metodo __str__ restituisce una stringa formattata con il titolo, l'autore e l'anno del libro.
    # Questo metodo viene chiamato automaticamente quando si utilizza la funzione print() sull'oggetto Libro.

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Genere: {self.genere}"

class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def stampa_libri(self):
        for libro in self.libri:
            print(libro)

def main():
    biblioteca = Biblioteca()

    numero_libri = input("Quanti libri vuoi inserire? (premi SPAZIO e INVIO per inserire direttamente, se non vuoi scegliere quanti libri inserire): ")
    if numero_libri == "":
        while True:
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            anno = input("Inserisci l'anno di pubblicazione del libro: ")
            genere = input("Inserisci il genere di pubblicazione del libro: ")

            libro = Libro(titolo, autore, anno)
            biblioteca.aggiungi_libro(libro)

            ripetere = input("Vuoi aggiungere un altro libro? (sì/no): ").lower()
            if ripetere != 'sì':
                break
    else:
        numero_libri = int(numero_libri)
        for i in range(numero_libri):
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            anno = input("Inserisci l'anno di pubblicazione del libro: ")
            genere = input("Inserisci il genere di pubblicazione del libro: ")

            libro = Libro(titolo, autore, anno, genere)
            biblioteca.aggiungi_libro(libro)

    print("\nLibri nella biblioteca:")
    biblioteca.stampa_libri()

# Avvia il programma
main()
