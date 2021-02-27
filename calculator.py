from tkinter import *
tk=Tk()
tk.title("Calculator")
l=Label(tk,text="CALCULATOR",bg="dark gray",font=("Times",30,'bold')).grid(row=0,column=0,columnspan=3)
tk.config(bg="dark gray")
text=StringVar()
operator=""
def clk(char):
     global operator
     operator=e.get()
     if(str(char)=="="):
          try:
               op=str(eval(operator))
               text.set(op)
               operator=''
          except:
               clk("CLR")
               pass
     elif(str(char)=="CLR"):
          operator=""
          text.set(operator)
          
     else:
          operator+=str(char)
          text.set(operator)

e= Entry(tk,borderwidth=5,textvar=text,font=("Courier New",20,'bold'))
e.grid(row=1,column=0,columnspan=4,padx=10,pady=10)          
b1=Button(tk,text="1",padx=24,pady=20,command=lambda:clk(1),font=("Courier New",16,'bold')).grid(row=4,column=0)
b2=Button(tk,text="2",padx=24,pady=20,command=lambda:clk(2),font=("Courier New",16,'bold')).grid(row=4,column=1)
b3=Button(tk,text="3",padx=24,pady=20,command=lambda:clk(3),font=("Courier New",16,'bold')).grid(row=4,column=2)
b4=Button(tk,text="4",padx=24,pady=20,command=lambda:clk(4),font=("Courier New",16,'bold')).grid(row=3,column=0)
b5=Button(tk,text="5",padx=24,pady=20,command=lambda:clk(5),font=("Courier New",16,'bold')).grid(row=3,column=1)
b6=Button(tk,text="6",padx=24,pady=20,command=lambda:clk(6),font=("Courier New",16,'bold')).grid(row=3,column=2)
b7=Button(tk,text="7",padx=24,pady=20,command=lambda:clk(7),font=("Courier New",16,'bold')).grid(row=2,column=0)
b8=Button(tk,text="8",padx=24,pady=20,command=lambda:clk(8),font=("Courier New",16,'bold')).grid(row=2,column=1)
b9=Button(tk,text="9",padx=24,pady=20,command=lambda:clk(9),font=("Courier New",16,'bold')).grid(row=2,column=2)
b0=Button(tk,text="0",padx=24,pady=20,command=lambda:clk(0),font=("Courier New",16,'bold')).grid(row=5,column=1)
bdot=Button(tk,text=".",padx=24,pady=20,command=lambda:clk("."),font=("Courier New",16,'bold')).grid(row=5,column=0)
bl=Button(tk,text="(",padx=24,pady=20,command=lambda:clk("("),font=("Courier New",16,'bold')).grid(row=6,column=0)
br=Button(tk,text=")",padx=24,pady=20,command=lambda:clk(")"),font=("Courier New",16,'bold')).grid(row=6,column=1)
bmod=Button(tk,text="%",padx=24,pady=20,command=lambda:clk("%"),font=("Courier New",16,'bold')).grid(row=5,column=2)
bclr=Button(tk,text="CLEAR",padx=0,pady=20,command=lambda:clk("CLR"),font=("Courier New",16,'bold')).grid(row=6,column=2)
beq=Button(tk,text="=",padx=24,pady=20,command=lambda:clk("="),font=("Courier New",16,'bold')).grid(row=6,column=3)
badd=Button(tk,text="+",padx=24,pady=20,command=lambda:clk("+"),font=("Courier New",16,'bold')).grid(row=2,column=3)
bsub=Button(tk,text="-",padx=24,pady=20,command=lambda:clk("-"),font=("Courier New",16,'bold')).grid(row=3,column=3)
bmul=Button(tk,text="*",padx=24,pady=20,command=lambda:clk("*"),font=("Courier New",16,'bold')).grid(row=4,column=3)
bdiv=Button(tk,text="/",padx=24,pady=20,command=lambda:clk("/"),font=("Courier New",16,'bold')).grid(row=5,column=3)
