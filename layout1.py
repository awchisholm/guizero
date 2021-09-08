from guizero import App, Text, Box
app = App()
box = Box(app,layout="grid", width="fill", height="fill")
red = Text(box, bg="red", grid=[5,0])
blue = Text(box, bg="blue", grid=[5,1])
green = Text(box, bg="green", grid=[1,4])
white = Text(box, bg="white", grid=[1,1])
app.display()

# The learning point is that if there are missing items, the objects to the right and below are shuffled across or up
