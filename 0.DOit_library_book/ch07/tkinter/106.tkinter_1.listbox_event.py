# Tcl/TK 툴킷을 사용하는데 필요한 인터페이스 모듈
# Listbox: 정해진 순서가 있는 여러개의 데이터를 표시하는 컴포넌트
# https://076923.github.io/posts/Python-tkinter-1/


# 리스트 박스를 선택햇을때 특별한 동작을 하게하려면 이벤트를 구현하면 된다

from tkinter import *
import tkinter.messagebox

#%%
# 이벤트 추가 - 기본형
# 클릭하면 콘솔창에뜸
'''
def event_for_listbox(event):
    print(f"리스트박스{item}가 클릭되었습니다.")
    # for반복문으로 넣어서 멀 클릭해도 item에 제일 마지막에 넣은 four만 나옴
'''

#%%

# 이벤트 추가
# 클릭하면 메시지박스가 뜨고 콘솔창에도뜸
def event_for_listbox(event):
    w = event.widget
    # 클릭한 value값이 뜨게
    # 아직 정해지지 않은 위치를 클릭할거니까 curselection이 들어감 
    index = int(w.curselection()[0])  
    value = w.get(index)
    msg = f"selected item: index({index}), value({value})"
    # 콘솔창
    print("리스트박스가 클릭되었습니다.", msg)
    # 메시지 박스
    tkinter.messagebox.showinfo("리스트 선택", msg)

    
#%%

# 
root = Tk()
listbox = Listbox(root)
listbox.pack()

for item in ["one", "two", "three", "four"] :
    # END는 리스트박스의 마지막 위치에 새로운 데이터를 추가하는 역할
    listbox.insert(END, item)  
    

# 이벤트를 컴포넌트에 연결하려면 bind를 써야됨
# '<<ListboxSelect>>'는 클릭했을때 라는 이벤트이름이 event_for_listbox(event)의 event로 들어감
listbox.bind('<<ListboxSelect>>', event_for_listbox)


root.mainloop()