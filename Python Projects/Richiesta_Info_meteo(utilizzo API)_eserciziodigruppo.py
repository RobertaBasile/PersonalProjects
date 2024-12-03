'''
Create un programma python che permette tramite le api
https://open-meteo.com/en/docs (per le previsioni metereologiche) e
(per l’ottenimento in automatico della propria
langitudine e latitudine tramite l’indirizzo ip), di vedere le previsione
metereologiche.
L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni.


'''

import requests
import json

## link1 = "https://open-meteo.com/en/docs"
## link1extended = "https://open-meteo.com/en/docs#latitude=10&longitude=11&hourly=temperature_2m,precipitation_probability,wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m&forecast_days=3"

api_link_start = "https://api.open-meteo.com/v1/forecast?daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&"
api_link_1 = "latitude="
api_link_2 = "&longitude="
api_link_3 = "&precipitation_probability"
api_link_4 = "&forecast_days="


link2_part1 = "https://geocoding-api.open-meteo.com/v1/search?name="
link2_part2 = "&count=1&language=en&format=json"

def request_dumper(link):
    response = requests.get(link)
    text_response = response.text
    json_response = json.loads(text_response)
    return json_response

input1 = input("Dammi la città da cercare: ")

link_completo = link2_part1 + input1 + link2_part2
json_citta = request_dumper(link_completo)
##print(json_citta)

latitudine = json_citta.get("results")[0].get("latitude")
longitudine = json_citta.get("results")[0].get("longitude")

api_call_link = api_link_start + api_link_1 + str(latitudine) + api_link_2 + str(longitudine) + api_link_3
input2 = input("Per quanti giorni restituire le previsioni? Scegli tra 1, 3 o 7 giorni: ")
api_call_link += api_link_4 + input2

print(api_call_link)

previsioni = request_dumper(api_call_link)
##previsioni = json.dumps(previsioni, indent = 4)
##print(previsioni)

print("Le previsioni per la città: " + input1 + ", situata in latitudine " + str(latitudine) + " e longitudine " + str(longitudine) + " sono:")


print("\nPrevisioni meteo:")
for i in range( int(input2) ):
    data = previsioni["daily"]["time"][i]
    temp_massima = previsioni["daily"]["temperature_2m_max"][i]
    temp_minima = previsioni["daily"]["temperature_2m_min"][i]
    precipitazioni = previsioni["daily"]["precipitation_sum"][i]
    vento = previsioni["daily"]["wind_speed_10m_max"][i]
    print(f"\nData: {data}")
    print(f"Temperatura massima: {temp_massima}°C")
    print(f"Temperatura minima: {temp_minima}°C")
    print(f"Precipitazioni: {precipitazioni} mm")
    print(f"Velocità del vento: {vento} km/h")

