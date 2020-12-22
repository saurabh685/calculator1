from tkinter import*
def buttonclick(numbers):
    global operator
    operator= operator+str(numbers)
    textinput.set(operator)
def buttonclear():
    global operator
    operator=""
    textinput.set(operator)
def buttonequal():
    global operator
    z=str(eval(operator))
    textinput.set(z)
x=Tk()
x.title("calculator")
operator=""
textinput=StringVar()
DISPLAY=Entry(x,font=("Times New Roman",25,"bold"),textvariable=textinput,bd=30,insertwidth=4,
              bg="white",justify="right").grid(columnspan=4)
button1=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="1",command=lambda:buttonclick(1)).grid(row=1,column=0)
button2=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="2",command=lambda:buttonclick(2)).grid(row=1,column=1)
button3=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="3",command=lambda:buttonclick(3)).grid(row=1,column=2)
add=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold")
           ,text="+",command=lambda:buttonclick("+")).grid(row=1,column=3)

button4=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="4",command=lambda:buttonclick(4)).grid(row=2,column=0)
button5=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="5",command=lambda:buttonclick(5)).grid(row=2,column=1)
button6=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="6",command=lambda:buttonclick(6)).grid(row=2,column=2)
sub=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="-",command=lambda:buttonclick("-")).grid(row=2,column=3)

button7=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="7",command=lambda:buttonclick(7)).grid(row=3,column=0)
button8=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="8",command=lambda:buttonclick(8)).grid(row=3,column=1)
button9=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="9",command=lambda:buttonclick(9)).grid(row=3,column=2)
multi=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="*",command=lambda:buttonclick("*")).grid(row=3,column=3)

button0=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="0",command=lambda:buttonclick(0)).grid(row=4,column=0)
clear=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="C",command=buttonclear).grid(row=4,column=1)

equal=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="=",command=buttonequal).grid(row=4,column=2)
div=Button(x,padx=15,bd=7,fg="black",font=("Times New Roman",25,"bold"),
               text="/",command=lambda:buttonclick("/")).grid(row=4,column=3)
x.mainloop()






