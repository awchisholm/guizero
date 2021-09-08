from guizero import App, Text, Box
app = App(layout="grid")
#box = Box(app,layout="grid", width="fill", height="fill")
red = Text(app, bg="red", grid=[5,0], text='red')
blue = Text(app, bg="blue", grid=[5,1], text = 'blue')
green = Text(app, bg="green", grid=[1,4], text = 'green')
white = Text(app, bg="white", grid=[7,6], text = 'white')
app.display()

# The learning point is that if there are missing items, the objects to the right and below are shuffled across or up
