# test the aplication on localhost

import requests
import json

image = "https://imagenes.20minutos.es/files/image_656_370/uploads/imagenes/2020/01/29/meme-de-una-mujer-gritando-me-dijiste-que-a-un-gato.jpeg"
url = f"http://localhost:5000/api?url={image}"
r = requests.get(url)

# extracting data in json format
try:
    data = r.json()
    print(data)
except:
    print("Not working ")
