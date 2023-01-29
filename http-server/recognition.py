import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

project_root = os.path.abspath(os.path.dirname(__file__))
folder = "../images"

cascPath = "haarcascade_frontalface_alt.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)


def food_recognition(file_name):
    img = mpimg.imread(imgDirPath + file_name)
    plt.imshow(img, cmap="gray")
    plt.axis('off')
    plt.show()
    return {"works" : True}




def menu_recognition(file_name):
    pass
    # return json object (bson)


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

    return {
        "number_of_faces": len(faces),
        "topic": "restaurant"
    }
