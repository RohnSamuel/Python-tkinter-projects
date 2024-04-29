#finding gcd of two numbers
from math import gcd
from tkinter import *

def f_gcd(roota,rootaa):
    try:
            
        num1=int(roota.get())
        num2=int(rootaa.get())
        ans=gcd(num1,num2)
        answer.config(text=f'The GCD of {num1} and {num2} is {ans}')
    except Exception:
        answer.config(text='Error occured!!!Try again')

#gui
root=Tk()
rootl=Label(root,text='GCD OF TWO GIVEN NUMBERS',font=('Century Gothic',25))
rootl.pack(fill='x')
rootq=Label(root,text='Enter first number',font=('Century Gothic',20))
rootq.pack(fill='x')
roota=Entry(root,font=('Century Gothic',18))
roota.pack(fill='x')

rootqq=Label(root,text='Enter second number',font=('Century Gothic',20))
rootqq.pack(fill='x')
rootaa=Entry(root,font=('Century Gothic',18))
rootaa.pack(fill='x')

but=Button(root,text='Answer',font=('Century Gothic',20),command=lambda:f_gcd(roota,rootaa))
but.pack()
answer=Label(root,text='',font=('Century Gothic',16))
answer.pack(fill='x')
mainloop()
