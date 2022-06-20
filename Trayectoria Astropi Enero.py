import folium
import pandas as pd
m=folium.Map(location=[10,0],zoom_start=2,tiles="Stamen Terrain")
df=pd.read_excel("astropi_datos_enero2022.xls")
latitud=df.iloc[:,1]
print(latitud)
longitud=df.iloc[:,2]
print(longitud)
for valor in range(len(latitud)):
    folium.Circle(radius=100,location=[latitud[valor],longitud[valor]],popup="The Waterfront",color="crimson",fill=False,).add_to(m)
m.save("trayectoria2.html")