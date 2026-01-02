"""
Завдання 2. Рекурсія. Створення фрактала "дерево Піфагора" за допомогою рекурсії
"""
import turtle


def draw_pythagoras_tree(t: turtle.Turtle, branch_length: float, level: int, angle: float = 45) -> None:
    if level == 0:
        return

    t.forward(branch_length)
    
    pos = t.position()
    heading = t.heading()
    
    # Ліва гілка
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1, angle)
    
    # Повертаємося до початкової позиції
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()
    
    # Права гілка
    t.right(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1, angle)
    
    # Повертаємося до початкової позиції
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()


def main():
    level = int(input("Введіть рівень рекурсії (рекомендовано 5-12): "))
    
    screen = turtle.Screen()
    screen.title(f"Дерево Піфагора (рівень {level})")
    screen.bgcolor("white")
    screen.colormode(255)
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()
    
    draw_pythagoras_tree(t, 120, level)    
    screen.mainloop()

if __name__ == "__main__":
    main()

