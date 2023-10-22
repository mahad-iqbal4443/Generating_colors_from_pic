import turtle
from turtle import Turtle, Screen
import random
import colorgram

turtle.colormode(255)
my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("Khaki4")
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)


# Drawing a Dashed line
# for _ in range(15):
#     turtle.fo![](../../OneDrive/Desktop/my_pic.jpg)forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()


# # Drawing Shapes of different colors
# for _ in range(3):
#     my_turtle.pencolor("PapayaWhip")
#     my_turtle.forward(100)
#     my_turtle.right(120)
# for _ in range(4):
#     my_turtle.pencolor("PaleGreen")
#     my_turtle.forward(100)
#     my_turtle.right(90)
# for _ in range(5):
#     my_turtle.pencolor("LightSteelBlue2")
#     my_turtle.forward(100)
#     my_turtle.right(72)
# for _ in range(6):
#     my_turtle.pencolor("MediumPurple1")
#     my_turtle.forward(100)
#     my_turtle.right(60)
# for _ in range(7):
#     my_turtle.pencolor("NavajoWhite")
#     my_turtle.forward(100)
#     my_turtle.right(51.428)
# for _ in range(8):
#     my_turtle.pencolor("snow4")
#     my_turtle.forward(100)
#     my_turtle.right(45)
# for _ in range(9):
#     my_turtle.pencolor("thistle3")
#     my_turtle.forward(100)
#     my_turtle.right(40)
# for _ in range(10):
#     my_turtle.pencolor("RosyBrown2")
#     my_turtle.forward(100)
#     my_turtle.right(36)
# colors = ["maroon", "thistle3", "snow4", "wheat", "violet", "tan", "snow", "salmon"]

# Drawing 8 shapes with functions
# def shapes(siz):
#     angle = 360 / siz
#     my_turtle.color(random.choice(colors))
#     for _ in range(siz):
#         my_turtle.forward(100)
#         my_turtle.left(angle)
#
#
# def size():
#     for new in range(3, 11):
#         shapes(new)
# size()

# random colors with random movement
# def random_color():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     color_tuple = (r, b, g)
#     return color_tuple


my_turtle.speed(10)
# my_turtle.width(10)
# moves = [0, 90, 180, 270]
#
# for _ in range(100):
#     my_turtle.color(random_color())
#     my_turtle.forward(30)
#     my_turtle.seth(random.choice(moves))

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         my_turtle.color(random_color())
#         my_turtle.speed(100)
#         my_turtle.circle(120)
#         my_turtle.seth(my_turtle.heading() + size_of_gap)


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
