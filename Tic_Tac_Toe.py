from ctypes import windll
from lib2to3.pgen2.tokenize import TokenError
from sys import call_tracing
from tkinter import *
from array import *
from tkinter import ttk
from tkinter import messagebox
from webbrowser import BackgroundBrowser
from PIL import Image, ImageTk

global tic ; tic = int(0)
global toe ; toe = int(0)
global tie ; tie = int(0)
global turn; turn = int(1)

def destroy() :
    global tic, toe, tie 
    clearall()
    root.geometry("475x255")
    m.f.tkraise()
    if tie > 0 and tic == toe == 0 :
        messagebox.showinfo('Game Over','"///It`s a tie!\\\\\\\"');
    elif toe == tic :
        messagebox.showinfo('Game Over','"///It`s a tie!\\\\\\\"');
    elif tic > toe :
        messagebox.showinfo('Game Over','"///X wins!\\\\\\\"');
    elif toe > tic :
        messagebox.showinfo('Game Over','"///O wins!\\\\\\"');
    tic = toe = tie = int(0)

def switch() :
    l1.config(text="X  : \n "+str(tic)+" pts")
    l2.config(text="0  : \n "+str(toe)+" pts")
    l3.config(text="Tie : \n "+str(tie)+" pts\n")
    clearall()
    root.geometry("475x625")
    frame.tkraise()

def state(num) :
    if (num % 2) == 0:
        return True
    else:
        return False

def click(event):
    global tic, toe,tie,turn
    x = event.x_root - frame.winfo_rootx()
    y = event.y_root - frame.winfo_rooty()
    draw(frame.grid_location(x, y))
    if check("X") == True :
        tic = tic+1
        l1.config(text="X  : \n "+str(tic)+" pts")
        clearall()
    elif check("O") == True :
        toe = toe+1
        l2.config(text="0  : \n "+str(toe)+" pts")
        clearall()
    elif turn > 9 :
        tie = tie+1
        l3.config(text="Tie : \n "+str(tie)+" pts\n")
        clearall()
      
def draw(tuple) :
    global turn
    x,y = tuple
    if state(turn) == False :
        turn = squares[x][y].drawX(turn)
    else :
        turn = squares[x][y].drawO(turn)

def clearall() :
    global turn
    turn = 1
    for i in range(3) :
        for j in range(3):
            squares[i][j].clear()

def check(str) :
    #Horizontals/Verticals
    for i in range(3) :
        if squares[i][0].getShape() == squares[i][1].getShape() == squares[i][2].getShape() == str:
                return True
        if squares[0][i].getShape() == squares[1][i].getShape() == squares[2][i].getShape() == str:
                return True
    #Diagonals
    if squares[0][0].getShape() == squares[1][1].getShape() == squares[2][2].getShape() == str:
        return True
    if squares[0][2].getShape() == squares[1][1].getShape() == squares[2][0].getShape() == str:
        return True
    return False
                     
class square :
    
    def __init__(self,root,x,y) :
        #Root window. Could be Tk() or frame...
        self.root = root
        #Style with ttk 
        s = ttk.Style(self.root)
        #Canvas on which we'll draw either x or y
        self.canvas = Canvas(self.root,bd=0, highlightthickness=0, relief='ridge')
        self.canvas.config(borderwidth=4)
        self.canvas.config(width=150,height=150)
        #self.create_line()
        self.canvas.grid(column=x,row=y,sticky=N+E+W+S)
        #boolean variables for either x or y that will determine if canvas is occupied
        self.Xdrawn = False
        self.Odrawn = False
        
    def getShape(self) :
        if self.Xdrawn == True :
            return "X"
        if self.Odrawn == True:
            return "O"
        else :
            return "NO"  
    
    def IsDrawn(self) :
        if self.Xdrawn == True : 
            return True
        elif self.Odrawn == True :
            return True
        else :
            return False
        
    def drawX(self,int) :
        global turn
        if self.IsDrawn() == False :
            self.canvas.create_line((15, 15, 135, 135), width=7, fill="#EE4035")
            self.canvas.create_line((15, 135, 135, 15), width=7, fill="#EE4035")
            self.Xdrawn = True
            return (int+1)
        else :
            return int

            
    def drawO(self,int) :
        global turn
        if self.IsDrawn() == False :
            self.canvas.create_oval((20, 15, 130, 135), width=10,outline="#0492CF")
            self.Odrawn = True
            return (int+1)
        else:
            return int

    
    def draw_horizontal(self) :
        self.canvas.create_line(0,75,150,75,width=4)
            
    def clear(self) :
        self.canvas.delete("all")
        self.Xdrawn = False
        self.Odrawn = False

