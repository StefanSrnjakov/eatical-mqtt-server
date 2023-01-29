import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

imgDirPath = "D:\\fakultet\\treta\\prvSem\\proekti\\pora\\backend\\eatical-mqtt-server\\images\\"
# add your path here

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
    gray = cv2.cvtColor(file_name, cv2.COLOR_BGR2GRAY)

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
        cv2.rectangle(file_name, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show found faces for 1 second
    cv2.imshow("Faces found", file_name)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    # Save the processed image
    # new_filename = "processed_" + file_name
    # status = cv2.imwrite(os.path.join("saved", new_filename), file_name)
    # print("Image written to file-system:", status)

    return {
        "number_of_faces": len(faces),
        "topic": "restaurant"
    }
