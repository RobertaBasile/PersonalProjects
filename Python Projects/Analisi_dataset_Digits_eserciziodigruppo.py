"""Scikit-learn

 Riduzione della Dimensionalità

Esercizio:



Utilizzando il dataset "Digits" disponibile in scikit-learn, 
applica l'Analisi delle Componenti Principali (PCA) per ridurre la dimensionalità dei dati e visualizza le prime due componenti principali. 
Successivamente, valuta l'effetto della riduzione della dimensionalità sulla classificazione utilizzando un semplice modello di classificazione.



Istruzioni:



Carica il dataset "Digits" utilizzando sklearn.datasets.load_digits().
Esplora i dati per comprendere la struttura delle immagini e le etichette associate.
Applica PCA per ridurre i dati da 64 dimensioni (8x8 pixel) a 2 dimensioni.
Visualizza i dati nel nuovo spazio bidimensionale, colorando i punti in base alla cifra rappresentata.
Suddividi il dataset originale in set di training e test.
Addestra un modello di classificazione (ad esempio, LogisticRegression o SVC) sui dati originali e calcola l'accuratezza sul test set.
Ripeti l'addestramento del modello utilizzando i dati ridotti con PCA e confronta le prestazioni.
Analizza come la riduzione della dimensionalità influisce sulla capacità del modello di classificare correttamente le cifre."""
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carica il dataset "Digits"
digits = load_digits()
X = digits.data
y = digits.target

# Esplora i dati
print(f"Shape of X: {X.shape}")
print(f"Shape of y: {y.shape}")

# Applica PCA per ridurre i dati a 2 dimensioni
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualizza i dati nel nuovo spazio bidimensionale
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='cividis', edgecolor='k', s=50)
plt.colorbar(scatter)
plt.xlabel('Prima Componente principale')
plt.ylabel('Seconda Componente principale')
plt.title('PCA of Digits Dataset')
plt.show()
# Le due componenti principali che si ottengono rappresentano le direzioni nei dati originali lungo le quali la varianza è massima. 
# In altre parole, queste componenti principali sono combinazioni lineari delle dimensioni originali che meglio catturano la struttura dei dati.

# Suddividi il dataset originale in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Addestra un modello di classificazione sui dati originali
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy_original = accuracy_score(y_test, y_pred)
print(f"Accuracy dati orig.: {accuracy_original:.2f}")

# Addestra un modello di classificazione sui dati ridotti con PCA
X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y, test_size=0.3, random_state=42)
model_pca = LogisticRegression(max_iter=10000)
model_pca.fit(X_train_pca, y_train_pca)
y_pred_pca = model_pca.predict(X_test_pca)
accuracy_pca = accuracy_score(y_test_pca, y_pred_pca)
print(f"Accuracy con PCA: {accuracy_pca:.2f}")

# Analizza l'effetto della riduzione della dimensionalità
print(f"differenza tra Accuracy: {accuracy_original - accuracy_pca:.2f}")
