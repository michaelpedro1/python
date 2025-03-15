import turtle
pen=turtle.Turtle()
pen.fillcolor('blue')
pen.begin_fill()
for _ in range(4):
  pen.forward(100)
  pen.right(90)
pen.end_fill()  
turtle.done() 

pen.penup()
pen.goto(-20, -150)
pen.pendown()

pen.fillcolor('green')
pen.begin_fill()
for _ in range(2):
  pen.forward(200)
  pen.right(90)
  pen.forward(50)
  pen.right(90)
  
pen.end_fill()  
pen.penup()
pen.goto(20, 30)
pen.pendown()
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(80)
pen.end_fill()

pen.penup()
pen.goto(-10, 130)
pen.pendown()
pen.fillcolor('black')
pen.begin_fill()
pen.circle(5)
pen.end_fill()

pen.penup()
pen.goto(60, 130)
pen.pendown()
pen.fillcolor('black')
pen.begin_fill()
pen.circle(5)
pen.end_fill()


pen.penup()
pen.goto(10, 80)
pen.pendown()
pen.fillcolor('red')
pen.begin_fill()
for _ in range(3):
  pen.forward(40)
  pen.right(120)
pen.end_fill()  