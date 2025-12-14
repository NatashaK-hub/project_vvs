import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
import os


class MathAnalysisPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui() #метод, где происходит инициализация пользовательского интерфейса

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title = QLabel("Математический анализ")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter) #выравнивание по центру
        title_font = QFont() #объект для настройки шрифта
        title_font.setPointSize(20)
        title_font.setBold(True) #полужирный шрифт
        title.setFont(title_font) #применение настроенного шрифта к заголовку
        layout.addWidget(title)

        #создается компоновщик для кнопок
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(20) #расстояние между элементами 20 пикселей
        buttons_layout.setContentsMargins(50, 20, 50, 20) #внутренние отступы от краев лейаута

        # Первый замечательный предел
        limit1_btn = QPushButton("Первый замечательный предел")
        limit1_btn.setFont(QFont("Arial", 12))
        limit1_btn.setMinimumHeight(60) #минимальная высота кнопки в пикселях
        limit1_btn.clicked.connect(lambda: self.open_limit_page("Первый замечательный предел"))
        buttons_layout.addWidget(limit1_btn)

        # Второй замечательный предел
        limit2_btn = QPushButton("Второй замечательный предел")
        limit2_btn.setFont(QFont("Arial", 12))
        limit2_btn.setMinimumHeight(60)
        limit2_btn.clicked.connect(lambda: self.open_limit_page("Второй замечательный предел"))
        buttons_layout.addWidget(limit2_btn)

        # Касательная
        tangent_btn = QPushButton("Касательная к кривой")
        tangent_btn.setFont(QFont("Arial", 12))
        tangent_btn.setMinimumHeight(60)
        tangent_btn.clicked.connect(self.open_tangent_page)
        buttons_layout.addWidget(tangent_btn)

        # Таблица эквивалентных
        same_btn = QPushButton("Таблица эквивалентных")
        same_btn.setFont(QFont("Arial", 12))
        same_btn.setMinimumHeight(60)
        same_btn.clicked.connect(self.open_same_page)
        buttons_layout.addWidget(same_btn)


        layout.addLayout(buttons_layout)

        # Кнопка возврата
        back_btn = QPushButton("← Назад к разделам математики")
        #.connect - метод привязки функции к сигналу
        #show_main_page - метод главного окна, который переключает на главную страницу
        back_btn.clicked.connect(self.main_window.show_main_page)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def open_limit_page(self, title):
        """Открытие страницы с пределом"""
        page = LimitPage(self.main_window, title)
        self.main_window.set_page(page, title)

    def open_tangent_page(self):
        """Открытие страницы с касательной"""
        page = TangentPage(self.main_window)
        self.main_window.set_page(page, "Касательная к кривой")

    def open_same_page(self):
        """Открытие страницы с эквивалентными"""
        page = SamePage(self.main_window)
        self.main_window.set_page(page, "Таблица эквивалентных")


class LimitPage(QWidget):
    def __init__(self, main_window, title):
        super().__init__()
        self.main_window = main_window
        self.title = title
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel(self.title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)





        layout.addWidget(title_label)

        # Формула
        if "Первый" in self.title:
            formula = r"$\lim_{x \to 0} \frac{\sin x}{x} = 1$"
            description = "Этот предел показывает, что синус малого угла примерно равен самому углу (в радианах)."
        else:
            formula = r"$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$"
            description = "Этот предел определяет число Эйлера (e) - основание натурального логарифма."

        formula_label = QLabel(formula)
        formula_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        formula_font = QFont()
        formula_font.setPointSize(16)
        formula_label.setFont(formula_font)
        layout.addWidget(formula_label)

        # Описание
        description_label = QLabel(description)
        description_label.setWordWrap(True) #включение переноса слов
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description_label)

        layout.addStretch()

        # Кнопка возврата
        back_btn = QPushButton("← Назад к математическому анализу")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def go_back(self):
        page = MathAnalysisPage(self.main_window)
        self.main_window.set_page(page, "Математический анализ")


class TangentPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Касательная к кривой")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)

        # Описание
        desc_label = QLabel(
            "Касательная прямая к графику функции в точке x₀ - это прямая, "
            "которая наилучшим образом аппроксимирует функцию в окрестности этой точки."
        )
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(desc_label)

        layout.addStretch()

        # Кнопка возврата
        back_btn = QPushButton("← Назад к математическому анализу")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def go_back(self):
        page = MathAnalysisPage(self.main_window)
        self.main_window.set_page(page, "Математический анализ")


class SamePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Таблица эквивалентных")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)


        same_btn_sinus = QPushButton("Синус")
        same_btn_sinus.setFont(QFont("Arial", 12))
        same_btn_sinus.setMinimumHeight(60)
        same_btn_sinus.clicked.connect(self.open_sinus_page)
        layout.addWidget(same_btn_sinus)


        same_btn_cosinus = QPushButton("Косинус")
        same_btn_cosinus.setFont(QFont("Arial", 12))
        same_btn_cosinus.setMinimumHeight(60)
        same_btn_cosinus.clicked.connect(self.open_cosinus_page)
        layout.addWidget(same_btn_cosinus)

        same_btn_ln = QPushButton("Натуральный логарифм")
        same_btn_ln.setFont(QFont("Arial", 12))
        same_btn_ln.setMinimumHeight(60)
        same_btn_ln.clicked.connect(self.open_ln_page)
        layout.addWidget(same_btn_ln)


        same_btn_exp = QPushButton("Экспонента")
        same_btn_exp.setFont(QFont("Arial", 12))
        same_btn_exp.setMinimumHeight(60)
        same_btn_exp.clicked.connect(self.open_exp_page)
        layout.addWidget(same_btn_exp)



        # Описание
        desc_label = QLabel(
            " "

        )
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(desc_label)

        layout.addStretch()

        # Кнопка возврата
        back_btn = QPushButton("← Назад к математическому анализу")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def open_sinus_page(self):
        """Открытие страницы с синусом"""
        page = SinusPage(self.main_window)
        self.main_window.set_page(page, "Эквивалентность синуса")

    def open_cosinus_page(self):
        page = CosinusPage(self.main_window)
        self.main_window.set_page(page, "Эквивалентность косинуса")

    def open_ln_page(self):
        page = LnPage(self.main_window)
        self.main_window.set_page(page, "Эквивалентность натурального логарифма")

    def open_exp_page(self):
        page = ExpPage(self.main_window)
        self.main_window.set_page(page, "Эквивалентность экспоненты")

    def go_back(self):
        page = MathAnalysisPage(self.main_window)
        self.main_window.set_page(page, "Математический анализ")


class SinusPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        video_path = "C:/Users/andre/PycharmProjects/misis_BBC/Example.mp4"

        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        self.player.setSource(QUrl.fromLocalFile(video_path))
        layout.addWidget(self.video_widget)

        # Автозапуск
        self.player.play()

        # Заголовок
        #title_label = QLabel("Эквивалентность синуса")
        #title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #title_font = QFont()
        #title_font.setPointSize(18)
        #title_font.setBold(True)
        #title_label.setFont(title_font)
        #layout.addWidget(title_label)

        # Формула
        #formula_label = QLabel(r"$\sin x \sim x$ при $x \to 0$")
        #formula_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #formula_label.setFont(QFont("Arial", 16))
        #layout.addWidget(formula_label)

        # Кнопка назад
        back_btn = QPushButton("← Назад к таблице эквивалентных")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def go_back(self):
        page = SamePage(self.main_window)
        self.main_window.set_page(page, "Таблица эквивалентных")


class CosinusPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        video_path = "C:/Users/andre/PycharmProjects/misis_BBC/cos.mp4"

        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        self.player.setSource(QUrl.fromLocalFile(video_path))
        layout.addWidget(self.video_widget)

        # Автозапуск
        self.player.play()

        back_btn = QPushButton("← Назад к таблице эквивалентных")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def go_back(self):
        page = SamePage(self.main_window)
        self.main_window.set_page(page, "Таблица эквивалентных")


class LnPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        video_path = "C:/Users/andre/PycharmProjects/misis_BBC/ln.mp4"

        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        self.player.setSource(QUrl.fromLocalFile(video_path))
        layout.addWidget(self.video_widget)

        # Автозапуск
        self.player.play()

        back_btn = QPushButton("← Назад к таблице эквивалентных")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def go_back(self):
        page = SamePage(self.main_window)
        self.main_window.set_page(page, "Таблица эквивалентных")


class ExpPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        video_path = "C:/Users/andre/PycharmProjects/misis_BBC/exp.mp4"

        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        self.player.setSource(QUrl.fromLocalFile(video_path))
        layout.addWidget(self.video_widget)

        # Автозапуск
        self.player.play()

        back_btn = QPushButton("← Назад к таблице эквивалентных")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def go_back(self):
        page = SamePage(self.main_window)
        self.main_window.set_page(page, "Таблица эквивалентных")

class LinearAlgebraPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Линейная алгебра")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        content = QLabel("Страница линейной алгебры в разработке...")
        content.setWordWrap(True)
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(content)

        layout.addStretch()

        # Кнопка возврата
        back_btn = QPushButton("← Назад к разделам математики")
        back_btn.clicked.connect(self.main_window.show_main_page)
        layout.addWidget(back_btn)

        self.setLayout(layout)


class AnalyticGeometryPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Аналитическая геометрия")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        content = QLabel("Страница аналитической геометрии в разработке...")
        content.setWordWrap(True)
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(content)

        layout.addStretch()

        # Кнопка возврата
        back_btn = QPushButton("← Назад к разделам математики")
        back_btn.clicked.connect(self.main_window.show_main_page)
        layout.addWidget(back_btn)

        self.setLayout(layout)


class MathApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_page = None
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 1000, 700)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.main_page = self.create_main_page()
        self.central_widget.addWidget(self.main_page)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QPushButton {
                background-color: #4a90e2;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #357abd;
                border: 2px solid #2a5d8a;
            }
            QPushButton:pressed {
                background-color: #2a5d8a;
            }
            QLabel {
                color: #2c3e50;
            }
            QGroupBox {
                border: 2px solid #3498db;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
                font-weight: bold;
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
                color: #2c3e50;
            }
        """)

        self.show_main_page()


    def create_main_page(self):
        widget = QWidget()
        layout = QVBoxLayout()


        buttons_layout = QGridLayout()
        buttons_layout.setSpacing(25)
        buttons_layout.setContentsMargins(30, 30, 30, 30)

        # Кнопки разделов
        self.math_analysis_btn = self.create_section_button(
            "Математический анализ",
            "#236583"
        )
        self.math_analysis_btn.clicked.connect(self.show_math_analysis)
        buttons_layout.addWidget(self.math_analysis_btn, 0, 0)

        self.analytic_geom_btn = self.create_section_button(
            "Аналитическая геометрия",
            "#236583"
        )
        self.analytic_geom_btn.clicked.connect(self.show_analytic_geometry)
        buttons_layout.addWidget(self.analytic_geom_btn, 0, 1)

        self.linear_algebra_btn = self.create_section_button(
            "Линейная алгебра",
            "#236583"
        )
        self.linear_algebra_btn.clicked.connect(self.show_linear_algebra)
        buttons_layout.addWidget(self.linear_algebra_btn, 1, 0, 1, 2)

        layout.addLayout(buttons_layout)
        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def create_section_button(self, title, color):
        button = QPushButton()
        button.setMinimumHeight(120)
        button.setCursor(Qt.CursorShape.PointingHandCursor)

        button_text = f"""
            {title}
        """
        button.setText(button_text)

        button.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                          stop: 0 {color}, stop: 1 {self.darken_color(color)});
                border-radius: 15px;
                text-align: center;
                padding: 25px;
                border: 3px solid {self.lighten_color(color)};
                color: white;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                          stop: 0 {self.lighten_color(color)}, 
                                          stop: 1 {color});
                border: 3px solid white;
            }}
            QPushButton:pressed {{
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                          stop: 0 {self.darken_color(color)}, 
                                          stop: 1 {color});
            }}
        """)

        return button

    def darken_color(self, hex_color):
        r = int(hex_color[1:3], 16) - 40
        g = int(hex_color[3:5], 16) - 40
        b = int(hex_color[5:7], 16) - 40

        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        return f'{r:02x}{g:02x}{b:02x}'

    def lighten_color(self, hex_color):
        r = min(255, int(hex_color[1:3], 16) + 40)
        g = min(255, int(hex_color[3:5], 16) + 40)
        b = min(255, int(hex_color[5:7], 16) + 40)

        return f'{r:02x}{g:02x}{b:02x}'

    def show_main_page(self):
        self.central_widget.setCurrentWidget(self.main_page)

    def show_math_analysis(self):
        page = MathAnalysisPage(self)
        self.set_page(page, "Математический анализ")

    def show_analytic_geometry(self):
        page = AnalyticGeometryPage(self)
        self.set_page(page, "Аналитическая геометрия")

    def show_linear_algebra(self):
        page = LinearAlgebraPage(self)
        self.set_page(page, "Линейная алгебра")

    def set_page(self, page, title):
        for i in range(self.central_widget.count()):
            if self.central_widget.widget(i) == page:
                self.central_widget.setCurrentWidget(page)
                break
        else:
            self.central_widget.addWidget(page)
            self.central_widget.setCurrentWidget(page)

        self.current_page = page
        self.setWindowTitle(f"{title} - визуальные доказательства по математике")


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MathApp()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()