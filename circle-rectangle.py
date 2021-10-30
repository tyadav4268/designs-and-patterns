import turtle 

Narren = turtle.Turtle()
Narren.speed(40)
def square ():
  Narren.color('green')  
  Narren.forward(100)
  Narren.right(90)
  Narren.forward(100)
  Narren.right(90)
  Narren.forward(100)
  Narren.right(90)
  Narren.forward(100)
  Narren.right(100)
  
def flower () :
  Narren.color('red')
  Narren.circle(50) 
for DrawPattern in range (100):
  square()
  flower()
