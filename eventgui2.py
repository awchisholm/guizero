from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_go_clicked():
    info("Greetings","Hello, " + txt_name.value)

def btn_go2_clicked():
    info("Greetings","Hello, " + txt_name.value + " " + animal_name.value)

# Your GUI widgets go here
lbl_name = Text(app, text="Hello. What's your name?") # this is the first text box asking for your name
txt_name = TextBox(app)  # this is an empty box where you can enter your name
lbl_animal = Text(app, text="Hello. What's your animal?") 
animal_name = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text="Done")  # this is the Done button - when you press it the function is called
btn_go2 = PushButton(app, command=btn_go2_clicked, text="Done")  # this is the Done button - when you press it the function is called

# Show the GUI on the screen
app.display()
