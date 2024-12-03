def conta_parole_righe_caratteri(file_path):
    try:
        with open(file_path, 'r') as file:
            testo = file.read()
            
            # Conta il numero di righe
            righe = testo.splitlines()
            numero_righe = len(righe)
            
            # Conta il numero di parole
            parole = testo.split()
            numero_parole = len(parole)
            
            # Conta il numero di caratteri
            numero_caratteri = len(testo)
            
            return numero_righe, numero_parole, numero_caratteri
    except FileNotFoundError:
        print(f"Errore: Il file '{file_path}' non è stato trovato.")
        return None

# Esempio di utilizzo
file_path = 'loremipsum.txt'
risultati = conta_parole_righe_caratteri(file_path)

if risultati:
    numero_righe, numero_parole, numero_caratteri = risultati
    print(f"Numero di righe: {numero_righe}")
    print(f"Numero di parole: {numero_parole}")
    print(f"Numero di caratteri: {numero_caratteri}")
