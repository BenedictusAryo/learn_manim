from manim import *

class SequencePlot(GraphScene):
    CONFIG = {
        "y_axis_label": r"Concentration [\%]",
        "x_axis_label": "Time [s]",
        }

    def construct(self):
        data = [1, 2, 2, 4, 4, 1, 3]
        self.setup_axes()
        for time, dat in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(time, dat))
            self.add(dot)