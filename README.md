# api-photo-ai
Api for object recognition via POST or GET request of an image url, using the model MobileNetSSD
## Example 
````` shell
input :
`````
<img src="https://imagenes.20minutos.es/files/image_656_370/uploads/imagenes/2020/01/29/meme-de-una-mujer-gritando-me-dijiste-que-a-un-gato.jpeg">

`````shell
Output : ['bottle: 61.01%', 'cat: 69.77%', 'person: 92.28%']
`````

## How to used to api
````shell
curl  "https://localhost:5000/api?{[URL]}"
````
It would return a json array with the objects detected and the probability of them

If you don't specify the model or change the model it would use by default MobileNetSSD

### Supported models
| Model | Description |
| --- | --- |
| `MobileNetSSD` | The mobilenet-ssd model is a Single-Shot multibox Detection (SSD) network intended to perform object detection. This model is implemented using the Caffe* framework. For details about this model, check out the<a href="https://github.com/chuanqi305/MobileNet-SSD"> repository.</a> |
### How make it  work local :

To run the server first install the requierements.txt, then run 
`````python
$ python3 server.py
`````
In server.py there is a list of object that with using the MobileNetSSD can recognize, you can change the model and the list.

To check that it works you can run :
````python 
$ python3 tests/tests.py

``````

## TODO :

- do support to others models
- add to a server so the people can use it 
