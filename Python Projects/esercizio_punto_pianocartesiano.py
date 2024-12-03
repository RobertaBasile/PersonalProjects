# Crea una classe chiamata Punto. Questa classe dovrebbe avere:

# Due attributi: x e y, per rappresentare le coordinate del punto nel piano.

# Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le
# coordinate del punto di questi valori.

# Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del
# piano.
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)

def main():
    punti = []
    x = input("Inserisci la coordinata x (o premi INVIO per terminare): ")
    y = input("Inserisci la coordinata y: ")
    while True:
        
        punto = Punto(float(x), float(y))
        punti.append(punto)
    
        for i, punto in enumerate(punti):
            print(f"Punto {i+1}: ({punto.x}, {punto.y})")
            distanza = punto.distanza_da_origine()
            print(f"Distanza dall'origine: {distanza}")

        dx = float(input("Inserisci il valore per dx: "))
        dy = float(input("Inserisci il valore per dy: "))
        
        for punto in punti:
            punto.muovi(dx, dy)
            print(f"Coordinate dopo lo spostamento: ({punto.x}, {punto.y})")
        ripetere = input("Vuoi riprovare a spostare i punti o vuoi terminare? (riprovare/terminare): ").strip().lower() 
        if ripetere == 'no': 
            break

# Avvia il programma
main()

