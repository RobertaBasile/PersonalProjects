
# Creare un modello di classificazione avanzato
# utilizzando il dataset "Wine" di scikit-learn.



# Il modello dovrà:



# Pre-elaborare i dati con scaling standard.
# Ridurre la dimensionalità con PCA per
# migliorare l'efficienza computazionale.
# Utilizzare un modello di Gradient Boosting
# Classifier.
# Ottimizzare gli iperparametri con
# RandomizedSearchCV.
# Valutare le prestazioni utilizzando
# StratifiedKFold per mantenere la proporzione
# delle classi.


from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

'''1. PCA (pca__n_components):
Valori: [5, 8, 10]
Questi numeri rappresentano il numero di componenti principali da mantenere dopo la riduzione della dimensionalità.
Sono stati scelti valori moderati perché il dataset "Wine" ha solo 13 feature originali, 
e ridurre drasticamente la dimensionalità potrebbe portare alla perdita di informazioni utili.
5, 8 e 10 permettono di testare diverse quantità di informazioni mantenute, bilanciando complessità e prestazioni.
2. Gradient Boosting Classifier - Numero di alberi (gbc__n_estimators):
Valori: [50, 100, 150]
Il numero di alberi influenza direttamente la capacità del modello di apprendere pattern complessi.
50 alberi forniscono un modello veloce con meno rischio di overfitting.
150 alberi permettono un apprendimento più approfondito, ma con un costo computazionale maggiore.
100 è un valore intermedio comunemente usato come default.
3. Gradient Boosting Classifier - Tasso di apprendimento (gbc__learning_rate):
Valori: [0.01, 0.1, 0.2]
Il learning_rate controlla quanto velocemente il modello si adatta agli errori residui.
0.01 è un valore piccolo, utile per modelli più stabili ma più lenti da allenare.
0.2 è relativamente più grande e permette di apprendere più rapidamente, ma con un rischio maggiore di overfitting.
0.1 è spesso una scelta predefinita bilanciata.
4. Gradient Boosting Classifier - Profondità massima degli alberi (gbc__max_depth):
Valori: [3, 4, 5]
La profondità massima controlla la complessità di ogni albero. Alberi più profondi possono modellare meglio i dati complessi, ma rischiano di overfittare.
Una profondità di 3 è leggera e spesso sufficiente per dataset con meno feature o meno complessi.
4 e 5 permettono di modellare strutture più complesse senza eccessivo rischio di overfitting grazie all'uso del learning_rate.'''

# Caricamento del dataset Wine
wine = load_wine()
X, y = wine.data, wine.target

# Suddivisione dei dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Creazione della pipeline con StandardScaler, PCA e GradientBoostingClassifier
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('gbc', GradientBoostingClassifier(random_state=42))
])

# Definizione dei parametri per la ricerca degli iperparametri
param_distributions = {
    'pca__n_components': [5, 8, 10],
    'gbc__n_estimators': [50, 100, 150],
    'gbc__learning_rate': [0.01, 0.1, 0.2],
    'gbc__max_depth': [3, 4, 5]
}

# Impostazione della StratifiedKFold per il cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Creazione del RandomizedSearchCV
random_search = RandomizedSearchCV(
    pipeline,
    param_distributions=param_distributions,
    n_iter=20,
    scoring='accuracy',
    cv=cv, 
    random_state=42,
    n_jobs=-1
)

# Esecuzione della ricerca degli iperparametri
random_search.fit(X_train, y_train)

# Valutazione del modello sui dati di test
y_pred = random_search.best_estimator_.predict(X_test)
report = classification_report(y_test, y_pred, target_names=wine.target_names)

# Migliori parametri trovati e report di classificazione
print("Migliori parametri:", random_search.best_params_)
print("\nReport di classificazione:\n", report)
