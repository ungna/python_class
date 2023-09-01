# Tcl/TK 툴킷을 사용하는데 필요한 인터페이스 모듈
# Tcl은 파이썬과 같은 스크립트 언어  
# Tk는 Tcl을 위한 GUI 툴킷
# 인터페이스를 간단하게 만들어서 DB를 쉽게 관리하게 도와줌 

from tkinter import *
import tkinter.messagebox

#%%
# 이벤트
# 
def onevent(event):
    w = event.widget
 # 버튼은 클릭할 위치가 정해져있으니까 curselection이 없음
    msg = f"button click ({w}) : 버튼이 클릭되었습니다"
    # 콘솔창
    print("리스트박스가 클릭되었습니다.", msg)
    # 메시지 박스
    tkinter.messagebox.showinfo("리스트 선택", msg)
    

#%%
#

root = Tk()
btn = Button(root, text="여기를 클릭해 주세요")
btn.pack()

btn.bind("<Button-1>", onevent)

root.mainloop()