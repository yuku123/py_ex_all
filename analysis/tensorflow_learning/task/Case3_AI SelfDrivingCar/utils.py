# -*- coding: UTF-8 -*-

"""
此为样例代码，之后第三个案例录制时会完全重制代码，跟这个代码基本没什么关系
"""

import sys
import array
import numpy as np

from skimage.color import rgb2gray
from skimage.transform import resize
from skimage.io import imread

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from inputs import get_gamepad
import math
import threading

def resize_image(img):
    im = resize(img, (Sample.IMG_H, Sample.IMG_W, Sample.IMG_D))
    im_arr = im.reshape((Sample.IMG_H, Sample.IMG_W, Sample.IMG_D))
    return im_arr

class Screenshot(object):
    SRC_W = 640
    SRC_H = 480
    SRC_D = 3

    OFFSET_X = 0
    OFFSET_Y = 0

class Sample:
    IMG_W = 200
    IMG_H = 66
    IMG_D = 3

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def read(self):
        x = self.LeftJoystickX
        y = self.LeftJoystickY
        a = self.A
        b = self.X
        rb = self.RightBumper
        return [x, y, a, b, rb]

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state

class Data(object):
    def __init__(self):
        self._X = np.load("data/X.npy")
        self._y = np.load("data/y.npy")
        self._epochs_completed = 0
        self._index_in_epoch = 0
        self._num_examples = self._X.shape[0]

    @property
    def num_examples(self):
        return self._num_examples

    def next_batch(self, batch_size):
        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > self._num_examples:

            self._epochs_completed += 1

            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._num_examples
        end = self._index_in_epoch
        return self._X[start:end], self._y[start:end]


def load_sample(sample):
    image_files = np.loadtxt(sample + '/data.csv', delimiter=',', dtype=str, usecols=(0,))
    joystick_values = np.loadtxt(sample + '/data.csv', delimiter=',', usecols=(1,2,3,4,5))
    return image_files, joystick_values

def viewer(sample):
    image_files, joystick_values = load_sample(sample)

    plotData = []

    plt.ion()
    plt.figure('viewer', figsize=(16, 6))

    for i in range(len(image_files)):

        print(i, " ", joystick_values[i,:])

        plotData.append( joystick_values[i,:] )
        if len(plotData) > 30:
            plotData.pop(0)
        x = np.asarray(plotData)

        if (i % 3 == 0):
            plt.subplot(121)
            image_file = image_files[i]
            img = mpimg.imread(image_file)
            plt.imshow(img)

        plt.subplot(122)
        plt.plot(range(i,i+len(plotData)), x[:,0], 'r')
        plt.hold(True)
        plt.plot(range(i,i+len(plotData)), x[:,1], 'b')
        plt.plot(range(i,i+len(plotData)), x[:,2], 'g')
        plt.plot(range(i,i+len(plotData)), x[:,3], 'k')
        plt.plot(range(i,i+len(plotData)), x[:,4], 'y')
        plt.draw()
        plt.hold(False)

        plt.pause(0.0001)
        i += 1

def prepare(samples):
    print("Preparing data")

    X = []
    y = []

    for sample in samples:
        print(sample)
        
        image_files, joystick_values = load_sample(sample)

        y.append(joystick_values)

        for image_file in image_files:
            image = imread(image_file)
            vec = resize_image(image)
            X.append(vec)

    print("Saving to file...")
    X = np.asarray(X)
    y = np.concatenate(y)

    np.save("data/X", X)
    np.save("data/y", y)

    print("Done!")
    return

if __name__ == '__main__':
    if sys.argv[1] == 'viewer':
        viewer(sys.argv[2])
    elif sys.argv[1] == 'prepare':
        prepare(sys.argv[2:])
