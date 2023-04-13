from tkinter import *
from random import shuffle
from tkinter import messagebox


def app_exit():
    win.destroy()


def win_clear():
    # Очистка фрейма окна

    for child in frame_content.winfo_children():
        child.destroy()
    frame_content.forget()
    win.update()


def res_update(k):
    # Суммирование очков

    if 'points' in glbl_var:
        glbl_var['points'] += k
    else:
        glbl_var['points'] = k
    # Обновление файла с результатами
    try:
        # Чтение очков из файла
        with open('data/points.txt', 'r') as f:
            s = f.readlines()
            if s:
                last_res = int(s[0])
        # Запись очков в файл
        with open('data/points.txt', 'w') as f:
            f.write(str(glbl_var["points"]))
    except Exception as error:
        messagebox.showinfo('Ошибка чтения/записи файла', error)


def res_show():
    # Чтение и вывод результатов

    win_clear()  # очистка окна
    try:
        with open('data/points.txt', 'r') as f:
            last_res = f.readline()

        lbl_res = Label(frame_content, text=f'Общая сумма очков: {last_res}',
                        font="Calibri 14", bg="#cff4fc")
        btn_res = Button(frame_content, text='Удалить результаты',
                         font="Calibri 15", bg="#f8d7da", width=20,
                         relief=GROOVE, command=res_clear)
        lbl_res.pack()
        btn_res.pack(pady=10)
        frame_content.pack()
        # frame_content.pack(fill=X, expand=True)
    except Exception as error:
        messagebox.showinfo('Ошибка чтения файла', error)


def res_clear():
    # Удаление результатов

    glbl_var['points'] = 0

    with open('data/points.txt', 'w') as f:
        f.write(str(glbl_var["points"]))
    res_show()  # обновление виджетов результатов


def numbers_menu_click(level):
    # Запуск игры Числа

    win_clear()  # очистка окна

    glbl_var['lvl'] = level
    label1 = Label(frame_content, font="Calibri 14", bg="#cff4fc",
                   text="Будут показаны числа\n Ваша задача запомнить их расположение в порядке возрастания,\n и нажать на них в этом порядке.")
    btn = Button(frame_content, text='Начать', font="Calibri 15", width=12,
                 bg="#f8d7da", relief=GROOVE, command=numbers_run)
    label1.pack()
    btn.pack(pady=10)

    frame_content.pack(fill=X, expand=True)


def numbers_run():
    # Установка лимита на кол-во слов
    if glbl_var['lvl'] == 1:
        loop = 6
    elif glbl_var['lvl'] == 2:
        loop = 9
    else:
        loop = 12
    numbers_var["loop"] = loop
    numbers_var["sub_lvl"] = glbl_var["lvl"]  # стартовый уровень игры
    numbers_field()


def numbers_field():
    # Создание поля

    win_clear()  # очистка окна

    a = [f'{j}-{i}' for j in range(6) for i in range(6)]
    shuffle(a)
    a = a[:numbers_var["sub_lvl"] + 3]

    for x in range(6):
        for y in range(6):
            if f'{x}-{y}' in a:
                b = a.index(f'{x}-{y}') + 1
                btn = Button(frame_content, text=a.index(f'{x}-{y}') + 1,
                             bg="violet", font="Calibri 16 bold", width=6,
                             height=2)
                btn.config(command=lambda params=(btn, b): numbers_btn_click(params))
                btn.grid(row=x, column=y)
            else:
                b = 'no'
                btn = Button(frame_content, bg='lavender',
                             font="Calibri 16 bold", width=6, height=2)
                btn.config(command=lambda params=(btn, b): numbers_btn_click(params))
                btn.grid(row=x, column=y)
    frame_content.pack(expand=True)
    win.update()


def numbers_btn_click(params):
    # Обработка нажатия кнопок поля

    button, b = params
    numbers_var['count'] += 1
    if b == numbers_var['count']:
        button.config(bg='lavender')
        if numbers_var['count'] == numbers_var["loop"]:
            win_clear()
            numbers_var['count'] = 0
            res_update(glbl_var['lvl'] * 3)
            lbl = Label(frame_content, text='Поздравляем, Вы выиграли!',
                        font="Calibri 14 bold", bg="#cff4fc", fg="#dc3545")
            lbl.pack()
            mess = Label(frame_content, font="Calibri 16 bold", bg="#cff4fc",
                         text=f'Заработанные очки: {glbl_var["lvl"] * 3}')
            mess.pack(side=TOP, pady=10)
            restart_btn = Button(frame_content, text='Играть снова',
                                 font="Calibri 15", width=20, bg="#f8d7da",
                                 relief=GROOVE, command=numbers_run)
            restart_btn.pack(pady=10)
            frame_content.pack()
            # frame_content.pack(fill=X, expand=True)
        if numbers_var['count'] == numbers_var["sub_lvl"] + 3:
            numbers_var['count'] = 0
            numbers_var["sub_lvl"] += 1
            numbers_field()
        if numbers_var['count'] == 1:
            for btn in frame_content.winfo_children():
                btn.config(text='')
    else:
        win_clear()  # очистка
        numbers_var['count'] = 0
        label = Label(frame_content, text='Вы проиграли', bg="#cff4fc",
                      font="Calibri 14 bold")
        label.pack()
        restart_btn = Button(frame_content, text='Играть снова',
                             font="Calibri 15", width=20, bg="#f8d7da",
                             relief=GROOVE, command=numbers_run)
        restart_btn.pack(pady=10)
        frame_content.pack(fill=X, expand=True)


glbl_var = {}  # общие параметры игры (уровень, результаты)
numbers_var = {'count': 0}  # параметры для блока Числа

# Создание окна приложения
win = Tk()
win.title("MemoGame")
win.geometry("650x500")
win.configure(bg="#cff4fc")

# Создание фрейма для виджетов
frame_content = Frame(win, bg="#cff4fc")

# Создание главного меню
main_menu = Menu(font="Calibri 14")

# Создание подменю для Чисел
num_menu = Menu(font=("Calibri", 12), tearoff=0,
                activebackground='pink', activeforeground='brown')
num_menu.add_command(label="Уровень 1", command=lambda: numbers_menu_click(1))
num_menu.add_command(label="Уровень 2", command=lambda: numbers_menu_click(2))
num_menu.add_command(label="Уровень 3", command=lambda: numbers_menu_click(3))

# Создание пунктов главного меню
main_menu.add_cascade(label="Числа", menu=num_menu)
main_menu.add_separator()
main_menu.add_command(label="Результат", command=res_show)
main_menu.add_separator()
main_menu.add_command(label="Выход", command=app_exit)

# Добавление главного меню в окно программы
win.config(menu=main_menu)

win.mainloop()
