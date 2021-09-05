from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_go_clicked():
    # This is called when the button is pressed
    # The function uses whatever has been entered into the box
    # and this is txt_name.value 
    # The info function brings up a dialog box
    info("Greetings","Hello, " + txt_name.value + " - I hope you're having a nice day")

# Your GUI widgets go here
lbl_name = Text(app, text="Hello. What's your name?") # this is the first text box asking for your name
txt_name = TextBox(app)  # this is an empty box where you can enter your name
btn_go = PushButton(app, command=btn_go_clicked, text="Done")  # this is the Done button - when you press it the function is called

# Show the GUI on the screen
app.display()
