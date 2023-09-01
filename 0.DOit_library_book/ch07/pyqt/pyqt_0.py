

# 테이블 전체 초기화하기

import sys
import numpy as np
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        # row col이 20 x 4 구조로 되있음
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        # 테이블 전체 초기화하는 버튼만들기
        self.clearBtn = QPushButton('Clear')
        self.clearBtn.clicked.connect(self.tableWidget.clear)
        
        # numpy사용 난수발생  행렬 20 x 4 why? 꺼내고 넣기 편하게  
        rand_items = np.random.randint(1, 100, size=(20, 4))

        # 테이블에 값 넣음
        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(rand_items[i, j])))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout = QVBoxLayout()  # layout을 만듬  like css 컨테이너
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.clearBtn)
        self.setLayout(layout)   # layout을 self에 적용

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    
    #%%
#  스크롤 버튼 만들기,  셀 정보 가져오기  추가

import sys
import numpy as np
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)
        
        # 셀정보를 띄울 label 추가
        self.label = QLabel('')

        # 초기화 버튼
        self.clearBtn = QPushButton('Clear')
        self.clearBtn.clicked.connect(self.tableWidget.clear)

        #  스크롤 버튼 
        self.scrollToTop = QPushButton('Scroll to Top')
        self.scrollToTop.clicked.connect(self.tableWidget.scrollToTop)

        self.scrollToBottom = QPushButton('Scroll to Bottom')
        self.scrollToBottom.clicked.connect(self.tableWidget.scrollToBottom)

        # 셀 정보 가져오기
        self.tableWidget.cellClicked.connect(self.set_label)

        rand_items = np.random.randint(1, 100, size=(20, 4))

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(rand_items[i, j])))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.clearBtn)
        layout.addWidget(self.scrollToTop)   # 스크롤 버튼 위젯
        layout.addWidget(self.scrollToBottom)  # 스크롤 버튼 위젯
        layout.addWidget(self.label)      # 셀정보를 띄울 label 위젯
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 150, 600, 400)
        self.show()
        
        
    # 셀 정보 가져오기 위한  set_label 함수 추가
    def set_label(self, row, column):
        item = self.tableWidget.item(row, column)
        value = item.text()
        label_string = 'Row: ' + str(row+1) + ', Column: ' + str(column+1) + ', Value: ' + str(value)
        self.label.setText(label_string)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())