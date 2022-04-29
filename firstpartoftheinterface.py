import tkinter as tk

#def help1():


#def spravka():

window = tk.Tk()
window.title("Приложение")
window.geometry("500x500")


label = tk.Label(text = "Приложение для получения информации об акциях",
                 font = 'Arial 15', bg = 'thistle3', bd = '13.6', relief = 'sunken')
label.pack(side='top')

btnLeftDown = tk.Button(window, text = "Помощь",
                        padx='16', pady='10', font='Arial 15')
btnLeftDown.place(relx=0.15, rely=0.75)

btnRightDown = tk.Button(window, text = "Справка",
                        padx='16', pady='10', font='Arial 15')
btnRightDown.place(relx=0.60, rely=0.75)

label1 = tk.Label(text = "Введите тикер акции",
                  font = 'Arial 13', bd = '13.6')
label1.place(relx=0.31, rely=0.27)

entry = tk.Entry(window, font = 'Arial 13', bd = '5', relief = 'sunken' )
entry.place(relx=0.31, rely=0.35)

btnMiddle = tk.Button(window, text = "Поиск",
                      padx='5', pady='3', font='Arial 10')
btnMiddle.place(relx=0.44, rely=0.425)

window.mainloop()
