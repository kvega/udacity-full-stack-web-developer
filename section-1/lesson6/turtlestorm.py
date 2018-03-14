import turtle


def draw_square(some_turtle, edge):
    for _ in range(4):
        some_turtle.forward(edge)
        some_turtle.right(90)
        
def change_direction(some_turtle, angle):
    some_turtle.seth(angle)
    
def draw_turtles(num_of_squares=12, square_length=100):
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    phil = turtle.Turtle()
    phil.shape("turtle")
    phil.color("green")
    phil.speed(0)

    bill = turtle.Turtle()
    bill.shape("turtle")
    bill.color("blue")
    bill.speed(0)

    steve = turtle.Turtle()
    steve.shape("turtle")
    steve.color("red")
    steve.speed(0)

    turtles = [phil, bill, steve]
    angle = 0
    square_length = 100
    for some_turtle in turtles:
        angle = 0
    
        for i in range(num_of_squares+1):
            
            draw_square(some_turtle, square_length)
            change_direction(some_turtle, angle)
            angle = angle + int(360/num_of_squares)
            print(angle)
        square_length+=100
        
    window.exitonclick()

draw_turtles(72)
