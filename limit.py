import numpy as np
from manim import *

class Example(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([248, 249, 250])
        #axes - оси
        axes= Axes (
            x_range=[-6, 6, 1],#диапазон для x с шагом 1
            y_range=[-9, 9, 1],
            x_length=14,
            y_length=14,
            axis_config={"color": BLACK},#цвет системы координат
            x_axis_config={"color":BLACK,
                'numbers_to_include': np.arange(-6, 6, 1),#координаты будут показываться на коорд-ой плоскости
                'numbers_with_elongated_ticks': np.arange(-6, 6, 1)
            },#координаты выделяются (длинными поперечными линиями)
            tips=False
        )#определим метки по x и y:
        axes_labels=axes.get_axis_labels()
        #np.sin(x)- ф-ия из библиотеки numpy
        up_graph=axes.plot(lambda x: x+2, x_range=[0, 6], color=PURPLE, stroke_opacity=1.3)
        down_graph=axes.plot(lambda x: -x, x_range=[-6, 0], color=PURPLE, stroke_opacity=1.3)

        #указываем подписи: x_val, direction (c какой стороны от точки появится метка) - позиции подписи
        up_label = axes.get_graph_label(up_graph, "y=x+2", x_val=4, direction=2*DOWN, color=PURPLE)
        up_label.scale(0.8)#метод изменения размера текстовой метки
        down_label = axes.get_graph_label(down_graph, "y=-x", x_val=-4, direction=UR)
        down_label.scale(0.8)

        text_1 = Text('lim f(h) не определён', font_size=28, color=BLACK)
        text_1.move_to(axes.c2p(-3, -3))
        text_2 = Text("h-> 0", font_size=16, color=BLACK)
        text_2.next_to(text_1[:4], DOWN/2)

        plot=VGroup(axes, up_graph, down_graph)
        #VGroup - создание виртуальной группы объектов;
        labels=VGroup(axes_labels, up_label, down_label, text_1, text_2)

        # горизонтальная линия (справа)
        hor_line_r = DashedLine(
            start=axes.c2p(-1, 3),
            end=axes.c2p(3, 3),
            color=BLACK
        )
        # вертикальная линия (справа)
        ver_line_r = DashedLine(
            start=axes.c2p(1, 1),
            end=axes.c2p(1, 5),
            color=BLACK
        )

        # горизонтальная линия (слева)
        hor_line_l = DashedLine(
            start=axes.c2p(-3, 1),
            end=axes.c2p(1, 1),
            color=BLACK
        )
        # вертикальная линия (слева)
        ver_line_l = DashedLine(
            start=axes.c2p(-1, -1),
            end=axes.c2p(-1, 3),
            color=BLACK
        )
        lines = VGroup(hor_line_r, ver_line_r, hor_line_l, ver_line_l)
        self.play(Create(plot))
        self.play(Create(labels))
        self.wait(2)
        self.play(Create(lines))
        self.wait(2)

        #горизонтальная линия (справа) после перемещения
        hor_line_r_1 = DashedLine(
            start=axes.c2p(-2, 2),
            end=axes.c2p(2, 2),
            color=BLACK
        )
        # вертикальная линия (справа) после перемещения
        ver_line_r_1 = DashedLine(
            start=axes.c2p(0.04, 0),
            end=axes.c2p(0.04, 4),
            color=BLACK
        )
        # горизонтальная линия (слева) после перемещения
        hor_line_l_1 = DashedLine(
            start=axes.c2p(-2, 0),
            end=axes.c2p(2, 0),
            color=BLACK
        )
        # вертикальная линия (слева) после перемещения
        ver_line_l_1 = DashedLine(
            start=axes.c2p(-0.04, -2),
            end=axes.c2p(-0.04, 2),
            color=BLACK
        )
        lines_1 = VGroup(hor_line_r_1, ver_line_r_1, hor_line_l_1, ver_line_l_1)

        text_3 = Text('   Если мы сжимаем промежуток аргумента, \n'
                      'промежуток значений функции не стягивается\n'
                      '    к какой-то одной конкретной точке\n', font_size=20, color=BLACK)
        text_3.move_to(axes.c2p(3, -2))

        self.play(
            ReplacementTransform(lines, lines_1),
            Write(text_3),
            run_time=6
        )
        self.wait(5)