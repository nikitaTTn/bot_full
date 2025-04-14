from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class MerchPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.items = {
            "Футболка с логотипом": 1500,
            "Кепка стильная": 800,
            "Худи тёплое": 3000,
            "Стикеры (набор)": 300
        }
        self.selected_items = {}
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title = QLabel("Выберите товары:")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Список товаров с чекбоксами
        self.checkboxes = {}
        for item, price in self.items.items():
            checkbox = QCheckBox(f"{item} - {price} руб.")
            checkbox.stateChanged.connect(self.update_total)
            self.checkboxes[item] = checkbox
            layout.addWidget(checkbox)

        # Поле для отображения суммы
        self.total_display = QTextEdit()
        self.total_display.setReadOnly(True)
        self.total_display.setMarkdown("## Сумма к оплате: 0 руб.")
        self.total_display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.total_display)

        # Кнопка возврата
        back_button = QPushButton("На главную")
        back_button.clicked.connect(lambda: self.parent.show_page(0))
        layout.addWidget(back_button)

        self.setLayout(layout)

    def update_total(self):
        total = 0
        self.selected_items.clear()
        for item, checkbox in self.checkboxes.items():
            if checkbox.isChecked():
                self.selected_items[item] = self.items[item]
                total += self.items[item]
        self.total_display.setMarkdown(f"## Сумма к оплате: {total} руб.\n\n**Выбранные товары**:\n" + 
                                      "\n".join(f"- {item}: {price} руб." for item, price in self.selected_items.items()))