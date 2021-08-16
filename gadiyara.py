def f(event):
    def f1(event):
        def length(event):
            if opt.get():
                if En.get().isdigit():
                    tx=En.get()
                    s=ca.create_text((a+x)/2,(b+y)/2+10,text=tx)
                else:
                    tx=str(int(((a-event.x)**2+(b-event.y)**2)**0.5))
                    s=ca.create_text((a+event.x)/2,(b+event.y)/2+10,text=tx)
        nonlocal s
        if s!=None:
            ca.delete(s)
        if En.get().isdigit():
            d=int(En.get())
            try:
                theta=tanh((b-event.y)/(a-event.x))
            except:
                theta=3*pi/2
            if event.x < a:
                s=ca.create_line(a,b,a-d*cos(theta),b-d*sin(theta),width=wi.get())
                x=a-d*cos(theta)
                y=b-d*sin(theta)
            else:
                s=ca.create_line(a,b,a+d*cos(theta),b+d*sin(theta),width=wi.get())
                x=a+d*cos(theta)
                y=b+d*sin(theta)
        else:
            s=ca.create_line(a,b,event.x,event.y,width=wi.get())
        if op.get():
            ca.itemconfig(s,dash=(4,4))
        ca.bind("<ButtonRelease-1>",length)
    a=event.x
    b=event.y
    s=None
    ca.bind("<B1-Motion>",f1)
def arc(event):
    def f1(event):
        nonlocal s
        if s!=None:
            ca.delete(s)
        try:
            s=ca.create_arc(a,b,event.x,event.y,start=int(st.get()),extent=int(en.get()),width=wi.get())
            if op.get():
                ca.itemconfig(s,dash=(4,4))
        except:
            en.delete(0,END)
            st.delete(0,END)
            en.insert(0,"90")
            st.insert(0,"0")
    
    a=event.x
    b=event.y
    s=None
    ca.bind("<B1-Motion>",f1)
def oval(event):
    def f1(event):
        nonlocal s 
        if s!=None:
            ca.delete(s)
        s=ca.create_oval(a,b,event.x,event.y,width=wi.get())
        if op.get():
            ca.itemconfig(s,dash=(4,4))
    
    a=event.x
    b=event.y
    s=None
    ca.bind("<B1-Motion>",f1)
def rectangle(event):
    def f1(event):
        nonlocal s
        if s!=None:
            ca.delete(s)
        s=ca.create_rectangle(a,b,event.x,event.y,width=wi.get())
        if op.get():
            ca.itemconfig(s,dash=(4,4))
    
    a=event.x
    b=event.y
    s=None
    ca.bind("<B1-Motion>",f1)
def romb(event,i):
    def f1(event):
        nonlocal s
        if s!=None:
            ca.delete(s)
        x=event.x
        y=event.y
        if i==0:
            s=ca.create_polygon(a,((b+y)/2),((a+x)/2),b,x,(b+y)/2,(a+x)/2,y,fill="white",outline="black",width=wi.get())#--rombus
        elif i==5:
            s=ca.create_polygon(((a+x)/2),b,a,y,x,y,fill="white",outline="black",width=wi.get())#--triangle
        elif i==6:
            s=ca.create_polygon(a,b,a,y,x,y,fill="white",outline="black",width=wi.get())#--right triangle
        elif i==2:
            s=ca.create_polygon(a,(3*b+y)/4,(a+x)/2,(3*b+y)/4,(a+x)/2,b,x,(b+y)/2,(x+a)/2,y,(x+a)/2,(b+3*y)/4,a,(b+3*y)/4,fill="white",outline="black",width=wi.get()) #left
        elif i==3:
            s=ca.create_polygon((3*a+x)/4,b,(a+3*x)/4,b,(a+3*x)/4,(b+y)/2,x,(b+y)/2,(a+x)/2,y,a,(b+y)/2,(3*a+x)/4,(b+y)/2,fill="white",outline="black",width=wi.get())#down
        elif i==4:
            s=ca.create_polygon(x,(3*y+b)/4,(x+a)/2,(3*y+b)/4,(x+a)/2,y,a,(b+y)/2,(x+a)/2,b,(x+a)/2,(y+3*b)/4,x,(y+3*b)/4,fill="white",outline="black",width=wi.get())# right
        elif i==1:
            s=ca.create_polygon((3*x+a)/4,y,(x+3*a)/4,y,(x+3*a)/4,(b+y)/2,a,(b+y)/2,(a+x)/2,b,x,(b+y)/2,(3*x+a)/4,(b+y)/2,fill="white",outline="black",width=wi.get())
        elif i==7:
            s=ca.create_polygon(a,(5*b+3*y)/8,(a+x)/2,b,x,(5*b+3*y)/8,(a+7*x)/8,y,(7*a+x)/8,y,fill="white",outline="black",width=wi.get())# pentagone
        elif i==8:
            s=ca.create_polygon(a,(b+3*y)/4,a,(3*b+y)/4,(a+x)/2,b,x,(3*b+y)/4,x,(b+3*y)/4,(x+a)/2,y,fill="white",outline="black",width=wi.get()) #hexagone
        elif i==9:
            s=ca.create_polygon(a,(3*b+y)/4,(3*a+x)/4,b,(a+x)/2,(3*b+y)/4,(a+3*x)/4,b,x,(3*b+y)/4,(x+a)/2,y,fill="white",outline="black",smooth=True,width=wi.get())
        if op.get():
            ca.itemconfig(s,dash=(4,4))
    a=event.x
    b=event.y
    s=None
    ca.bind("<B1-Motion>",f1)
