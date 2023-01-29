import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

imgDirPath = "D:\\fakultet\\treta\\prvSem\\proekti\\pora\\backend\\eatical-mqtt-server\\images\\"
# add your path here
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
    pass
    # return json object (bson)
