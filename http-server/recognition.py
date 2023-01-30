import json
import cv2
import os
import keras
import matplotlib.pyplot as plt

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.applications.efficientnet import EfficientNetB4, preprocess_input
import efficientnet.tfkeras as efn
from PIL import Image

from glob import glob
import keras_ocr

project_root = os.path.abspath(os.path.dirname(__file__))
folder = "../images"

cascPath = "haarcascade_frontalface_alt.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)


def food_recognition(file_name):
    model = EfficientNetB4(weights='imagenet')

    file = os.path.join(project_root, folder, file_name)
    img = Image.open(file)
    img = img.resize((380, 380))

    x = np.array(img)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x)
    preds = model.predict(x)
    labels = keras.applications.imagenet_utils.decode_predictions(preds, top=3)[0]
    prediction = [
        (labels[0][1], str(labels[0][2])),
        (labels[1][1], str(labels[1][2])),
        (labels[2][1], str(labels[2][2]))
    ]
    output = {"prediction": prediction, "topic": "food", "status": True}
    return json.dumps(output)


def menu_recognition(file_name):
    file = os.path.join(project_root, folder, file_name)
    img = glob(file)

    pipeline = keras_ocr.pipeline.Pipeline()
    results = pipeline.recognize(img)

    words = []
    for result in results[0]:
        text = result[0]
        words.append(text)

    output = {
        "topic": "menu",
        "words": words,
        "status": True
    }
    return json.dumps(output)


def restaurant_recognition(file_name):
    # Read the image
    path = os.path.join(project_root, folder, file_name)
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Found {0} faces in image {1}!".format(len(faces), file_name))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show found faces for 1 second
    cv2.imshow("Faces found", image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
    # Save the processed image
    # new_filename = "processed_" + path
    # status = cv2.imwrite(os.path.join("saved", new_filename), path)
    # print("Image written to file-system:", status)

    output = {
        "number_of_faces": len(faces),
        "topic": "restaurant",
        "status": True
    }
    return json.dumps(output)
