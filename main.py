import turtle
from turtle import Turtle, Screen
import random
import colorgram

turtle.colormode(255)
my_turtle = Turtle()
my_turtle.speed(10)


# draw_spirograph(5)
# colors = colorgram.extract("my_pic.jpg", 30)
rgb_list = [(208, 160, 111), (188, 168, 17), (32, 105, 142), (173, 82, 29), (13, 51, 84), (142, 174, 195),
            (217, 209, 123), (158, 23, 13), (195, 142, 157), (144, 68, 102), (94, 161, 80), (137, 177, 149),
            (50, 54, 90), (216, 171, 181), (47, 155, 187), (128, 35, 42), (96, 36, 15), (72, 22, 38), (180, 90, 118),
            (4, 102, 55), (1, 84, 111), (69, 79, 20), (225, 173, 171), (189, 78, 71), (18, 131, 75), (235, 205, 5)]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
# print(rgb_list)

# color_list = ["red", "blue", "green"]
my_turtle.penup()
my_turtle.setpos((-250, -250))
my_turtle.hideturtle()


def printing_lines():
    for _ in range(10):
        my_turtle.dot(15, random.choice(rgb_list))
        my_turtle.fd(50)


printing_lines()
my_turtle.setpos(-250, -200)
printing_lines()
my_turtle.setpos(-250, -150)
printing_lines()
my_turtle.setpos(-250, -100)
printing_lines()
my_turtle.setpos(-250, -50)
printing_lines()
my_turtle.setpos(-250, 0)
printing_lines()
my_turtle.setpos(-250, 50)
printing_lines()
my_turtle.setpos(-250, 100)
printing_lines()
my_turtle.setpos(-250, 150)
printing_lines()
my_turtle.setpos(-250, 200)
printing_lines()



screen = Screen()
screen.exitonclick()
