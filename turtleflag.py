import turtle

turtle.colormode(1.0)

colordict = {"blue": (60/255, 59/255, 110/255), "white": (1, 1, 1),
             "red": (178/255, 34/255, 52/255), "dkblue" : (0.164, 0.219, 0.56),
             "ltblue" : (0.07, 0.5, 0.72), "yellow": (0.9, 0.95, 0.019),
             "black" : (0, 0, 0)}

def get_color(color: str):
    global colordict
    if color in colordict.keys():
        return colordict[color]
    else:
        return (0, 0, 0)


def draw_rectangle(x, y, length, height, col):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.color(get_color(col))
    turtle.begin_fill()
    turtle.goto(x + length, y)
    turtle.goto(x + length, y- height)
    turtle.goto(x, y - height)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_star(x, y, diameter, col):
    x = x + (diameter/6)
    y = y + (diameter/6)
    z = diameter /2.5
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.color(get_color(col))
    turtle.begin_fill()
    for arm in range(5):
        turtle.forward(z)
        turtle.right(144)
        turtle.forward(z)
        turtle.left(72)
    turtle.end_fill()

def draw_flag(x, y, height):
    stripes(x, y, height)
    starfield(x, y, height)

def stripes(x, y, height):
    sy = height / 13
    sx = height * 1.9
    for yoffset in range(0, 13):
        if yoffset % 2 == 0:
            draw_rectangle(x, y - (yoffset*sy), sx, sy, "red")
        else:
            draw_rectangle(x, y - (yoffset* sy), sx, sy,"white")

def starfield(x, y, height):
    xs = height * 0.76
    ys = height * 0.5385
    draw_rectangle(x, y, xs, ys, "blue")

    xgap = xs / 12
    ygap = ys / 10
    diam = height * 0.0616
    for i in range(9):
        if i%2 == 0:
            for j in range(6):
                draw_star(x + xgap + (2 * j * xgap),
                          y - ygap - (i * ygap) , diam, "white")
            
        else:
            for j in range(1, 6):
                draw_star(x + (2 * j * xgap),
                          y - ygap - (i * ygap) , diam, "white")

    


if __name__ == "__main__":
    turtle.speed(0)
    turtle.tracer(1000, 10)
    turtle.hideturtle()
    from random import randint
    for x in range(200):
        draw_flag(randint(-400, 400), randint(-400, 400), randint(-100, 500))







