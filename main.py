import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from main_page import MainPage
from communities_page import CommunitiesPage
from merch_page import MerchPage

class AssistantBot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Помощник-бот")
        self.setGeometry(100, 100, 600, 400)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.main_page = MainPage(self)
        self.communities_page = CommunitiesPage(self)
        self.merch_page = MerchPage(self)

        self.stack.addWidget(self.main_page)
        self.stack.addWidget(self.communities_page)
        self.stack.addWidget(self.merch_page)

        self.show_page(0)

    def show_page(self, index):
        self.stack.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AssistantBot()
    window.show()
    sys.exit(app.exec_())