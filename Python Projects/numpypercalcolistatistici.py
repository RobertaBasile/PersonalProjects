#Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 
# e fate i seguenti calcoli:
# Calcolo della media;
# Calcolo della moda;
# Calcolo della deviazione standard;
# Trasformatelo in un array 5 X 10
import numpy as np
from scipy import stats

# Creazione dell'array unidimensionale con 50 valori randomici 
# compresi tra 1 e 1.000
array_unidimensionale = np.random.randint(1, 1000, 50)
print("Array unidimensionale:", array_unidimensionale)

# Calcolo della media
media = np.mean(array_unidimensionale)
print("Media:", media)

# Calcolo della moda
moda = stats.mode(array_unidimensionale)
print("Moda:", moda.mode)

# Calcolo della deviazione standard
deviazione_standard = np.std(array_unidimensionale)
print("Deviazione standard:", deviazione_standard)

# Trasformazione in un array 5x10
array_5x10 = array_unidimensionale.reshape(5, 10)
print("Array 5x10:\n", array_5x10)
