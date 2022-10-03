import json

import pandas as pd
import requests

url = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"
data = requests.get(url)
json_data = json.loads(data.content)

df_ballot = pd.DataFrame(json_data['cand'])[['nm', 'vap', 'pvap']] 
df_ballot.columns = ['Candidato','Votos','%']
df_ballot
