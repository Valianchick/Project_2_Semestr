import tkinter as tk


def quest2():
    root = tk.Tk()
    root.title("Что такое акция?")
    otvet2 = tk.Label(root, text="""Акция — это ценная бумага, которую выпускает акционерное общество,\n другими словами — компания-эмитент. Все инвесторы, которые купили акции,\n стали совладельцами компании. Акция как раз и подтверждает, что у ее владельца есть доля в компании, пусть даже совсем маленькая.""",
                      font="Arial 14")
    otvet2.pack()


def quest3():
    root = tk.Tk()
    root.title("Что такое тикер?")
    otvet3 = tk.Label(root, text="""Ти́кер — краткое название в биржевой информации котируемых инструментов.\n Является уникальным идентификатором в рамках одной биржи или информационной системы.\n Используется для того, чтобы постоянно не печатать в сводках полное наименование ценных бумаг или других объектов торговли.""",
                      font="Arial 14")
    otvet3.pack()


def quest4():
    root = tk.Tk()
    root.title("Что такое капитализация?")
    otvet4 = tk.Label(root, text="""Капитализация – произведение количества выпущенных акций\n на цену одной акции, сложившуюся на бирже.""",
                      font="Arial 14")
    otvet4.pack()


def quest5():
    root = tk.Tk()
    root.title("Что такое дивиденды?")
    otvet5 = tk.Label(root, text="""Дивиденды — часть прибыли компании, которая распределяется\n между акционерами пропорционально их доле ценных бумаг, чаще всего акций.""",
                      font="Arial 14")
    otvet5.pack()


def quest6():
    root = tk.Tk()
    root.title("Что такое объем торгов?")
    otvet6 = tk.Label(root, text="""Объём торгов на фондовом рассчитывается как суммарное число акций,\n сменивших владельца за торговый период.""",
                      font="Arial 14")
    otvet6.pack()


def help1():
    root = tk.Tk()
    root.title("Помощь")
    root.geometry("280x500+420+300")
    root.resizable(0, 0)

    question = tk.Label(root, text="Вопросы:",
                        font='Arial 16')
    question.grid(column=0, row=0)
    work = tk.Button(root, text="Как работает приложение?",
                     font='Arial 16')
    work.grid(column=0, row=1)

    share = tk.Button(root, text="Что такое акция?",
                      font='Arial 16',
                      command=quest2)
    share.grid(column=0, row=2)

    ticker = tk.Button(root, text="Что такое тикер?",
                       font='Arial 16',
                       command=quest3)
    ticker.grid(column=0, row=3)

    cap = tk.Button(root, text="Что такое капитализация?",
                    font='Arial 16',
                    command=quest4)
    cap.grid(column=0, row=4)

    div = tk.Button(root, text="Что такое дивиденды?",
                    font='Arial 16',
                    command=quest5)
    div.grid(column=0, row=5)

    ob = tk.Button(root, text="Что такое объем торгов?",
                   font='Arial 16',
                   command=quest6)
    ob.grid(column=0, row=6)


def spravka():
    root1 = tk.Tk()
    root1.title("Cправка")
    root1.geometry("500x500+1200+300")
    root1.resizable(0, 0)


window = tk.Tk()

window.title("Приложение")
window.geometry("500x500+700+300")
window.resizable(0, 0)
window['bg'] = 'blanchedalmond'

label = tk.Label(text="Приложение для получения информации об акциях",
                 font='Arial 15', bg='thistle3', bd='13.6', relief='sunken')
label.pack(side='top')

btnLeftDown = tk.Button(window, text="Помощь",
                        padx='16',
                        pady='10',
                        font='Arial 15',
                        command=help1)
btnLeftDown.place(relx=0.15, rely=0.75)

btnRightDown = tk.Button(window, text="Справка",
                         padx='16',
                         pady='10',
                         font='Arial 15',
                         command=spravka)
btnRightDown.place(relx=0.60, rely=0.75)

label1 = tk.Label(text="Введите тикер акции",
                  font='Arial 13',
                  bd='13.6')
label1.place(relx=0.31, rely=0.27)

entry = tk.Entry(window,
                 font='Arial 13',
                 bd='5',
                 relief='sunken')
entry.place(relx=0.31, rely=0.35)

btnMiddle = tk.Button(window, text="Поиск",
                      padx='5',
                      pady='3',
                      font='Arial 10')
btnMiddle.place(relx=0.44, rely=0.425)

window.mainloop()
