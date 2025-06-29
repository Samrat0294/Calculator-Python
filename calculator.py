from tkinter import *
root = Tk()

first_no = second_no =operator= None

def get_digit(digit):
    current=result_label["text"]
    new = current+ str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")

def get_operator(op):
    global first_no,operator
    first_no=int(result_label["text"])
    operator=op
    result_label.config(text="")

def get_result():
    global first_no,second_no,operator
    second_no=int(result_label["text"])

    if operator=="+":
        result_label.config(text=str(first_no +second_no))
    elif operator=="-":
        result_label.config(text=str(first_no-second_no))
    elif operator=="*":
        result_label.config(text=str(first_no*second_no))
    else:
        if second_no==0:
            result_label.config(text="Error")
        else:
            result_label.config(text=str(round(first_no/second_no,4)))

root.geometry("300x340")
root.title("Calculator")
root.resizable(0,0)
root.configure(background="grey")

result_label = Label(root, text="", fg="black", bg="grey")
result_label.grid(column=0,columnspan=10, row=0,pady=(50,25),sticky="w")

result_label.config(font=("verdana", 30,"bold"))

# for button 7
btn7 = Button(root, text="7", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(7))
btn7.grid(column=0, row=1)
btn7.config(font=("verdana", 9))

# for button 8
btn8 = Button(root, text="8", fg="black", bg="#00a65a",width=5,height=3 , command=lambda:get_digit(8))
btn8.grid(column=1, row=1)
btn8.config(font=("verdana", 9))

# for button 9
btn9 = Button(root, text="9", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(9))
btn9.grid(column=2, row=1)
btn9.config(font=("verdana", 9))

# for button add
btn_add = Button(root, text="+", fg="black", bg="#00a65a",width=5,height=3,command=lambda:get_operator("+"))
btn_add.grid(column=3, row=1)
btn_add.config(font=("verdana", 9))

# for button sin
btn_sin = Button(root, text="sin", fg="black", bg="#00a65a",width=12,height=3)
btn_sin.grid(column=4, row=1)
btn_sin.config(font=("verdana", 9))

# for button 4
btn4 = Button(root, text="4", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(4))
btn4.grid(column=0, row=2)
btn4.config(font=("verdana", 9))

# for button 5
btn5 = Button(root, text="5", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(5))
btn5.grid(column=1, row=2)
btn5.config(font=("verdana", 9))

# for button 6
btn6 = Button(root, text="6", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(6))
btn6.grid(column=2, row=2)
btn6.config(font=("verdana", 9))

# for button sub
btn_sub = Button(root, text="-", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_operator("-"))
btn_sub.grid(column=3, row=2)
btn_sub.config(font=("verdana", 9))

# for button cos
btn_cos = Button(root, text="cos", fg="black", bg="#00a65a",width=12,height=3, command=lambda:get_digit(cos))
btn_cos.grid(column=4, row=2)
btn_cos.config(font=("verdana", 9))


# for button 1
btn1 = Button(root, text="1", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(1))
btn1.grid(column=0, row=3)
btn1.config(font=("verdana", 9))

# for button 2
btn2 = Button(root, text="2", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(2))
btn2.grid(column=1, row=3)
btn2.config(font=("verdana", 9))

# for button 3
btn3 = Button(root, text="3", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(3))
btn3.grid(column=2, row=3)
btn3.config(font=("verdana", 9))

# for button mul
btn_mul = Button(root, text="*", fg="black", bg="#00a65a",width=5,height=3,command=lambda:get_operator("*"))
btn_mul.grid(column=3, row=3)
btn_mul.config(font=("verdana", 9))

# for button div
btn_div = Button(root, text="/", fg="black", bg="#00a65a",width=5,height=3,command=lambda:get_operator("/"))
btn_div.grid(column=3, row=4)
btn_div.config(font=("verdana", 9))


# for button tan
btn_tan = Button(root, text="tan", fg="black", bg="#00a65a",width=12,height=3)
btn_tan.grid(column=4, row=3)
btn_tan.config(font=("verdana", 9))

# for button zero
btn_zero = Button(root, text="0", fg="black", bg="#00a65a",width=5,height=3, command=lambda:get_digit(0))
btn_zero.grid(column=2, row=4)
btn_zero.config(font=("verdana", 9))


# for button cancel
btn_clr = Button(root, text="C", fg="black", bg="#00a65a",width=12,height=3,command=lambda:clear())
btn_clr.grid(column=4, row=4)
btn_clr.config(font=("verdana", 9))

# for button equal
btn_eq = Button(root, text="=", fg="black", bg="#00a65a",width=11,height=3,command=lambda:get_result())
btn_eq.grid(column=0, row=4,columnspan=2)
btn_eq.config(font=("verdana", 9))

root.mainloop()