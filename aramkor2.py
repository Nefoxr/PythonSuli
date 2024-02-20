class jel:
    x=0
    y=0
    meret=100
    szin="black"
    def __init__(self,x,y,meret,canvas):
        self.x=x
        self.y=y
        self.meret=meret
        self.canvas=canvas
        self.rajz()

    def rajz(self,vonalak=[]):
        self.canvas.create_rectangle(self.x,self.y,
                              self.x+self.meret,self.y+self.meret,
                              fill="gray")

        
        for egyVonal in vonalak:
            self.canvas.create_line(egyVonal, width=self.meret*0.03, fill=self.szin)


class elem(jel):  
    def rajz(self):
        vonalak=[
            [
                self.x, self.y+self.meret*0.5,
                self.x+self.meret*0.45, self.y+self.meret*0.5,
            ],
            [
                self.x+self.meret*0.45, self.y+self.meret*0.2,
                self.x+self.meret*0.45, self.y+self.meret*0.8,
            ],
            [
                self.x+self.meret*0.55, self.y+self.meret*0.4,
                self.x+self.meret*0.55, self.y+self.meret*0.6,
            ],
            [
                self.x+self.meret*0.55, self.y+self.meret*0.5,
                self.x + self.meret*1.00, self.x + self.meret*0.5,
            ],
        ]
        jel.rajz(self,vonalak=vonalak)

class kapcsolo(jel):  
    def rajz(self):
        vonalak=[
            [
                self.x, self.y+self.meret*0.5,
                self.x+self.meret*0.45, self.y+self.meret*0.5,
            ],
            [
                self.x+self.meret*0.45, self.y+self.meret*0.2,
                self.x+self.meret*0.45, self.y+self.meret*0.8,
            ],
            [
                self.x+self.meret*0.55, self.y+self.meret*0.4,
                self.x+self.meret*0.55, self.y+self.meret*0.6,
            ],
            [
                self.x+self.meret*0.55, self.y+self.meret*0.5,
                self.x + self.meret*1.00, self.y + self.meret*0.5,
            ],
        ]
        jel.rajz(self,vonalak=vonalak)

from tkinter import *



win=Tk()
win.geometry("600x620+100+20")
win.title("Áramkör 10.B/1 2024")
canvas=Canvas(win,bg="white")
print(canvas)

canvas.pack(fill = BOTH, expand = 1)

elem1=elem(0,0,100,canvas)
elem1.rajz()

elem2=elem(100,100,50,canvas)
elem2.szin="red"
elem2.rajz()
kapcsolo1=kapcsolo(400,350,100,canvas)

win.mainloop()