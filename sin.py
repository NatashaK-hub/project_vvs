import numpy as np
from manim import *

class Example(Scene):
    def construct(self):
        #axes - оси
        axes= Axes (
            x_range=[-6, 6, 1],#диапазон для x с шагом 1
            y_range=[-6, 6, 1],
            x_length=14,
            y_length=10,
            axis_config={"color": GREEN},#цвет системы координат
            x_axis_config={
                'numbers_to_include': np.arange(-6, 6, 1),#координаты будут показываться на коорд-ой плоскости
                'numbers_with_elongated_ticks': np.arange(-6, 6, 1)
            },#координаты выделяются (длинными поперечными линиями)
            tips=False
        )#определим метки по x и y:
        axes_labels=axes.get_axis_labels()
        #np.sin(x)- ф-ия из библиотеки numpy
        sin_graph=axes.plot(lambda x: np.sin(x), color=BLUE, stroke_opacity=0.2)
        lin_graph=axes.plot(lambda x: x, color=GREEN, stroke_opacity=0.2)

        #указываем подписи: x_val, direction (c какой стороны от точки появится метка) - позиции подписи
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)", x_val=-5, direction=UP / 2)
        lin_label = axes.get_graph_label(lin_graph, "y=x", x_val=2, direction=UP)

        plot=VGroup(axes, sin_graph, lin_graph)
        #VGroup - создание виртуальной группы объектов;
        labels=VGroup(axes_labels, sin_label, lin_label)

        self.play(Create(plot))
        self.play(Create(labels))
        self.wait(2)

        axes_zoom = Axes(
            x_range=[-2, 2, 0.2],  # диапазон для x с шагом 0.2
            y_range=[-2, 2, 0.2],
            x_length=14,
            y_length=10,
            axis_config={"color": GREEN},  # цвет системы координат
            x_axis_config={
                'numbers_to_include': np.arange(-2, 2, 0.2),  # координаты будут показываться на коорд-ой плоскости
                'numbers_with_elongated_ticks': np.arange(-2, 2, 1)
            },  # координаты выделяются (длинными поперечными линиями)
            tips=False
        )
        lin_zoom = axes.plot(lambda x: x, color=GREEN, stroke_opacity=0.2)
        sin_zoom=axes_zoom.plot(lambda x: np.sin(x), color=BLUE, stroke_opacity=0.2)
        text= Text("sin(x) ~x при x->0", font_size=48)
        text.to_edge(DOWN)#добавляем текст вниз
        self.play(
            ReplacementTransform(axes, axes_zoom),
            ReplacementTransform(sin_graph, sin_zoom),
            ReplacementTransform(lin_graph, lin_zoom),
            Write(text),
            run_time=6
        )
        self.wait(5)