class main :    
    def __init__(self,root) :
        s = ttk.Style(root)
        s.theme_use("alt")
        s.configure("M.TFrame",background="white")
        s.configure("M.TButton",font = ("bauhaus 93", 30), foreground="#7BC043",background="white",borderwidth=3,relief="ridge")
        s.configure("M.TLabel",font = ("bauhaus 93", 50), foreground="#7BC043",background="white",borderwidth=3,relief="ridge")
        self.f = ttk.Frame(root,style="M.TFrame")
        self.f.config(width=300,height=300)
        self.f.tkraise()
        self.f.columnconfigure(0,weight=1)
        self.f.rowconfigure(0,weight=1); self.f.rowconfigure(1,weight=1); self.f.rowconfigure(2,weight=1); self.f.rowconfigure(3,weight=1);self.f.rowconfigure(4,weight=1);self.f.rowconfigure(5,weight=1);self.f.rowconfigure(6,weight=1);self.f.rowconfigure(7,weight=1);self.f.rowconfigure(8,weight=1);self.f.rowconfigure(9,weight=1);
        self.l = ttk.Label(self.f,text="TIC  \nTAC  \nTOE ",anchor="center",style="M.TLabel")
        self.l.grid(column=0,row=0,rowspan=2,sticky="news")
        self.b = ttk.Button(self.f,text="Play",style="M.TButton")
        self.b.grid(column=0,row=2,sticky="new")
        self.f.grid(column=0,row=0,rowspan=2,sticky="news")
        pass 
           
global root 
root = Tk()
root.resizable(1,1)
root.geometry("475x255")
root.title("Tic&Toe")      

global frame;frame= ttk.Frame(root)
frame.columnconfigure(0,weight=1);frame.columnconfigure(1,weight=1);frame.columnconfigure(2,weight=1);
frame.rowconfigure(0,weight=1);frame.rowconfigure(1,weight=1);frame.rowconfigure(2,weight=1);
frame.grid(column=0,row=0)    

global m ; m = main(root) 
m.b.config(command=switch)

s = ttk.Style(root)
s.theme_use("alt")
s.configure("M.TLabel",font = ("bauhaus 93", 22), foreground="#EE4035",background="white",borderwidth=3,relief="ridge")
s.configure("N.TLabel",font = ("bauhaus 93", 22), foreground="#0492CF",background="white",borderwidth=3,relief="ridge")
s.configure("O.TLabel",font = ("bauhaus 93", 22), foreground="#7BC043",background="white",borderwidth=3,relief="ridge")
s.configure("O.TButton",font = ("bauhaus 93", 22), foreground="#7BC043",background="white",borderwidth=3,relief="ridge")

l1 = ttk.Label(frame, style="M.TLabel", text="X  : \n "+str(tic)+" pts", anchor='nw')
l1.grid(column=0, row=4,ipadx=0, ipady=0, sticky=W+E+N+S)
l2 = ttk.Label(frame, style="N.TLabel", text= "0  : \n "+str(toe)+" pts", anchor='nw')
l2.grid(column=2, row=4,ipadx=0, ipady=0, sticky=N+E+W+S)
l3 = ttk.Label(frame, style="O.TLabel", text="Tie : \n "+str(tie)+" pts\n", anchor='nw')
l3.grid(column=1, row=4,ipadx=0, ipady=0, sticky=N+E+W+S)
back = ttk.Button(frame,style="O.TButton",text="End Round",command=destroy)
back.grid(column=0, row=5,columnspan=3, sticky=N+E+W+S)
global squares
squares =[]    
for i in range(3) :
    x = []
    for j in range(3):
        x.append(square(frame,i,j))
    squares.append(x) 

#windll.shcore.SetProcessDpiAwareness(1);
root.bind("<Button-1>",click)
mainloop()