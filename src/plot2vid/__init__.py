import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import cv2
import numpy as np
import math

__version__ = "1.0.3"


class PlotRecorder():
    def __init__(self, destination: str, fps=30):
        self.destination = destination
        self.fps = fps

        self.writer = None

        self.width = None
        self.height = None

    def add(self, figure):
        image = self.__plot_to_image(figure)
        height, width, depth = image.shape

        if self.writer is None:
            self.width = width
            self.height = height

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.writer = cv2.VideoWriter(
                self.destination, fourcc, self.fps, (width, height))

        if self.width != width or self.height != height:
            print(
                f"[plot2vid] Provided plot has dimensions {width, height} instead of {self.width, self.height} as previously added plots. Skipping this frame in the recording")
            return

        self.writer.write(image)

    def close(self):
        self.writer.release()

    def __plot_to_image(self, figure):
        canvas = FigureCanvasAgg(figure)
        canvas.draw()
        s, (width, height) = canvas.print_to_buffer()
        image = np.frombuffer(s, np.uint8).reshape((height, width, 4))
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

        return image
