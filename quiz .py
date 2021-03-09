import pandas as pd
from tkinter import*

top = Tk()
top.title('QUIZ')
df = pd.read_csv(r"F:\codes for py\Analogy.csv",delimiter=',')#file location of the csv 
i=0
total=0
qvar=[]
global L1,L2,value,var,var1

def reset():
    R1.deselect()
    R2.deselect()
    R3.deselect()
    R4.deselect()
    R5.deselect()


def makewindow():
    global i,L1,qvar,top,R1,R2,R3,R4,R5,var,var1,qvar
    L1 = Label(top)
    L1.config(text=qvar)
    L1.pack()
    var=StringVar()
    R1=Radiobutton(top,value="A",variable=var)
    R1.deselect()
    R1.pack(anchor=W)
    R2=Radiobutton(top,value="B",variable=var)
    R2.deselect()
    R2.pack(anchor=W)
    R3=Radiobutton(top,value="C",variable=var)
    R3.deselect()
    R3.pack(anchor=W)
    R4=Radiobutton(top,value="D",variable=var)
    R4.deselect()
    R4.pack(anchor=W)
    R5=Radiobutton(top,value="E",variable=var)
    R5.deselect()
    R5.pack(anchor=W)
    B4=Button(top,text="CLEAR YOUR RESPONSE",command=reset)
    B4.pack(side=BOTTOM)
    

def loop():
    global i,qvar,r1var,r2var,r3var,r4var,r5var,r6var,L1,R1,R2,R3,R4,R5,L2,var1
    i=0
    qvar=df.iloc[i,0]
    r1var=df.iloc[i,1]
    r2var=df.iloc[i,2]
    r3var=df.iloc[i,3]
    r4var=df.iloc[i,4]
    r5var=df.iloc[i,5]
    r6var=df.iloc[i,6]
    L1.config(text=qvar)
    R1.config(text=r1var)
    R2.config(text=r2var)
    R3.config(text=r3var)
    R4.config(text=r4var)
    R5.config(text=r5var)
    
def inn():
    global i,qvar,r1var,r2var,r3var,r4var,r5var,r6var,L1,R1,R2,R3,R4,R5,L2
    i=i+1
    global r6var,total
    
    ans=var.get()
    for j in ans:
        if(ans==r6var):
            total=total+4
        elif(ans==0):
            total=total
            break
        else:
            total=total-1
    
         
    qvar=df.iloc[i,0]
    r1var=df.iloc[i,1]
    r2var=df.iloc[i,2]
    r3var=df.iloc[i,3]
    r4var=df.iloc[i,4]
    r5var=df.iloc[i,5]
    r6var=df.iloc[i,6]
    L1.config(text=qvar)
    #L2.config(text=total_marks)
    R1.config(text=r1var)
    R2.config(text=r2var)
    R3.config(text=r3var)
    R4.config(text=r4var)
    R5.config(text=r5var)       

def total_marks():
    global total,L2,top
    root=Tk()
    L2=Label(root,text=("your mark:"+str(total)))
    L2.pack()
    top.destroy()
    add_marks()

def add_marks():
   
    global r6var,total
    
    ans=var.get()
    for j in ans:
        if(ans==r6var):
            total=total+2
        elif(ans==0):
            total=total
            break
        else:
            total=total-1
    
    
def out():
    global i,qvar,r1var,r2var,r3var,r4var,r5var,L1,R1,R2,R3,R4,R5,L2
    i=i-1
    global r6var,total
    
    ans=var.get()
    if(ans==r6var):
        total=total-2
    elif(ans==0):
        total=total
        
    qvar=df.iloc[i,0]
    r1var=df.iloc[i,1]
    r2var=df.iloc[i,2]
    r3var=df.iloc[i,3]
    r4var=df.iloc[i,4]
    r5var=df.iloc[i,5]
    r6var=df.iloc[i,6]
    R1.config(text=r1var)
    R2.config(text=r2var)
    R3.config(text=r3var)
    R4.config(text=r4var)
    R5.config(text=r5var)
    L1.config(text=qvar)
    #L2.config(text=total_marks)
    
frame1=Frame(top)
frame1.pack(side=BOTTOM)
B1 = Button(frame1,text ="next",bg='black',fg='white', command = inn)
B1.grid(row=0,column=2)
B2 = Button(frame1,text ="prev",bg='black',fg='white', command = out)
B2.grid(row=0,column=0)
B3=Button(frame1,text='FINISH',bg='black',fg='white',command=total_marks)
B3.grid(row=0,column=1)             


  

makewindow()
loop()
inn()
add_marks()









