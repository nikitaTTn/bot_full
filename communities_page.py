from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QComboBox, QTextEdit, QPushButton
from PyQt5.QtCore import Qt

class CommunitiesPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Форма для ввода предпочтений
        form_layout = QFormLayout()

        # Вопрос 1: Интересы
        self.interest_combo = QComboBox()
        self.interest_combo.addItems(["Технологии", "Искусство", "Спорт", "Музыка", "Литература"])
        form_layout.addRow("Что вас интересует?", self.interest_combo)

        # Вопрос 2: Настроение
        self.mood_combo = QComboBox()
        self.mood_combo.addItems(["Энергичное", "Спокойное", "Творческое", "Мотивационное"])
        form_layout.addRow("Какое у вас настроение?", self.mood_combo)

        # Вопрос 3: Тип общения
        self.communication_combo = QComboBox()
        self.communication_combo.addItems(["Онлайн", "Офлайн", "Смешанное"])
        form_layout.addRow("Как предпочитаете общаться?", self.communication_combo)

        layout.addLayout(form_layout)

        # Кнопка анализа
        analyze_button = QPushButton("Найти сообщества")
        analyze_button.clicked.connect(self.analyze_preferences)
        layout.addWidget(analyze_button)

        # Поле для результата
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_display)

        # Кнопка возврата
        back_button = QPushButton("На главную")
        back_button.clicked.connect(lambda: self.parent.show_page(0))
        layout.addWidget(back_button)

        self.setLayout(layout)

    def analyze_preferences(self):
        interest = self.interest_combo.currentText()
        mood = self.mood_combo.currentText()
        communication = self.communication_combo.currentText()

        # Простая логика подбора сообществ
        recommendations = {
            "Технологии": ["Tech Enthusiasts", "AI Innovators"],
            "Искусство": ["Art Creators", "Street Artists"],
            "Спорт": ["Fitness Club", "Running Community"],
            "Музыка": ["Music Lovers", "Indie Band Fans"],
            "Литература": ["Book Club", "Poetry Circle"]
        }

        communities = recommendations.get(interest, ["Неизвестная категория"])
        result = f"# Рекомендованные сообщества\n\n**Интересы**: {interest}\n**Настроение**: {mood}\n**Тип общения**: {communication}\n\n## Сообщества:\n"
        for community in communities:
            result += f"- {community}\n"

        self.result_display.setMarkdown(result)