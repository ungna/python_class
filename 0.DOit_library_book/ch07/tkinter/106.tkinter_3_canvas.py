# Tcl/TK 툴킷을 사용하는데 필요한 인터페이스 모듈


from tkinter import *
import tkinter.messagebox

import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
#  geometry 생성되는 창의 너비, 높이, 위치를 설정
# (창의 너비 x 	창의 높이 + 생성되는 창의 가로 방향 위치 + 생성되는 창의 세로 방향 위치) 
window.geometry("640x400+100+100")
window.resizable(False, False)

canvas=tkinter.Canvas(window, relief="solid", bd=2)

# 10, 10 에서 출발 (20, 20)  (20, 130) (30, 140) 으로 이동하면서 라인을 그림
line=canvas.create_line(10, 10, 20, 20, 20, 130, 30, 140, fill="red") 

polygon=canvas.create_polygon(50, 50, 170, 170, 100, 170, outline="yellow")
oval=canvas.create_oval(100, 200, 150, 250, fill="blue", width=3)
arc=canvas.create_arc(100, 100, 300, 300, start=0, extent=150, fill='red')

canvas.pack()

window.mainloop()


#%%

# 구경만
import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("700x500+100+100")
window.resizable(True, True)

width=1

def drawing(event):
    if width>0:
        x1=event.x-1
        y1=event.y-1
        x2=event.x+1
        y2=event.y+1
        canvas.create_oval(x1, y1, x2, y2, outline="red", width=width)

def scroll(event):
    global width
    if event.delta==120:
        width+=1
    if event.delta==-120:
        width-=1
    label.config(text=str(width))

canvas=tkinter.Canvas(window, relief="solid", bd=2)
canvas.pack(expand=True, fill="both")
canvas.bind("<B1-Motion>", drawing)
canvas.bind("<MouseWheel>", scroll)

label=tkinter.Label(window, text=str(width))
label.pack()

window.mainloop()