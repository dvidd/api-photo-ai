from flask import Flask, request , render_template
import numpy as np
import cv2
import requests

net = cv2.dnn.readNetFromCaffe("../models/MobileNetSSD_deploy.prototxt.txt", "../models/MobileNetSSD_deploy.caffemodel")


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api', methods=['GET', 'POST'])
def process_image():
  if request.json:
    data = request.json

    image_path = data.get("image_path")

    print(image_path)

    r = requests.get(image_path, timeout=60)

    # save the image to disk
    temp_file = 'tmp/temp.jpg'
    f = open(temp_file, "wb")
    f.write(r.content)
    f.close()

    image = cv2.imread(temp_file)

    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
      # extract the confidence (i.e., probability) associated with the
      # prediction
      confidence = detections[0, 0, i, 2]

      # filter out weak detections by ensuring the `confidence` is
      # greater than the minimum confidence
      if confidence > .5:
        # extract the index of the class label from the `detections`,
        # then compute the (x, y)-coordinates of the bounding box for
        # the object
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # display the prediction
        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
        print("[INFO] {}".format(label))

        return str(label)
  else:
    return "no json received"


if __name__ == "__main__":
    app.run()
