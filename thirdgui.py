from guizero import App, Text
app = App(title="This is my first GUI")

firstmessage = Text(app, text="This is big text")
secondmessage = Text(app, text="This is green")
thirdmessage = Text(app, text = "message 3")

firstmessage.text_size=40
secondmessage.bg = "green"
thirdmessage.color="red"
thirdmessage.font="Courier"
app.display()
