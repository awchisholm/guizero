from guizero import App, Text
app = App(title="This is my first GUI")

firstmessage = Text(app, text="This is big text")
secondmessage = Text(app, text="This is green")

firstmessage.text_size=40
secondmessage.bg = "green"
app.display()
