import folium
import pandas as pd
from colormap.colors import rgb2hex
m = folium.Map(location=[10, 0], zoom_start=3, tiles="Stamen Terrain")
df=pd.read_excel('astropi_datos_enero2022.xls')
latitud=df.iloc[:,1]
print (latitud)
longitud=df.iloc[:,2]
print (longitud)
campomag=df.iloc[:,21]
print(campomag)
for valor in range(len(latitud)):
    campomag_modif=int((campomag[valor]-1)*255/(80-10))
    y=rgb2hex(campomag_modif,255-campomag_modif,0) 
    folium.Circle(radius=100,location=[latitud[valor],longitud[valor]],popup="TheWaterfront",color=y,fill=True,).add_to(m)
m.save("trayectoriamagnetico.html")
