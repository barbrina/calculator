from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import font as tkFont

root = Tk()
root.iconbitmap('./img/calculator.ico')
box = Entry(root, width = 33, font = 'Arial 12')
add = ''
result = ''

root.title("Calculator")
box.grid(column=0,
       row = 0,
       columnspan = 4,
       ipady = 10,
       pady = 5,
       padx = 5
       )

def button_click(number):
        global add
        global result
        try:
            if number == 'AC':
                add = ''
                result = ''
            else:
                if number == '÷':
                    add += number
                    result += '/'
                elif number == '×':
                    add += number
                    result += '*'
                elif number == 'CE':
                    add = add[:-1]
                    result = result[:-1]
                elif number == '=':
                    add = str(eval(result))
                    result = add
                else:
                    result += number
                    add += number
        except:
            add = result = '0'
            box.delete(0, END)
            box.insert(0, add)
        finally:
            box.delete(0, END)
            box.insert(0, add)

class Calculator:

    def __init__(self, text, row, column):
        self.text = text
        self.row = row
        self.column = column

    def press(self):
        arial = tkFont.Font(family = 'Arial', size = 12)
        button = Button(root,
                        text = self.text,
                        bd = 2,
                        width = 7,
                        height = 3,
                        justify = CENTER,
                        font = arial,
                        command = lambda: button_click(self.text))
        return button.grid(row = self.row, column = self.column, pady = 2)

word = [['(', ')', 'CE', 'AC'],
        ['7', '8', '9', '÷'],
        ['4', '5', '6', '×'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+']]

for number, row in enumerate(word):
    for index, column in enumerate(row):
        matrix = Calculator(text = row[index], row = number + 1, column = index).press()

root.mainloop()

