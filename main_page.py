from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt

class MainPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Описание функционала в Markdown
        description = QTextEdit()
        description.setReadOnly(True)
        description.setMarkdown("""
# Добро пожаловать в Помощник-бот!

Этот бот поможет вам найти сообщества по вашему настроению и приобрести стильный мерч.

## Возможности:
- **Сообщества по настроению**: Ответьте на вопросы, и мы подберём сообщества, которые вам подойдут.
- **Купить мерч**: Выберите товары и узнайте сумму к оплате.
        """)
        description.setAlignment(Qt.AlignCenter)
        layout.addWidget(description)

        # Кнопка для перехода к сообществам
        communities_button = QPushButton("Найти сообщества")
        communities_button.clicked.connect(lambda: self.parent.show_page(1))
        layout.addWidget(communities_button)

        # Кнопка для перехода к мерчу
        merch_button = QPushButton("Купить мерч")
        merch_button.clicked.connect(lambda: self.parent.show_page(2))
        layout.addWidget(merch_button)

        self.setLayout(layout)