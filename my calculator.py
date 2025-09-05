from tkinter import*
root= Tk()
root.title("my calculator")
root.config(bg="gold2")


def click(numbers):
    global operator
    operator = operator + str(numbers)
    a.set(operator)

operator=" "
def cancel():
    global operator
    operator = " "
    a.set(operator)
def equal():
    global operator
    operator = str(eval(operator))
    a.set(operator)
    



a=StringVar()
x=Entry(root,font="arial 20 bold",textvariable=a, bg="steel blue",fg="red",insertwidth=4,bd=28,justify=RIGHT).grid(columnspan=4)
btn7= Button(root,font="arial 20 bold", text="7", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(7)).grid(row=1,column=0)
btn8= Button(root,font="arial 20 bold", text="8", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(8)).grid(row=1,column=1)
btn9= Button(root,font="arial 20 bold", text="9", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(9)).grid(row=1,column=2)
btnpl= Button(root,font="arial 20 bold", text="+", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click("+")).grid(row=1,column=3)
btn4= Button(root,font="arial 20 bold", text="4", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(4)).grid(row=2,column=0)
btn5= Button(root,font="arial 20 bold", text="5", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click()).grid(row=2,column=1)
btn6= Button(root,font="arial 20 bold", text="6", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(6)).grid(row=2,column=2)
btnml= Button(root,font="arial 20 bold", text="*", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click("*")).grid(row=2,column=3)
btn1= Button(root,font="arial 20 bold", text="1", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(1)).grid(row=3,column=0)
btn2= Button(root,font="arial 20 bold", text="2", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(2)).grid(row=3,column=1)
btn3= Button(root,font="arial 20 bold", text="3", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(3)).grid(row=3,column=2)
btnms= Button(root,font="arial 20 bold", text="-", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click("-")).grid(row=3,column=3)
btn0= Button(root,font="arial 20 bold", text="0", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click(0)).grid(row=4,column=0)
btnC= Button(root,font="arial 20 bold", text="C", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=cancel).grid(row=4,column=1)
btneq= Button(root,font="arial 20 bold", text="=", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=equal).grid(row=4,column=2)
btndv= Button(root,font="arial 20 bold", text="/", bg="gold2", fg="red", bd=10, padx=16, pady=16,command=lambda:click("/")).grid(row=4,column=3)


root.mainloop()
