import numpy as np
from manim import *

class Example(Scene):
    def construct(self):
        #axes - оси
        axes= Axes (
            x_range=[-6, 6, 1],#диапазон для x с шагом 1
            y_range=[-6, 6, 1],
            x_length=12,
            y_length=6,
            axis_config={"color": GREEN},#цвет системы координат
            x_axis_config={
                'numbers_to_include': np.arange(-6, 6, 1),#координаты будут показываться на коорд-ой плоскости
                'numbers_with_elongated_ticks': np.arange(-6, 6, 1)
            },#координаты выделяются (длинными поперечными линиями)
            tips=False
        )#определим метки по x и y:
        axes_labels=axes.get_axis_labels()
        #np.sin(x)- ф-ия из библиотеки numpy
        cos_graph=axes.plot(lambda x: 1-np.cos(x), color=BLUE, stroke_opacity=0.2)
        lin_graph=axes.plot(lambda x: x**2/2, color=GREEN, stroke_opacity=0.2)

        #указываем подписи: x_val, direction (c какой стороны от точки появится метка) - позиции подписи
        cos_label = axes.get_graph_label(cos_graph, "1-cos(x)", x_val=-4, direction=UP / 2)
        lin_label = axes.get_graph_label(lin_graph, "x^2/2", x_val=2, direction=2*UP)

        plot=VGroup(axes, cos_graph, lin_graph)
        #VGroup - создание виртуальной группы объектов;
        labels=VGroup(axes_labels, cos_label, lin_label)

        self.play(Create(plot))
        self.play(Create(labels))
        self.wait(4)

        #переход к новым осям (смена масштаба)
        axes_zoom = Axes(
            x_range=[-2, 2, 0.3],  # диапазон для x с шагом 0.2
            y_range=[-2, 2, 0.3],
            x_length=12,
            y_length=6,
            axis_config={"color": GREEN},  # цвет системы координат
            x_axis_config={
                'numbers_to_include': np.arange(-2, 2, 0.3),  # координаты будут показываться на коорд-ой плоскости
                'numbers_with_elongated_ticks': np.arange(-2, 2, 1)
            },  # координаты выделяются (длинными поперечными линиями)
            tips=False
        )
        lin_zoom = axes_zoom.plot(lambda x: x**2/2, color=GREEN, stroke_opacity=0.2)
        cos_zoom=axes_zoom.plot(lambda x: 1-np.cos(x), color=BLUE, stroke_opacity=0.2)

        cos_zoom_label = axes_zoom.get_graph_label(cos_zoom, "1-cos(x)", x_val=-1.7, direction=2*DOWN)
        lin_zoom_label = axes_zoom.get_graph_label(lin_zoom, "x^2/2", x_val=1.3, direction=2*UP)

        text= Text("1-cos(x)~x²/2 при x->0", font_size=48)
        text.to_edge(DOWN)#добавляем подпись снизу
        self.play(
            ReplacementTransform(axes, axes_zoom),
            ReplacementTransform(cos_graph, cos_zoom),
            ReplacementTransform(lin_graph, lin_zoom),
            ReplacementTransform(cos_label, cos_zoom_label),
            ReplacementTransform(lin_label, lin_zoom_label),
            Write(text),
            run_time=6
        )
        self.wait(5)
