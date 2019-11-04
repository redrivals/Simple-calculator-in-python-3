#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *



    



def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnclear():
        global operator
        operator=""
        text_input.set("")

def btnequals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

    
    
cal= Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()
txtDisplay= Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=30,bg="powder blue",justify='right').grid(columnspan=4)

btn7=Button(cal,padx=16,pady=16,bd=8,fg="white",bg="Navy blue",font=('arial',20,'bold'),
           text="7",command=lambda:btnclick(7)).grid(row=1,column=1)
btn8=Button(cal,padx=16,pady=16,bd=8,fg="white",bg="Navy blue",font=('arial',20,'bold'),
           text="8",command=lambda:btnclick(8)).grid(row=1,column=2)
btn9=Button(cal,padx=16,pady=16,text="9",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
           command=lambda:btnclick(9)).grid(row=1,column=3)
btnP=Button(cal,padx=16,pady=16,text="+",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick("+")).grid(row=1,column=4)
########
btn4=Button(cal,padx=16,pady=16,text="4",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick(4)).grid(row=2,column=1)
btn5=Button(cal,padx=16,pady=16,text="5",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick(5)).grid(row=2,column=2)
btn6=Button(cal,padx=16,pady=16,text="6",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick(6)).grid(row=2,column=3)
btnMi=Button(cal,padx=16,pady=16,text="-",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
             command=lambda:btnclick("-")).grid(row=2,column=4)
########
btn1=Button(cal,padx=16,pady=16,text="1",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick(1)).grid(row=3,column=1)
btn2=Button(cal,padx=16,pady=16,text="2",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick(2)).grid(row=3,column=2)
btn3=Button(cal,padx=16,pady=16,text="3",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick(3)).grid(row=3,column=3)
btnM=Button(cal,padx=16,pady=16,text="*",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick("*")).grid(row=3,column=4)
########
btn0=Button(cal,padx=16,pady=16,text="0",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick(0)).grid(row=4,column=1)
btnC=Button(cal,padx=16,pady=16,text="C",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclear()).grid(row=4,column=2)
btnE=Button(cal,padx=16,pady=16,text="=",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnequals()).grid(row=4,column=3)
btnD=Button(cal,padx=16,pady=16,text="/",bd=8,fg="white",font=('arial',20,'bold'),bg="Navy blue",
            command=lambda:btnclick("/")).grid(row=4,column=4)


cal.mainloop()


# In[ ]:




