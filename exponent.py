import numpy as np
from manim import *

class Example(Scene):
    def construct(self):
        #axes - оси
        axes= Axes (
            x_range=[-6, 6, 2],#диапазон для x с шагом 1
            y_range=[-6, 6, 2],
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
        #np.exp(x)- ф-ия из библиотеки numpy
        exp_graph=axes.plot(lambda x: np.exp(x)-1, color=BLUE, stroke_opacity=0.3)
        lin_graph=axes.plot(lambda x: x, color=GREEN, stroke_opacity=0.3)

        #указываем подписи: x_val, direction (c какой стороны от точки появится метка) - позиции подписи
        exp_label = axes.get_graph_label(exp_graph, "e^x-1", x_val=-6, direction=DOWN)
        lin_label = axes.get_graph_label(lin_graph, "y=x", x_val=4, direction=DOWN)

        plot=VGroup(axes, exp_graph, lin_graph)
        #VGroup - создание виртуальной группы объектов;
        labels=VGroup(axes_labels, exp_label, lin_label)

        #создаем прямоугольник с зоной приближения
        rect = Rectangle(
            color=YELLOW,
            stroke_opacity=0.2,
            height=1.5,  # высота
            width=2
        )
        rect.move_to(axes.c2p(0, 0))  # c2p- преобразует в координаты графика

        self.play(Create(plot))
        self.play(Create(labels))
        self.play(Create(rect))
        self.wait(4)

        #создаем новые оси (для трансформации)
        axes_zoom = Axes(
            x_range=[-2, 2, 0.5],  # диапазон для x с шагом 0.2
            y_range=[-2, 2, 0.5],
            x_length=12,
            y_length=6,
            axis_config={"color": GREEN},  # цвет системы координат
            x_axis_config={
                'numbers_to_include': np.arange(-2, 2, 0.5),  # координаты будут показываться на коорд-ой плоскости
                'numbers_with_elongated_ticks': np.arange(-2, 2, 1)
            },  # координаты выделяются (длинными поперечными линиями)
            tips=False
        )
        lin_zoom = axes_zoom.plot(lambda x: x, color=GREEN, stroke_opacity=0.3)
        exp_zoom=axes_zoom.plot(lambda x: np.exp(x)-1, color=BLUE, stroke_opacity=0.3)

        exp_zoom_label = axes_zoom.get_graph_label(exp_zoom, "e^x", x_val=-1.7, direction=DOWN)
        lin_zoom_label = axes_zoom.get_graph_label(lin_zoom, "y=x", x_val=1.3, direction=DOWN)

        rect_zoom = Rectangle(
            color=YELLOW,
            stroke_opacity=0.2,
            height=4.5,  # высота
            width=6
        )
        rect_zoom.move_to(axes_zoom.c2p(0, 0))

        text= Text("exp(x)~x при x->0", font_size=48)
        text.to_edge(DOWN)#добавляем подпись снизу
        self.play(
            ReplacementTransform(axes, axes_zoom),
            ReplacementTransform(exp_graph, exp_zoom),
            ReplacementTransform(lin_graph, lin_zoom),
            ReplacementTransform(exp_label, exp_zoom_label),
            ReplacementTransform(lin_label, lin_zoom_label),
            ReplacementTransform(rect, rect_zoom),
            Write(text),
            run_time=6
        )
        self.wait(5)