def curve(event):
    global i,a,b
    def f1(event):
        global i,c,d
        global s
        def f11(event,e,sc):
               global i,s
               i=e
               s=sc
        if i==0:
            if s!=None:
                ca.delete(s)
            c=event.x
            d=event.y
            s=ca.create_line(a,b,c,d,width=wi.get())
            ca.itemconfig(s,dash=(5,5))
            ca.bind("<ButtonRelease-1>",lambda event :f11(event,1,s))
        else:
            ca.delete(s)
            s=ca.create_line(a,b,event.x,event.y,c,d,smooth=True,width=wi.get())
            if op.get():
                ca.itemconfig(s,dash=(4,4))
            ca.bind("<ButtonRelease-1>",lambda event:f11(event,0,None))
            
    if i==0:
        a=event.x
        b=event.y
    ca.bind("<B1-Motion>",f1)
def dele(event):
    try:
        ca.delete(ca.find_withtag(CURRENT)[0])
    except:
        pass
    #(event.widget.delete(CURRENT))
def new():
    ca.delete("all")
def openfile():
    messagebox.showinfo("Info","You cant open file")
def saveas():
    messagebox.showinfo("Info","You cant save file")
def save():
    messagebox.showinfo("Info","You cant save file")
def colour(clr):
    def f1(event):
         ca.itemconfig(ca.find_closest(event.x,event.y)[0],fill=clr)
         return 1
    op1.config(bg=clr)
    ca.bind("<Button-1>",f1)
def df():
    pain=[f,arc,oval,curve,rectangle,dele]
    ca.bind("<Button-1>",pain[v.get()])
def df1():
    i=v.get()
    ca.bind("<Button-1>",lambda event:romb(event,i))
def txt(event):
    s=ca.create_text(event.x,event.y,text=text.get())
  
