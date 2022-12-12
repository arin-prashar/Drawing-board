import turtle
import random as rd

turtle.setup(400, 500)                # Determine the window size
wn = turtle.Screen()                  # Get a reference to the window
wn.title("Handling keypresses!")      # Change the window title
wn.bgcolor("Cyan")              # Set the background color
tess = turtle.Turtle()                # Create our favorite turtle
tess.pensize(3)
crlr=["red","black","blue","green",'yellow','purple']
# The next four functions are our "event handlers".
def clr():
    tess.clear()
def color():
    tess.pencolor(crlr[rd.randint(0,6)])
def h():
    tess.penup()
def hm():
    tess.pendown()
def h1():
    tess.forward(30)
def h2():
    tess.left(45)
def h3():
    tess.right(45)
def h4():
    tess.backward(30)
def h5():
    wn.bye()                # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h, "0")
wn.onkey(hm, "/")
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4,"Down")
wn.onkey(clr, "w")
wn.onkey(color, ".")
wn.onkey(h5, "q")
wn.listen()                      # Listen for events
wn.mainloop()

