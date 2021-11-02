from guizero import App, Text, Picture, PushButton
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter  
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
    r = np.random.randint(10, size=200)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    plt.figure(1)
    plt.plot(t, r)
    plt.title(f'Simple graph {dt_string}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(image_location)
    plt.close(1)
    plt.show()

def animation(image_location):
    fig, ax = plt.subplots()  
    x, ysin, ycos = [], [], []  
    ln1, = plt.plot([], [], 'ro')  
    ln2, = plt.plot([], [], 'm*')  
    def init():
        ax.set_xlim(0, 2*np.pi)  
        ax.set_ylim(-1, 1) 
    
    def update(i):
        x.append(i)  
        ysin.append(np.sin(i))  
        ycos.append(np.cos(i))  
        ln1.set_data(x, ysin)  
        ln2.set_data(x, ycos)

    ani = FuncAnimation(fig, update, np.linspace(0, 2*np.pi, 64), init_func=init)  
    #plt.show()
    writer = PillowWriter(fps=25)  
    ani.save(image_location, writer=writer)  

def counter():
    text.value = int(text.value) + 1
    make_image(static_image)
    picture2.image=static_image

global_image_location = 'matplotlib_images/'
static_image = f'{global_image_location}plot.png'
animated_image = f'{global_image_location}demo_sine.gif'
app = App()
make_image(static_image)
animation(animated_image)

pushbutton2 = PushButton(app, image=static_image, width=100, height=100, text='Static')
pushbutton1 = PushButton(app, image=animated_image, width=100, height=100, text='Animated')
picture1 = Picture(app, image=static_image, height=200, width=200)
picture2 = Picture(app, image=static_image, height=200, width=200)
picture3 = Picture(app, image=animated_image, height=200, width=200)
text = Text(app, text="1")
text.repeat(1000, counter)  # Schedule call to counter() every 1000ms
app.display()