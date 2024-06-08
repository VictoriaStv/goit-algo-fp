import turtle
from prompt_toolkit.shortcuts import button_dialog, input_dialog
from prompt_toolkit.styles import Style

styles = Style.from_dict({
    'dialog':             'bg:#E7EEF3',
    'dialog frame.label': 'bg:#C4EEE1 #999',
    'dialog.body':        'bg:#F5F5F5 #C4EEE1',
    'dialog shadow':      'bg:#999',
})

def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return

    # Намалювати основну гілку
    turtle.forward(branch_length)

    # Зберегти поточне положення та напрямок черепашки
    pos = turtle.position()
    heading = turtle.heading()

    # Намалювати праве піддерево
    turtle.right(45)
    draw_pythagoras_tree(branch_length * 0.707, level - 1)  

    # Відновити положення та напрямок черепашки
    turtle.setposition(pos)
    turtle.setheading(heading)

    # Намалювати ліве піддерево
    turtle.left(45)
    draw_pythagoras_tree(branch_length * 0.707, level - 1)

    # Відновити положення та напрямок черепашки
    turtle.setposition(pos)
    turtle.setheading(heading)

    # Повернутися до початкової позиції
    turtle.backward(branch_length)

def main():
    while True:
        # Показати головне меню
        result = button_dialog(
            title='Дерево Піфагора',
            text='Вітаємо у програмі для побудови дерева Піфагора! Оберіть дію:',
            buttons=[
                ('Побудувати дерево', 1),
                ('Вийти', 2),
            ],
            style=styles
        ).run()

        if result == 1:
            # Запитати у користувача рівень рекурсії
            level_str = input_dialog(
                title='Рівень рекурсії',
                text='Введіть рівень рекурсії (рекомендований діапазон: 1-7):',
                style=styles
            ).run()

            if level_str is None:
                continue  
            try:
                level = int(level_str)
            except ValueError:
                print("Неправильне значення, спробуйте ще раз.")
                continue

            turtle.reset()
            turtle.speed(0) 
            turtle.left(90)  

            # Намалювати дерево Піфагора
            draw_pythagoras_tree(100, level)

            # Завершити малювання
            turtle.done()

            # Після закриття вікна вихід з програми
            print("Дякуємо за використання програми!")
            break
        elif result == 2:
            # Вихід з програми
            print("Дякуємо за використання програми!")
            break

if __name__ == "__main__":
    main()

