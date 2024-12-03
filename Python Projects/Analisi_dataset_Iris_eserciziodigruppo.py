# Esercizio:

# Utilizzando il dataset "Iris" disponibile in scikit-learn, applica l'algoritmo K-
# Means per raggruppare i campioni e confronta i cluster ottenuti con le etichette
# originali delle specie di iris.



# Istruzioni:

# Carica il dataset "Iris" utilizzando sklearn.datasets.load_iris().
# Considera tutte le quattro caratteristiche (lunghezza e larghezza di sepali e
# petali) per il clustering.
# Applica l'algoritmo K-Means con un numero di cluster pari a 3.
# Visualizza i cluster ottenuti utilizzando tecniche di visualizzazione adeguate
# (ad esempio, plot 2D delle prime due componenti principali).
# Confronta i cluster assegnati dall'algoritmo con le etichette reali delle
# specie di iris.
# Calcola metriche di valutazione come l'Indice di Rand Adjusted o l'Homogeneity
# Score per quantificare la qualità del clustering.
# Discuta i risultati e l'eventuale corrispondenza tra i cluster e le specie
# reali.

### Grafico dei Cluster K-Means
# - **Asse X e Asse Y**: In questo grafico, gli assi rappresentano le prime due caratteristiche del dataset Iris (lunghezza e larghezza del sepalo).
# - **Punti**: Ogni punto rappresenta un campione del dataset Iris.
# - **Colori**: I colori dei punti indicano i cluster assegnati dall'algoritmo K-Means. 
# Ogni colore rappresenta un cluster diverso.
# - **Titolo**: "Cluster K-Means (senza riduzione dimensionale)" indica che i cluster sono stati ottenuti utilizzando tutte le caratteristiche del dataset senza riduzione dimensionale.
# - **Legenda**: La barra dei colori a destra del grafico mostra la corrispondenza tra i colori e i cluster.

# ### Grafico delle Etichette Reali
# - **Asse X e Asse Y**: Anche in questo grafico, gli assi rappresentano le prime due caratteristiche del dataset Iris (lunghezza e larghezza del sepalo).
# - **Punti**: Ogni punto rappresenta un campione del dataset Iris.
# - **Colori**: I colori dei punti indicano le etichette reali delle specie di iris. Ogni colore rappresenta una specie diversa.
# - **Titolo**: "Etichette Reali (senza riduzione dimensionale)" indica che i punti sono colorati in base alle etichette reali delle specie di iris senza riduzione dimensionale.
# - **Legenda**: La barra dei colori a destra del grafico mostra la corrispondenza tra i colori e le specie di iris.

# ### Interpretazione
# - **Confronto**: Confrontando i due grafici, puoi vedere come i cluster ottenuti dall'algoritmo K-Means si sovrappongono con le etichette reali delle specie di iris. 
# Idealmente, i punti dello stesso colore nel grafico dei cluster K-Means dovrebbero corrispondere ai punti dello stesso colore nel grafico delle etichette reali.
# - **Valutazione**: Utilizzando metriche come l'Indice di Rand Adjusted (ARI) e 
# l'Homogeneity Score, si può quantificare quanto bene i cluster ottenuti corrispondono alle etichette reali. 
# Valori alti di queste metriche indicano una buona corrispondenza.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, homogeneity_score

# Carica il dataset Iris
iris = load_iris()
X = iris.data
y = iris.target
print (iris)
# Applica l'algoritmo K-Means con 3 cluster
kmeans = KMeans(n_clusters=3, random_state=42)
# Addestramento del modello
kmeans.fit(X)

# Predizione dei cluster
y_kmeans = kmeans.predict(X)

# Visualizza i cluster ottenuti
plt.figure(figsize=(14, 6))

# Plot dei cluster K-Means
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', marker='o', edgecolor='k', s=100)
plt.title('Cluster K-Means sepali')
plt.xlabel('Lunghezza sepalo')
plt.ylabel('Larghezza sepalo')
plt.colorbar()

# Plot delle etichette reali
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k', s=100)
plt.title('Etichette Reali sepali')
plt.xlabel('Lunghezza sepalo')
plt.ylabel('Larghezza sepalo')
plt.colorbar()

plt.show()

# Visualizza i cluster ottenuti
plt.figure(figsize=(14, 6))

# Plot dei cluster K-Means (caratteristiche dei petali)
plt.subplot(1, 2, 1)
plt.scatter(X[:, 2], X[:, 3], c=y_kmeans, cmap='viridis', marker='o', edgecolor='k', s=100)
plt.title('Cluster K-Means (caratteristiche dei petali)')
plt.xlabel('Lunghezza petalo')
plt.ylabel('Larghezza petalo')
plt.colorbar()

# Plot delle etichette reali (caratteristiche dei petali)
plt.subplot(1, 2, 2)
plt.scatter(X[:, 2], X[:, 3], c=y, cmap='viridis', marker='o', edgecolor='k', s=100)
plt.title('Etichette Reali (caratteristiche dei petali)')
plt.xlabel('Lunghezza petalo')
plt.ylabel('Larghezza petalo')
plt.colorbar()

plt.show()


# Confronta i cluster con le etichette reali
ari = adjusted_rand_score(y, y_kmeans)
homogeneity = homogeneity_score(y, y_kmeans)

print(f'Indice di Rand Adjusted: {ari:.2f}')
print(f'Homogeneity Score: {homogeneity:.2f}')


