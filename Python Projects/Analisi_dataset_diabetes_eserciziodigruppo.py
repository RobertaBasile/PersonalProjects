# Esercizio:



# Utilizzando il dataset "Diabetes" disponibile in scikit-learn, sviluppa un modello
# di regressione lineare per predire la progressione della malattia del diabete
# basandoti sulle dieci misurazioni cliniche fornite.



# Istruzioni:

# Carica il dataset "Diabetes" utilizzando sklearn.datasets.load_diabetes().
# Esplora i dati per comprendere le caratteristiche disponibili e la variabile
# target.
# Suddividi il dataset in set di training e test.
# Crea un modello di regressione lineare utilizzando LinearRegression di scikit-
# learn.
# Addestra il modello sui dati di training.
# Valuta le prestazioni del modello sui dati di test utilizzando metriche
# appropriate come l'Errore Quadratico Medio (MSE) e il Coefficiente di
# Determinazione (R²).
# Analizza i risultati e discuti l'efficacia del modello.
# Importazione delle librerie necessarie
### Spiegazione dei Grafici

#### 1. **Scatter Plot: Valori Reali vs Predetti**
# - **Descrizione**:  
#   Questo grafico confronta i valori reali della progressione della malattia del diabete (asse X) con i valori predetti dal modello (asse Y).  
#   - La **linea rossa tratteggiata** rappresenta il caso ideale, dove i valori predetti coincidono perfettamente con quelli reali (predizioni perfette).
#   - I **punti blu** (per i dati standardizzati) o verdi (per i dati non standardizzati) mostrano quanto il modello si avvicina al caso ideale.

# - **Come interpretarlo**:  
#   - Più i punti sono vicini alla linea rossa, migliore è la performance del modello.
#   - Una distribuzione uniforme dei punti intorno alla linea indica che il modello cattura bene il comportamento generale, ma potrebbe esserci rumore nei dati.

# ---

# #### 2. **Grafico dei Residui**
# - **Descrizione**:  
#   Mostra i **residui** (differenza tra valori reali e predetti) in funzione dei valori predetti.  
#   - L'asse X rappresenta i valori predetti dal modello.
#   - L'asse Y rappresenta i residui (valori reali - valori predetti).
#   - La **linea rossa orizzontale** indica residuo pari a 0 (nessun errore di predizione).

# - **Come interpretarlo**:  
#   - I **punti distribuiti casualmente** intorno alla linea rossa suggeriscono che il modello non presenta bias e funziona bene.
#   - Se esiste un **andamento sistematico** nei residui (ad esempio, una curva o una forma a imbuto), ciò indica che il modello non cattura correttamente alcune relazioni nei dati.  
#     - **Curvatura**: il modello potrebbe essere troppo semplice (ad esempio, una relazione non lineare mal rappresentata).
#     - **Forma a imbuto**: indica una varianza non costante nei residui, problema chiamato *eteroschedasticità*.

# ---

# ### Confronto tra Grafici (Standardizzato vs Non Standardizzato)
# 1. **Scatter Plot**:
#    - I grafici per dati standardizzati e non standardizzati dovrebbero essere molto simili, poiché il modello di regressione lineare non è influenzato dalla scala dei dati.
#    - La differenza potrebbe emergere nella comprensione delle caratteristiche (feature) e della loro importanza relativa.

# 2. **Grafico dei Residui**:
#    - Anche qui, una distribuzione casuale dei residui è segno di un buon modello.
#    - Eventuali differenze tra i due grafici potrebbero derivare da come il modello interpreta le variabili con valori su scale diverse.
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt

# Caricamento del dataset "Diabetes" con dati standardizzati
diabetes = load_diabetes()
X = diabetes.data  # Caratteristiche (10 misurazioni cliniche)
y = diabetes.target  # Variabile target (progressione della malattia)

# Esplorazione iniziale del dataset
print("Feature Names:", diabetes.feature_names)
print("\nEsempio di dati:")
print(pd.DataFrame(X, columns=diabetes.feature_names).head())

# Suddivisione del dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Caricamento del dataset "Diabetes" con dati non standardizzati
diabetes_notstandardized = load_diabetes(scaled= False)
X = diabetes_notstandardized.data  # Caratteristiche (10 misurazioni cliniche)
y = diabetes_notstandardized.target  # Variabile target (progressione della malattia)

# Esplorazione iniziale del dataset
print("Feature Names:", diabetes_notstandardized.feature_names)
print("\nEsempio di dati:")
print(pd.DataFrame(X, columns=diabetes_notstandardized.feature_names).head())

# Suddivisione del dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione del modello di regressione lineare
model = LinearRegression()

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione sui dati di test
y_pred = model.predict(X_test)

# Calcolo delle metriche di valutazione
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Stampa dei risultati
print("\nPrestazioni del modello:")
print(f"Errore Quadratico Medio (MSE): {mse:.2f}")
print(f"Coefficiente di Determinazione (R²): {r2:.2f}")


# Scatter plot delle predizioni rispetto ai valori reali
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.title("Confronto tra Valori Reali e Predetti", fontsize=14)
plt.xlabel("Valori Reali", fontsize=12)
plt.ylabel("Valori Predetti", fontsize=12)
plt.grid(alpha=0.3)
plt.show()

# Residual plot
residuals = y_test - y_pred

plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.7, color="purple")
plt.axhline(0, color='red', linestyle='--', linewidth=2)
plt.title("Grafico dei Residui", fontsize=14)
plt.xlabel("Valori Predetti", fontsize=12)
plt.ylabel("Residui (Valore Reale - Valore Predetto)", fontsize=12)
plt.grid(alpha=0.3)
plt.show()




