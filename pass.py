from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_check():
	password1 = pass1.value
	password2 = pass2.value
	if password1 == password2:
		info("Information", "Passwords the same")
	else:
		info("Information", "Passwords different")


# Your GUI widgets go here
lbl_name = Text(app, text="Enter your password twice") 

pass1 = TextBox(app, hide_text=True)
pass2 = TextBox(app, hide_text=True)
btn_go = PushButton(app, command=btn_check, text="Check")

# Show the GUI on the screen
app.display()
