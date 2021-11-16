import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui import Ui_mainWindow
from PySide6.QtGui import QStandardItem
from PySide6.QtCore import QTimer

class MainWindow(QMainWindow):
    last_read = 0
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.btn_send.clicked.connect(self.send)
        self.ui.edit_text.returnPressed.connect(self.send)

        nickname = self.random_nickname()
        self.ui.edit_nickname.setText(nickname)

        # 환영합니다 메시지
        with open('./server.txt', 'a+', encoding='utf-8') as f:
            f.writelines(f'-----{nickname}님이 접속하셨습니다.-----\n')
            
        self.listen()
        
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.listen)
        self.timer.start()
        
    def send(self):
        nickname = self.ui.edit_nickname.text()
        text = self.ui.edit_text.text()
        msg = f'{nickname}: {text}'
        
        # 파일에다가 msg 쓰기
        # cp 949-euc-kr
        # unicode 43012-'가' 매칭됨
        # 즉, 한글을 다른 숫자에다가 매칭시켜서 그렇다.
        with open('./server.txt', 'a+', encoding='utf-8') as f:
            f.writelines(msg+'\n')
            
        self.ui.edit_text.clear()

        # 읽어오기
        self.listen()
        
    def random_nickname(self):
        nickname = random.choice(['zealot', 'dragoon', 'marin', 'firbat', 'scv', 'probe', 'zergling', 'hydra', 'drone'])
        num = random.randint(1, 1000)
        return f'{nickname}{num}'
        
    def listen(self):
        try:
            with open('./server.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
            self.ui.list_chat.addItems(lines[self.last_read:])
            self.last_read = len(lines)
            self.ui.list_chat.scrollToBottom()
        except:
            pass
        
if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())