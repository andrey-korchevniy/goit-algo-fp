import turtle
import math

def draw_pythagoras_tree(t, length, depth):
    if depth == 0:
        t.forward(length)
        t.backward(length)
        return

    # Малюємо стовбур
    t.forward(length)

    # Малюємо праву гілку
    t.right(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)
    t.left(45)

    # Малюємо ліву гілку
    t.left(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)
    t.right(45)

    # Повертаємось до початкової позиції
    t.backward(length)

def screen():
    # Налаштування екрану
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed(0)  # Set the speed to the maximum
    t.left(90)  # Point the turtle upwards

    # Запит на введення глибини
    recursion_depth = int(input("Enter the recursion depth: "))

    # Малювання дерева
    draw_pythagoras_tree(t, 100, recursion_depth)

    # Закінчення
    t.hideturtle()
    turtle.done()

screen()