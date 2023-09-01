# Tcl/TK 툴킷을 사용하는데 필요한 인터페이스 모듈
# Tcl은 파이썬과 같은 스크립트 언어  
# Tk는 Tcl을 위한 GUI 툴킷
# 인터페이스를 간단하게 만들어서 DB를 쉽게 관리하게 도와줌 

from tkinter import *

# 기본 형식

root = Tk()
label = Label(root, text = "Hello, World")
label.pack()

root.mainloop()