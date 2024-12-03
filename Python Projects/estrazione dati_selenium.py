from selenium import webdriver
from selenium.webdriver.common.by import By
import time
""" Visita https://www.w3schools.com/html/html_tables.asp 
Estrai i dati dalla prima tabella sulla pagina e stampali in formato leggibile """
def extract_table_data():
    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    
    # Attendi che la pagina si carichi
    time.sleep(5)
    
    # Trova la prima tabella sulla pagina
    table = driver.find_element(By.XPATH, "//table[@id='customers']")
    
    # Estrai le intestazioni della tabella
    headers = table.find_elements(By.XPATH, ".//th")
    header_names = [header.text for header in headers]
    
    # Estrai le righe della tabella
    rows = table.find_elements(By.XPATH, ".//tr")
    
    # Estrai i dati delle celle
    table_data = []
    for row in rows[1:]:  # Salta la prima riga che contiene le intestazioni
        cells = row.find_elements(By.XPATH, ".//td")
        cell_data = [cell.text for cell in cells]
        table_data.append(cell_data)
    
    # Stampa i dati in formato leggibile
    print(" | ".join(header_names))
    print("-" * 50)
    for row_data in table_data:
        print(" | ".join(row_data))
    
    # Chiudi il driver
    driver.quit()

# Esegui la funzione
extract_table_data()
