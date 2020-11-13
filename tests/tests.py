# test the aplication on localhost

import urllib.request
import json

while True:
    image = "https://imagenes.20minutos.es/files/image_656_370/uploads/imagenes/2020/01/29/meme-de-una-mujer-gritando-me-dijiste-que-a-un-gato.jpeg"
    url = f"http://localhost:5000/api?url={image}"
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    if jsondataasbytes != None:
        print("No data recive")
