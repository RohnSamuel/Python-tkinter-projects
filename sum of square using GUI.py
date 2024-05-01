#creating a program from displaying sum of squares using the individual digits of a number with gui
from tkinter import *
#claculation algorithm
def sum_of_sqrs():
    try:      
        numb=int(inputt.get())  
        ans=0
        while numb>0:
            digit=numb%10
            ans+=digit**2
            numb//=10
        final_ans.config(text=f'The result is {ans}')
    except Exception:
        final_ans.config(text='Error occured!!!')
#gui
root=Tk()
root.title('Sum Of Squares')
heading=Label(root,text='Enter the number: ',font=('Century Gothic',18))
heading.pack(fill='x')
inputt=Entry(root,font=('Century Gothic',18))
inputt.pack(fill='x')
outputt=Button(root,text='Answer',font=('Century Gothic',18),command=sum_of_sqrs)
outputt.pack(fill='x')
final_ans=Label(root,text='',font=('Century Gothic',18))
final_ans.pack(fill='x')
mainloop()
