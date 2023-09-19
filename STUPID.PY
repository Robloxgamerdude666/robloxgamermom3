import turtle as trtl
W = float(input("RECTANGLE WIDTH"))
Y = float(input("retangle hith"))
painter = trtl.Turtle()

painter.forward(W)
painter.right(90)
painter.forward(Y)
painter.right(90)
painter.forward(W)
painter.right(90)
painter.forward(Y)
 
wn = trtl.Screen()
wn.mainloop()
