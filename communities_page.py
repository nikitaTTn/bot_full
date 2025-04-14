from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QComboBox, QTextEdit, QPushButton
from PyQt5.QtCore import Qt

class CommunitiesPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.interest_combo = QComboBox()
        self.interest_combo.addItems(["Технологии", "Искусство", "Спорт", "Музыка", "Литература"])
        form_layout.addRow("Что вас интересует?", self.interest_combo)

        self.mood_combo = QComboBox()
        self.mood_combo.addItems(["Энергичное", "Спокойное", "Творческое", "Мотивационное"])
        form_layout.addRow("Какое у вас настроение?", self.mood_combo)

        self.communication_combo = QComboBox()
        self.communication_combo.addItems(["Онлайн", "Офлайн", "Смешанное"])
        form_layout.addRow("Как предпочитаете общаться?", self.communication_combo)

        layout.addLayout(form_layout)

        analyze_button = QPushButton("Найти сообщества")
        analyze_button.clicked.connect(self.analyze_preferences)
        layout.addWidget(analyze_button)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_display)

        back_button = QPushButton("На главную")
        back_button.clicked.connect(lambda: self.parent.show_page(0))
        layout.addWidget(back_button)

        self.setLayout(layout)

    def analyze_preferences(self):
        interest = self.interest_combo.currentText()
        mood = self.mood_combo.currentText()
        communication = self.communication_combo.currentText()

        recommendations = {
            "Технологии": ["Техноэнтузиасты", "Инноваторы ИИ"],
            "Искусство": ["Творцы искусства", "Уличные художники"],
            "Спорт": ["Фитнес-клуб", "Беговое сообщество"],
            "Музыка": ["Меломаны", "Фанаты инди-групп"],
            "Литература": ["Книжный клуб", "Круг поэзии"]
        }

        communities = recommendations.get(interest, ["Неизвестная категория"])
        result = f"# Рекомендованные сообщества\n\n**Интересы**: {interest}\n**Настроение**: {mood}\n**Тип общения**: {communication}\n\n## Сообщества:\n"
        for community in communities:
            result += f"- {community}\n"

        self.result_display.setMarkdown(result)