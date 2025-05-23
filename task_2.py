# Завдання 2
import turtle

# функція малює лише одну сторону сніжинки 
# Визначає рекурсивну функцію для побудови однієї сторони кривої Коха.

# t — об'єкт Turtle.
# order — рівень рекурсії.
# size — довжина поточної лінії.



def koch_curve(t, order, size):
    # Якщо досягнуто 0 рівня рекурсії, малюється пряма лінія довжиною size.
    if order == 0:
        t.forward(size)
    # Інакше, розбиваємо лінію на 4 частини:
    # Малюємо першу третину.
    # Повертаємось на 60° вліво.
    # Малюємо другу третину.
    # Повертаємось на -120°.
    # Малюємо третю третину.
    # Повертаємось на 60°.
    # Малюємо останню третину.
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

# Функція для побудови сніжинки
def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)  # максимальна швидкість малювання
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):  # малюємо 3 сторони сніжинки
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    window.mainloop()

# Отримуємо рівень рекурсії від користувача
try:
    user_order = int(input("Введіть рівень рекурсії (наприклад, 0–5): "))
    if user_order < 0:
        print("Будь ласка, введіть невід’ємне число.")
    else:
        draw_koch_snowflake(user_order)
except ValueError:
    print("Будь ласка, введіть ціле число.")
