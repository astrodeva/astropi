import folium 
import pandas as pd 
m = folium.Map(location=[10, 0], zoom_start=2, tiles="Stamen Terrain") 
df=pd.read_excel('astropi_datos_enero2022.xls') 
latitud=df.iloc[:,1] 
longitud=df.iloc[:,2] 
angulo=df.iloc[:,6]
for valor in range(len(latitud)):
    folium.Marker(location=[latitud[valor],longitud[valor]], icon=folium.Icon(color="green", icon = 'fa-paper-plane', prefix='fa', angle=int(angulo[valor])),).add_to(m) 
m.save("trayectoriaorientación.html")