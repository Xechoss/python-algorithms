import turtle
import time
turtle.pensize(10)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.begin_fill()
for _ in range(5):
    turtle.forward(300)
    turtle.right(144)
turtle.end_fill()
time.sleep(2)
turtle.penup()
turtle.goto(-150, -120)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))
turtle.mainloop()
