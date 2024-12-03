# Scenario: Devi scrivere un programma Python che simuli un sistema di login. Il sistema deve permettere all'utente di 
# inserire un nome utente e una password. Poi. deve verificare se la combinazione di nome utente e password è corretta. 
# per semplicità, puoi hardcodare nel codice una coppia di nome utente e password che sia considerata corretta. 
# Requisiti: 
# 1 . Input dell'utente: 
# Il programma chiede all'utente di inserire il nome utente. 
# poi, chiede all'utente di inserire la password. 
# 2. Verifica delle Credenziali: 
# Il programma controlla se il nome utente e la password inseriti corrispondono a quelli predefiniti. 
# Puoi decidere di avere le credenziali hardcoded nel codice per questo esercizio. Ad esempio, puoi usare "admin" 
# come nome utente e "12345" come password. 
# 3. Output del Programma: 
# Se il nome utente e la password sono corretti, stampa un messaggio di benvenuto. 
# Altrimenti, informa l'utente che le credenziali sono errate. 
# 4. Modifica dati del programma: 
# o Inserisci una condizione interna che si occupi di cambiare un dato specifico tra quelli inseriti 
# Appena loggato fai scegliere fra due opzioni di domanda segreta e la risposta ( qual'è il colore preferito, quale 
# animale preferito ) 
def signin():
    credenziali = {}
    username_utente = input("REGISTRATI: Inserisci il nome utente: ")
    password_utente = input("REGISTRATI: Inserisci la password: ")
    credenziali['username'] = username_utente
    credenziali['password'] = password_utente
    return credenziali

def login(credenziali):
    n_errori = 0
    while n_errori < 5:
        # 1. Input dell'utente
        username = input("Inserisci il nome utente: ")
        password = input("Inserisci la password: ")

        # 2. Verifica delle Credenziali
        if username == credenziali['username'] and password == credenziali['password']:
            # 3. Output del Programma
            print("Benvenuto!")
            # 4. Modifica dati del programma: domanda segreta
            domanda_segreta()
            break
        else:
            n_errori += 1
            print("Credenziali errate. Riprova.")
            print(f"Numero di tentativi errati: {n_errori}")

    if n_errori == 5:
        print("Hai superato il numero massimo di tentativi. Cambia le credenziali.")
        new_username = input("Inserisci il nuovo nome utente: ")
        new_password = input("Inserisci la nuova password: ")
        credenziali['username'] = new_username
        credenziali['password'] = new_password
        print("Credenziali aggiornate. Riprova a fare il login.")
        login(credenziali)

def domanda_segreta():
    print("Scegli una domanda segreta:")
    print("1. Qual è il tuo colore preferito?")
    print("2. Qual è il tuo animale preferito?")
    
    scelta = input("Inserisci il numero della tua scelta: ")
    
    if scelta == "1":
        risposta = input("Qual è il tuo colore preferito? ")
        print(f"Hai scelto il colore: {risposta}")
    elif scelta == "2":
        risposta = input("Qual è il tuo animale preferito? ")
        print(f"Hai scelto l'animale: {risposta}")
    else:
        print("Scelta non valida.")

# Avvia il programma
credenziali = signin()
login(credenziali)

