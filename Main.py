import folium
import pandas as pd



Coord = pd.read_csv("coord.csv",encoding="utf8")


##Agrego columna para saber si es duplicado ##
Coord2 = Coord.duplicated(subset ="latitud")

Coord.insert(5,"dupl",Coord2)


#Coord.drop_duplicates(subset ="latitud", keep = False, inplace = True)

Coord.to_csv("RESULTADO.csv",sep=";",decimal=",")




# Make an empty map
m = folium.Map(location=[-36.631260,-64.310960], tiles='OpenStreetMap', zoom_start=4)

for i in range (0,len(Coord)):
    if Coord.iloc[i]["dupl"] == False:
        folium.Marker([Coord.iloc[i]["latitud"], Coord.iloc[i]["longitud"]],popup = Coord.iloc[i]["descripcion"],tooltip = Coord.iloc[i]["codigo"]).add_to(m)
    else:
        folium.Marker([Coord.iloc[i]["latitud"], Coord.iloc[i]["longitud"]], popup=Coord.iloc[i]["descripcion"],tooltip = Coord.iloc[i]["codigo"],icon = folium.Icon(color='blue',icon_color='#FFFF00')).add_to(m)

#,tooltip = Coord.iloc[i]["codigo"]
# Save it as html
m.save('Sucursales Andreani.html')
