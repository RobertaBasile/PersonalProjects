# ML Fin

# Esercizio finale



# Obiettivo: Creare un modello di Machine Learning per classificare le cifre da 0 a 9 utilizzando il
# dataset MNIST Digits.

# Punti dell'esercizio

# Importazione dei Dati
    # Carica il dataset MNIST Digits utilizzando sklearn.datasets.
    # Visualizza alcune cifre per comprendere i dati.
# Preprocessing dei Dati
    # Normalizza i dati dividendo i valori dei pixel per il massimo valore possibile (16).
    # Dividi il dataset in un training set e un test set usando train_test_split.
# Scelta del Modello
    # Scegli un algoritmo di classificazione, come Support Vector Machine (SVM) o Random Forest.
    # Configura il modello con parametri di base.
# Addestramento del Modello
    # Addestra il modello sui dati di training.
    # Verifica che il processo termini senza errori.
# Valutazione del Modello
    # Utilizza il test set per valutare il modello.
    # Calcola l'accuratezza e stampa un report di classificazione.
# Visualizzazione dei Risultati
    # Mostra alcune immagini del test set con le loro predizioni e i valori reali.
    # Identifica eventuali errori di classificazione.
# Esperimenti Extra (Facoltativo)
    # Cambia il modello con un altro algoritmo (es. k-Nearest Neighbors o Decision Tree).
    # Applica la cross-validation per migliorare la stabilità delle valutazioni.
    # Genera una matrice di confusione per analizzare gli errori.
#----------------------------------------------------------------
# Importa le librerie necessarie
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
from IPython.display import display

# Importazione dei Dati
digits = load_digits()
X = digits.data
y = digits.target

# Crea un DataFrame con i dati e le etichette delle caratteristiche 
df = pd.DataFrame(data=digits.data, columns=digits.feature_names) 
# Aggiungi la colonna delle classi 
df['target'] = digits.target 
# Visualizza il DataFrame utilizzando display()  
print("Ecco il dataset Digits:")
display(df)
# Utilizza il metodo describe() per ottenere una descrizione statistica del DataFrame 
descrizione = df.describe() 
# Stampa la descrizione 
print(descrizione)

# Preprocessing dei Dati
# Normalizza i dati dividendo i valori dei pixel per il massimo valore possibile (16)
X = X / 16.0

# Dividi il dataset in un training set e un test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scelta del Modello
# Scegli un algoritmo di classificazione, come Random Forest
model = RandomForestClassifier(random_state=42)

# Definisci una griglia di iperparametri
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'criterion': ['gini', 'entropy']
}

# Utilizza GridSearchCV per trovare la migliore combinazione di iperparametri
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Addestra il modello ottimizzato sull'intero set di training
best_rf = grid_search.best_estimator_
best_rf.fit(X_train, y_train)

# Valutazione del Modello
# Utilizza il test set per valutare il modello
y_pred = best_rf.predict(X_test)

# Calcola l'accuratezza e stampa un report di classificazione
accuracy = accuracy_score(y_test, y_pred)
print("Accuratezza:", accuracy)
print("Report di classificazione:\n", classification_report(y_test, y_pred))

# Visualizzazione dei Risultati
# Mostra alcune immagini del test set con le loro predizioni e i valori reali
# Il codice visualizza alcune immagini del test set con le loro predizioni e i valori reali. 
# Inizia creando una figura con una griglia di 1 riga e 10 colonne di assi, 
# impostando la dimensione della figura a 10 pollici di larghezza e 3 pollici di altezza. 
# Utilizza `zip` per combinare gli assi, le immagini del test set, le predizioni del modello 
# e i valori reali in un unico iteratore, permettendo di iterare simultaneamente su questi 
# quattro elementi. 
# Per ogni immagine, disattiva la visualizzazione degli assi per rendere la visualizzazione 
# più pulita, ridimensiona l'immagine da un array piatto di 64 elementi (8x8 pixel) 
# a una matrice 8x8, e visualizza l'immagine sull'asse corrente utilizzando una 
# mappa di colori in scala di grigi. 
# Imposta il titolo dell'asse corrente con le predizioni e i valori reali per ogni immagine.
# Infine, mostra la figura con tutte le immagini e i titoli impostati.

fig, axes = plt.subplots(1, 10, figsize=(10, 3))
for ax, image, prediction, actual in zip(axes, X_test, y_pred, y_test):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'P: {prediction}\nA: {actual}')
plt.show()

# Identifica eventuali errori di classificazione
errors = np.where(y_pred != y_test)[0]
print(f"Numero di errori di classificazione: {len(errors)}")

# Esperimenti Extra (Facoltativo)
# Genera una matrice di confusione per analizzare gli errori
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=digits.target_names, yticklabels=digits.target_names)
plt.xlabel('Predicted')
plt.ylabel('Reale')
plt.title('Confusion Matrix')
plt.show()
