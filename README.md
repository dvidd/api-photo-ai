# api-photo-ai
Api for object recognition for images via post request
### How it works :

To run the server first install the requierements.txt, then run 
`````python
$ python3 server.py
`````
In server.py there is a list of object that with using the MobileNetSSD can recognize, you can change the model and the list.

You have to sent a post request to the server [ http://localhost:5000/detection ] that is run with flask, it will download the image and the pass through the model and detect if any of the things in the list are in the image to test this run 
````python 
$ python3 post

``````
