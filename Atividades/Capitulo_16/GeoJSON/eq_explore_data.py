from pathlib import Path
import json

import plotly.express as px

# Lê os dados como uma string e os converte em um objeto Python
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Cria uma versão mais legível do arquivo de dados
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# Examina todos os terremotos no conjunto de dado
all_eq_dicts = all_eq_data['features']
mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

# print(mags[:10])
# print(lons[:10])
# print(lats[:10])
    
title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags, # Informa quais valores usar para determinar a correspondência de cada marcação com a escala de cores. 
        color_continuous_scale='Viridis', # Informa qual escala de cores usar. Viridis varia do azul escuro ao amarelo vivo 
        labels={'color': 'Magnitude'}, # Define o nome da escala de cores à direita do mapa
        projection='natural earth', # Define o estilo de projeção do mapa
        hover_name=eq_titles, # Adiciona título às tooltips
    )
fig.show()