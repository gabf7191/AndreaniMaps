import requests as rq
import json
import csv

#Requests...
response = rq.get("https://api.andreani.com/v2/sucursales")

#response = rq.get("https://api.qa.andreani.com/v1/regiones")



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


print(response.status_code)
jprint(response.json())

for line in response.json():
    print (line)


    with open('coord.csv', 'w',encoding="utf8") as f:
        f.write("id,codigo,descripcion,latitud,longitud")
        f.write('\n')
        for line in response.json():
                if line["id"] < 20000 and line["coordenadas"]["latitud"]!="":
                    f.write(str(line["id"]))
                    f.write(",")
                    f.write(str(line["codigo"]))
                    f.write(",")
                    f.write(str(line["descripcion"]))
                    f.write(",")
                    f.write(str(line["coordenadas"]["latitud"]))
                    f.write(",")
                    f.write(str(line["coordenadas"]["longitud"]))
                    f.write('\n')







