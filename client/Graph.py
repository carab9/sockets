from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from RunLR import RunLR

class Graph:
    def __init__(self, window):
        self.data = None
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.plot = self.fig.add_subplot()
        self.window = window
        self.canvas = FigureCanvasTkAgg(self.fig, master=window)

    def display_lin_reg(self, df, col1, col2):
        self.data = df
        print('Linear Regression result:')

        lr = RunLR()
        lr.run(self.data, col1, col2)
        intercept = lr.get_intercept()
        slope = lr.get_slope()
        print('intercept:', intercept)
        print('slope:', slope)

        x = self.data[self.data.columns[col1]].to_numpy()
        y = self.data[self.data.columns[col2]].to_numpy()

        # clear out previous plot
        self.plot.clear()
        self.plot.scatter(x, y, color="blue")
        y_pred = intercept + slope * x
        self.plot.plot(x, y_pred, color="green")

        self.plot.set_xlabel(self.data.columns[col1])
        self.plot.set_ylabel(self.data.columns[col2])
        self.plot.set_title(self.data.columns[col2] + "/" + self.data.columns[col1])

        # Show plot
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()