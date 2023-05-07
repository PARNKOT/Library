import random

import keras.models
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist


np.random.seed(123)


def train():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1).astype('float32')
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1).astype('float32')

    # Нормализация (нужна ли?)
    x_train /= 255
    x_test /= 255

    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)

    model = Sequential()

    model.add(Conv2D(32, (5, 5), activation='relu',
                     input_shape=(x_train.shape[1], x_train.shape[2], 1)))  # data_format='channels_first'))

    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              batch_size=32, epochs=2, verbose=1)

    model.save("model")
    model.save_weights("weights.h5")

    print(model.predict(x_test[0]))
    print(y_test[0])


def train2():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1).astype('float32')
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1).astype('float32')

    # Нормализация (нужна ли?)
    x_train /= 255
    x_test /= 255

    number_of_classes = 10

    y_train = np_utils.to_categorical(y_train, number_of_classes)
    y_test = np_utils.to_categorical(y_test, number_of_classes)

    model = Sequential()

    model.add(Conv2D(32, (5, 5), input_shape=(x_train.shape[1], x_train.shape[2], 1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(number_of_classes, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=2, batch_size=200)

    model.save("model2")
    model.save_weights("weights2.h5")

    print(model.predict(x_test[0]))
    print(y_test[0])


def test_predict():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    #x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1).astype('float32')
    #x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1).astype('float32')

    #x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    # Нормализация (нужна ли?)
    #x_train /= 255
    x_test /= 255

    # y_train = np_utils.to_categorical(y_train, 10)
    # y_test = np_utils.to_categorical(y_test, 10)

    # model = Sequential()
    #
    # model.add(Conv2D(32, (5, 5), activation='relu',
    #                  input_shape=(x_train.shape[1], x_train.shape[2], 1)))  # data_format='channels_first'))
    #
    # model.add(Conv2D(32, (3, 3), activation='relu'))
    # model.add(MaxPooling2D(pool_size=(2, 2)))
    # model.add(Dropout(0.25))
    #
    # model.add(Flatten())
    # model.add(Dense(128, activation='relu'))
    # model.add(Dropout(0.5))
    # model.add(Dense(10, activation='softmax'))
    #
    # model.compile(loss='categorical_crossentropy',
    #               optimizer='adam',
    #               metrics=['accuracy'])
    #
    # model.load_weights("weights.h5")

    model = keras.models.load_model("model2")

    rand_index = random.randint(0, len(x_test))
    rand_img_x = x_test[rand_index]
    rand_img_y = y_test[rand_index]

    rand_img_x = np.resize(rand_img_x, (28, 28, 1))
    #img2 = np.array(rand_img_x)
    #img2 = img2.reshape(1, 28, 28, 1)

    predicted_y = model.predict(rand_img_x)#.reshape(1, 28, 28, 1))

    # rand_img_x = cv.resize(rand_img_x, (rand_img_x.shape[0]*10, rand_img_x.shape[1]*10))
    print(rand_img_x.shape)
    # cv.putText(rand_img_x, f"Must be: {rand_img_y}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    # cv.putText(rand_img_x, f"Predict: {predicted_y}", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    plt.text(1, 1, f"{rand_img_y}")
    plt.imshow(rand_img_x)
    plt.show()


drawing = False  # true if mouse is pressed
mode = False  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix, iy, drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0),-1)
            else:
                cv.circle(img, (x,y), 7, (255, 255, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img, (x, y), 7, (255, 255, 255), -1)


if __name__ == "__main__":
    model = keras.models.load_model("model2")

    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while (1):
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == ord("q"):
            break

    img = cv.resize(img, (28, 28))
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    predicted_y = model.predict(img.reshape(1, 28, 28, 1))
    plt.text(1, 1, predicted_y.argmax())

    plt.imshow(img)
    plt.show()
    # model = keras.models.load_model("model2")
    # (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #
    #
    # digits_img = cv.imread("images/digits3.jpeg", cv.IMREAD_GRAYSCALE)
    # roi = cv.selectROI("roi", digits_img)
    # #img = digits_img[roi[0]:roi[0]+roi[2], roi[1]:roi[1]+roi[3]]
    # img = digits_img[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
    # img = cv.resize(img, (28, 28))
    # img = 255 - img
    #
    # img2 = x_test[1]
    # img2 = np.resize(img2, (28, 28, 1))
    #
    # predicted_y = model.predict(img.reshape(1, 28, 28, 1))  # .reshape(1, 28, 28, 1))
    # predicted_y_2 = model.predict(img2.reshape(1, 28, 28, 1))  # .reshape(1, 28, 28, 1))
    #
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.text(1, 1, f"{predicted_y.argmax()}")
    # ax2.text(1, 1, f"{predicted_y_2.argmax()}")
    # ax1.imshow(img)
    # ax2.imshow(img2)
    # plt.show()
    # #test_predict()


