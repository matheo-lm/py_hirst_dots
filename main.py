import colorgram
import turtle as t
import random

########################################################################################################################
colors = colorgram.extract('image.jpg', 10)
colors_2 = colorgram.extract('image2.jpg', 10)
rgb_colors = []


def color_extract():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)
########################################################################################################################

t.colormode(255)
#color_list = [(126, 104, 97), (155, 140, 133), (157, 163, 169), (96, 104, 109), (34, 36, 43), (167, 160, 165),
#              (151, 161, 155), (115, 85, 89), (93, 103, 101), (150, 118, 111)]
color_list = [(123, 156, 210), (220, 145, 74), (251, 248, 240), (209, 72, 116), (93, 102, 203), (207, 124, 164),
              (73, 86, 161), (158, 60, 108), (178, 74, 38), (115, 186, 144)]


tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(220)
tim.forward(420)
tim.setheading(0)
number_of_dots = 101


def dots_10():
    for dot_count in range(1, number_of_dots):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

dots_10()

screen = t.Screen()
screen.exitonclick()