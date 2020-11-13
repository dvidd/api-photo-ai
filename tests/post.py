# test the aplication on localhost

import urllib.request
import json

body = {'image_path': 'https://i.kym-cdn.com/photos/images/newsfeed/001/505/718/136.jpg'}


myurl = "http://localhost:8888/api"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
