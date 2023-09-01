# Tcl/TK 툴킷을 사용하는데 필요한 인터페이스 모듈
# Listbox: 정해진 순서가 있는 여러개의 데이터를 표시하는 컴포넌트

from tkinter import *

# 기본 형식

root = Tk()
listbox = Listbox(root)
listbox.pack()

for item in ["one", "two", "three", "four"]:
    # END는 리스트박스의 마지막 위치에 새로운 데이터를 추가하는 역할
    listbox.insert(END, item)  
    
root.mainloop()

