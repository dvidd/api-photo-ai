# test the aplication on localhost

import urllib.request
import json

body = {'image_path': 'https://cnet3.cbsistatic.com/img/hOQak1FRJY83unumvejS8f0H4ao=/1092x0/2019/10/15/0a8cb0d7-234a-4443-82e0-a17b149d6406/self-cleaning-water-bottles.jpg'}


while True:
    myurl = "http://localhost:5000/detection"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
