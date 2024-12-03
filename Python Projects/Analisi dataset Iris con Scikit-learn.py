# Esercizio Base


# Carica il dataset Iris.
# Suddividi i dati in training e test.
# Applica l'algoritmo K-Nearest Neighbors
# con n_neighbors=5.
# Valuta la performance del modello
# usando l'accuratezza.

# Importa le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Carica il dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Suddividi i dati in training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inizializza il classificatore K-Nearest Neighbors con n_neighbors=5
knn = KNeighborsClassifier(n_neighbors=5)

# Addestra il modello sui dati di training
knn.fit(X_train, y_train)

# Predici le etichette per il set di test
y_pred = knn.predict(X_test)

# Valuta la performance del modello usando l'accuratezza
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza: {accuracy:.2f}")
