from tkinter import *
from chat import get_response

root = Tk()

root.title('Chat Bot')

root.geometry('400x450')
root.maxsize(400,450)
root.resizable(False,False)

head = Label(root, text ='CHAT BOT', font=("times new roman",20))

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff= False)


def clear():
    chatWindow.delete('1.0',END)


file_menu.add_command(label='New', command= clear)
file_menu.add_command(label='Exit', command= root.destroy)

menu_bar.add_cascade(label='File', menu=file_menu)
root.config(menu=menu_bar)


def send():
    send = "YOU:  "+ textbox.get()
    x = "BOT:  "+ get_response(send)
    chatWindow.insert(END, "\n"+send)
    chatWindow.insert(END, "\n"+x)
    chatWindow.insert(END, "\n")
    textbox.delete(0, END)
    textbox.insert(0,"")


chatWindow = Text(root, bd=1, bg='#3A3B3C', fg='white', width = 50, height = 8, font =("times new roman",15))
chatWindow.place(x=6, y=6, height=384, width=384)

textbox= Entry(root, width =100, bg='#D3D3D3')
send = Button(root, text="SEND", command=send).place(x=341, y=396, height=30, width=50)
textbox.place(x=6, y=396, height=30, width=355)

root.mainloop()
