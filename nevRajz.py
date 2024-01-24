import transzformaciok
from tkinter import *

#ablak létrehozása
win=Tk()

#ablak mérete
win.geometry("600x600")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")

#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)
fenyo2=[100,0,
        0,400,
        100,400,
        125,300,
        200,300,
        225,400,
        325,400,
        225,0,
        100,0
        ]

adam=[
        [100,0,
        0,400,
        100,400,
        125,300,
        200,300,
        225,400,
        325,400,
        225,0,
        100,0
        ],

        [120,225,
        200,225,
        165,62.5,
        120,225,
        ]]

adam2=[]
for e in adam:
        e=transzformaciok.nagyit(e, 2)
        e=transzformaciok.eltol(e, 100, 100)
        e=transzformaciok.forgat(e,90)
        
        adam2.append(e)

adam2=transzformaciok.forgat(adam2,0)

print(adam2)

for e in adam2:
        canvas.create_line(e,width=5,fill="black")

fenyo2Masolat=transzformaciok.eltol(fenyo2,100,100)
#canvas.create_line(fenyo2Masolat,width=5,fill="green")
#fenyo3Masolat=transzformaciok.eltol(fenyo3,100,100)
#canvas.create_line(fenyo3Masolat,width=5,fill="green")
#fenyo4Masolat=transzformaciok.eltol(fenyo4,100,100)
#canvas.create_line(fenyo4Masolat,width=5,fill="green")

win.mainloop()