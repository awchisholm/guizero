from guizero import App, Text, Picture
import matplotlib.pyplot as plt
from  matplotlib.pyplot import isinteractive
import numpy as np
from datetime import datetime
import time
import os

# You must call this after the call to App() !!!
def make_image(image_location):
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    plt.figure(1)
    plt.plot(t, s)
    plt.title(f'Simple graph {dt_string}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(image_location)
    plt.close(1)
    plt.show()

# Action you would like to perform
def counter():
    text.value = int(text.value) + 1
    make_image(global_image_location)
    picture.image=global_image_location

global_image_location = 'matplotlib_images/plot.png'
app = App()
make_image(global_image_location)
picture = Picture(app, image=global_image_location)
text = Text(app, text="1")
text.repeat(1000, counter)  # Schedule call to counter() every 1000ms
app.display()