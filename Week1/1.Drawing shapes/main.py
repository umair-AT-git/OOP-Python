from shapes import Rectangle, Paper, Oval, Triangle

#creating instance of rectangle
rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")

#invoking draw method
rect1.draw()
# Paper.display()

# Challenge Rectangle
rect2 = Rectangle()
rect2.set_x(100)
rect2.set_y(100)
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")

#Challenge Oval

oval1 = Oval(100,100)
oval1.randomize()
oval1.draw()

rect2.draw()

# Challenge Triangle

tri1 = Triangle(5,5,100,5,100,200)
tri1.set_color("green")
tri1.draw()

Paper.display()