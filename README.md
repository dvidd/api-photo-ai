# Capi-photo-ai
Api for object recognition via POST or GET request of an image url, can be set with different models. It's call CAPi because there is no cap thet is the best

## How to used to api
````shell
curl  "https://capi-photo.com/api?{[URL]}"
````
It would return a json array with the objects detected and the probability of them
### Set other model 
```shell
curl "https://capi-photo.com/api?={[URL]}?model=MobileNetSSD"
```
If you don't specify the model it would use by default MobileNetSSD

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

You have to sent a post request to the server [ http://localhost:5000/detection ] that is run with flask, it will download the image and the pass through the model and detect if any of the things in the list are in the image to test this run 
````python 
$ python3 post

``````
