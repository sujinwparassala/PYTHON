import tkinter
from tkinter import *
root=tkinter.Tk()

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set("")

def equels():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

operator=""
text_input=StringVar()
root.title("first project")
root.iconbitmap("face.png")
root.geometry("380x500")
root.configure(bg="powder blue")
txtDisplay=Entry(root,font=('arial',20,'bold'),textvariable=text_input,bd=20,insertwidth=4,justify='right').grid(columnspan=3)
#btn1=Button(root,padx=5,pady=5,bd=5,fg='blue',font=('arial',10,'bold'),text="1").grid(column=0,row=3)
#btn2=Button(root,text="2",fg='blue',font=10,bd=5).grid(column=0,row=3)


button1 = Button(root, text=' 1', fg='black', bg='red',height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(1))
button1.grid(row=1, column=0)
button2 = Button(root, text=' 2 ', fg='black', bg='red',height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(2))
button2.grid(row=1, column=1)

button3 = Button(root, text=' 3 ', fg='black', bg='red',height=3,width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(3))
button3.grid(row=1, column=2)

button4 = Button(root, text=' 4 ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(4))
button4.grid(row=2, column=0)


button5 = Button(root, text=' 5 ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(5))
button5.grid(row=2, column=1)

button6 = Button(root, text=' 6 ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(6))
button6.grid(row=2, column=2)

button7 = Button(root, text=' 7 ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(7))
button7.grid(row=3, column=0)

button8 = Button(root, text=' 8 ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(8))
button8.grid(row=3, column=1)

button9 = Button(root, text=' 9 ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(9))
button9.grid(row=3, column=2)

button0 = Button(root, text=' 0 ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick(0))
button0.grid(row=4, column=0)

button_add = Button(root, text=' +', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick('+'))
button_add.grid(row=4, column=1)

button_sub = Button(root, text=' - ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick('-'))
button_sub.grid(row=4, column=2)

button_mul = Button(root, text=' *', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick('*'))
button_mul.grid(row=5, column=0)

button_div = Button(root, text=' / ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick('/'))
button_div.grid(row=5, column=1)

button_pont = Button(root, text=' . ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=lambda:btnClick('.'))
button_pont.grid(row=5, column=2)

button_del = Button(root, text=' DEL ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd=5,command=btnClear)
button_del.grid(row=5, column=2)


button_per = Button(root, text=' % ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd='5',command=lambda:btnClick('%'))
button_per.grid(row=6, column=0)

button_eql = Button(root, text=' = ', fg='black', bg='red', height=3, width=8,font=('arial',10,'bold'),bd='5',command=equels)
button_eql.grid(row=6, column=1)





root.mainloop()
