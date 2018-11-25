from Button import Button

button1 = Button(18, "PULLUP")
button2 = Button(23, "PULLUP")
button3 = Button(24, "PULLUP")

while True:
    button1state = button1.isPressed()
    button2state = button2.isPressed()
    button3state = button3.isPressed()
    if(button1state):
        print("Button 1 Pressed")
    if(button2state):
        print("Button 2 Pressed")
    if(button3state):
        print("Button 3 Pressed")
