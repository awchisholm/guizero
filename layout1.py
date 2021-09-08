from guizero import App, Text, Box
app = App(layout="grid")
#box = Box(app,layout="grid", width="fill", height="fill")
box = Box(app,layout="grid", grid=[0,0])
red = Text(box, bg="red", grid=[5,0], text = 'red  ')
blue = Text(box, bg="blue", grid=[5,1], text = 'blue ')
green = Text(box, bg="green", grid=[1,4], text = 'green')
white = Text(box, bg="white", grid=[10,7], text = 'white')
app.display()

# The learning point is that if there are missing items, the objects to the right and below are shuffled across or up
