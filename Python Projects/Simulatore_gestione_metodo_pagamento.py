class MetodoPagamento:
    def effettua_pagamento(self, importo):
       pass

class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Carta di Credito.")

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con PayPal.")

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Bonifico Bancario.")

class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento

    def paga(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)

def main():
    importo = float(input("Inserisci l'importo da pagare: "))

    metodo = input("Scegli il metodo di pagamento (carta, paypal, bonifico): ").lower()
    
    if metodo == "carta":
        metodo_pagamento = CartaDiCredito()
    elif metodo == "paypal":
        metodo_pagamento = PayPal()
    elif metodo == "bonifico":
        metodo_pagamento = BonificoBancario()
    else:
        print("Metodo di pagamento non valido.")
        return

    gestore = GestorePagamenti(metodo_pagamento)
    gestore.paga(importo)

# Avvia il programma
main()