from tkinter import *
from math import tanh,sin,cos,pi
from tkinter import messagebox
ob=Tk()
file="no"
s=None
i=a=b=c=d=0
ob.geometry("1600x800")
ob.config(bg="lightblue")
ob2=Frame(ob)
ob2.grid(sticky=W)
ob1=Frame(ob)
ob1.grid(row=5,sticky=N)
ca=Canvas(ob1,height=1000,width=1500,bg="white")
ca.grid(row=4)
v=IntVar()
r1=Radiobutton(ob2,text="Line",value=0,variable=v,command=df).grid(row=0,column=0,sticky="w")
r2=Radiobutton(ob2,text="Arc",value=1,variable=v,command=df).grid(row=0,column=1,sticky="w")
r3=Radiobutton(ob2,text="Oval",value=2,variable=v,command=df).grid(row=0,column=2,sticky="w")
r4=Radiobutton(ob2,text="Curve",value=3,variable=v,command=df).grid(row=0,column=3,sticky="w")
r5=Radiobutton(ob2,text="Rectangle",value=4,variable=v,command=df).grid(row=1,column=0,sticky="w")
r6=Radiobutton(ob2,text="Rombus",value=0,variable=v,command=df1).grid(row=1,column=1,sticky="w")
r6=Radiobutton(ob2,text="Arrow-up",value=1,variable=v,command=df1).grid(row=1,column=2,sticky="w")
r6=Radiobutton(ob2,text="Arrow-right",value=2,variable=v,command=df1).grid(row=1,column=3,sticky="w")
r6=Radiobutton(ob2,text="Arrow-down",value=3,variable=v,command=df1).grid(row=2,column=0,sticky="w")
r6=Radiobutton(ob2,text="Arrow-left",value=4,variable=v,command=df1).grid(row=2,column=1,sticky="w")
r6=Radiobutton(ob2,text="Triangle",value=5,variable=v,command=df1).grid(row=2,column=2,sticky="w")
r6=Radiobutton(ob2,text="Right triangle",value=6,variable=v,command=df1).grid(row=2,column=3,sticky="w")
r6=Radiobutton(ob2,text="pentagone",value=7,variable=v,command=df1).grid(row=3,column=0,sticky="w")
r6=Radiobutton(ob2,text="Hexagone",value=8,variable=v,command=df1).grid(row=3,column=1,sticky="w")
r6=Radiobutton(ob2,text="Heart",value=9,variable=v,command=df1).grid(row=3,column=2,sticky="w")
r6=Radiobutton(ob2,text="Delete",value=5,variable=v,command=df).grid(row=4,column=1,sticky="w")
colors=["white","black","red","orange","green","yellow","violet","indigo","blue","purple"]
colo=StringVar(ob)
colo.set(colors[0])
op1=OptionMenu(ob2,colo,*colors,command=colour)
op1.grid(row=2,column=5)
wid=[1,2,3,4,5,6,7,8,9,10]
wi=StringVar(ob)
wi.set(wid[2])
op2=OptionMenu(ob2,wi,*wid).grid(column=6,row=2)
opt=IntVar()
Label(ob2,text="Include measurment with Line:-").grid(column=8,row=0,columnspan=1,sticky="w")
Radiobutton(ob2,variable=opt,value=0,text="No").grid(column=8,row=1,sticky="e")
Radiobutton(ob2,variable=opt,value=1,text="Yes").grid(column=9,row=1,sticky="e")
Label(ob2,text="Draw the mesured line").grid(column=10,row=0,columnspan=1,sticky="w")
En=Entry(ob2,width=10)
En.grid(column=10,row=1,sticky=E)
op=IntVar()
Label(ob2,text="Include Dashed line:-").grid(column=8,row=2,columnspan=1,sticky="w")
Radiobutton(ob2,variable=op,value=0,text="No").grid(column=8,row=3,sticky="e")
Radiobutton(ob2,variable=op,value=1,text="Yes").grid(column=9,row=3,sticky="e")
Label(ob2,text="Enter the start and extent value:-").grid(column=11,row=0,columnspan=1,sticky="w")
st=Entry(ob2,width=10)
st.grid(column=11,row=1,sticky=E)
en=Entry(ob2,width=10)
en.grid(column=12,row=1,sticky=W)
en.insert(0,"90")
st.insert(0,"0")
Label(ob2,text="Enter the text.double click to insert in area").grid(column=15,row=0,columnspan=1,sticky="w")
text=Entry(ob2,width=40)
text.grid(column=15,row=1,sticky=W)
ca.bind("<Double-1>",txt)
Label(ob2,text="File menu :--").grid(column=14,row=0,sticky=W)
b1=Button(ob2,text="New    ",bg="yellow",command=new).grid(column=14,row=1)
b2=Button(ob2,text="Open   ",bg="yellow",command=openfile).grid(column=14,row=2)
b1=Button(ob2,text="Save As",bg="yellow",command=saveas).grid(column=14,row=3)
b1=Button(ob2,text="Save   ",bg="yellow",command=save).grid(column=14,row=4)
ob.mainloop()
