import tensorflow.keras
from PIL import Image, ImageOps


from flask import Flask, request , render_template, jsonify
import numpy as np
import cv2
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Server running"


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('/nodechron-models/keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

@app.route("/api", methods=['GET'])
def process_image():
# Replace this with the path to your image

    url = request.args.get('url')

    r = requests.get(url, timeout=60)

    # save the image to disk
    temp_file = 'tmp/temp.jpg'
    f = open(temp_file, "wb")
    f.write(r.content)
    f.close()


    image = Image.open('test_photo.jpg')

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)



if __name__ == "__main__":
    app.run()


