from tkinter import *
#mainwindow conatining the calculator
cal = Tk()
cal.title("Calculator")
operator=""
#text input containing the numbers which are input
text_input = StringVar()
txtDisplay = Entry(cal,font=('arial',20,'bold'),textvariable=text_input,insertwidth=4,bg='powderblue',justify='right',bd=30)
txtDisplay.grid(columnspan=4)
#calculator buttons
btn7 = Button(cal,padx=16,pady=20,bd=8,text='7',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=1,column=0)
btn8 = Button(cal,padx=16,pady=20,bd=8,text='8',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=1,column=1)
btn9 = Button(cal,padx=16,pady=20,bd=8,text='9',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=1,column=2)
Addition = Button(cal,padx=16,pady=20,bd=8,text='+',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=1,column=3)

#next row of buttons
btn4 = Button(cal,padx=16,pady=20,bd=8,text='4',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=2,column=0)
btn5 = Button(cal,padx=16,pady=20,bd=8,text='5',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=2,column=1)
btn6 = Button(cal,padx=16,pady=20,bd=8,text='6',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=2,column=2)
Subtraction = Button(cal,padx=16,pady=20,bd=8,text='-',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=2,column=3)

#next row of buttons
btn1 = Button(cal,padx=16,pady=20,bd=8,text='1',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=3,column=0)
btn2 = Button(cal,padx=16,pady=20,bd=8,text='2',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=3,column=1)
btn3 = Button(cal,padx=16,pady=20,bd=8,text='3',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=3,column=2)
Multiplication = Button(cal,padx=16,pady=20,bd=8,text='*',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=3,column=3)

#next row of buttons
btn0 = Button(cal,padx=16,pady=20,bd=8,text='0',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=4,column=0)
btnClear = Button(cal,padx=16,pady=20,bd=8,text='C',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=4,column=1)
btnEquals = Button(cal,padx=16,pady=20,bd=8,text='=',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=4,column=2)
Division = Button(cal,padx=16,pady=20,bd=8,text='/',fg='black',bg='powderblue',font=('arial',20,'bold'),).grid(row=4,column=3)



#to open the screen until program is not closed
cal.mainloop()