import sys
# from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from math import sqrt, sin
from plot_to_func_design import Ui_MainWindow


class PlotToFunc(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('plot_to_func_design.ui', self)
        self.setupUi(self)
        self.setWindowTitle('Нахождение функции по графику')
        self.delButton.clicked.connect(self.clear)
        self.plotWidget.scene().sigMouseMoved.connect(self.mouse_moved)
        self.plotWidget.scene().sigMouseClicked.connect(self.mouse_clicked)
        self.count = 0
        self.show()

    def mouse_moved(self, event):
        point = event.toPoint()
        mouse_point = self.plotWidget.plotItem.vb.mapSceneToView(point)
        self.x, self.y = round(mouse_point.x(), 2), round(mouse_point.y(), 2)
        self.coordsEdit.setText('x: {0}, y: {1}'.format(self.x, self.y))

    def mouse_clicked(self, event):
        self.set_color()
        if self.radioButton.isChecked():
            self.point()
            self.count += 1
            if self.count == 1:
                self.x1, self.y1 = self.x, self.y
            elif self.count == 2:
                self.line(self.x1, self.y1, self.x, self.y)
                self.count = 0
        elif self.radioButton_4.isChecked():
            self.point()
            self.count += 1
            if self.count == 1:
                self.x1, self.y1 = self.x, self.y
            elif self.count == 2:
                self.x2, self.y2 = self.x, self.y
            else:
                self.square_func(self.x1, self.y1, self.x2, self.y2, self.x, self.y)
                self.count = 0
        elif self.radioButton_2.isChecked():
            self.point()
            self.sqrt_func(self.x, self.y)
        elif self.radioButton_3.isChecked():
            self.point()
            self.module_func(self.x, self.y)
        elif self.radioButton_5.isChecked():
            self.point()
            self.cubic_func(self.x, self.y)
        elif self.radioButton_6.isChecked():
            self.point()
            self.sin_func(self.x, self.y)

    def set_color(self):
        if self.white.isChecked():
            self.color = 'w'
        elif self.red.isChecked():
            self.color = 'r'
        elif self.green.isChecked():
            self.color = 'g'
        elif self.blue.isChecked():
            self.color = 'b'

    def point(self):
        self.plotWidget.plot((self.x, self.x), (self.y, self.y), symbolPen=self.color, symbol='o')

    def clear(self):
        self.plotWidget.clear()
        self.funcEdit.clear()

    def line(self, x1, y1, x2, y2):
        self.plotWidget.plot((x1, x2), (y1, y2), pen=self.color)

        try:
            k = round((y1 - y2) / (x1 - x2), 2)
        except ZeroDivisionError:
            self.funcEdit.setText('Невозможно вычислить: деление на ноль')
            return
        b = round(y2 - k * x2, 2)

        if k == 0:
            eq = 'y = {}'.format(b)
        elif k == 1:
            if b < 0:
                eq = 'y = x - {}'.format(-b)
            elif b == 0:
                eq = 'y = x'
            else:
                eq = 'y = x + {}'.format(b)
        elif k == -1:
            if b < 0:
                eq = 'y = -x - {}'.format(-b)
            elif b == 0:
                eq = 'y = -x'
            else:
                eq = 'y = -x + {}'.format(b)
        elif b < 0:
            eq = 'y = {0}x - {1}'.format(k, -b)
        elif b == 0:
            eq = 'y = {0}x'.format(k)
        else:
            eq = 'y = {0}x + {1}'.format(k, b)

        self.funcEdit.setText(eq)

    def square_func(self, x1, y1, x2, y2, x3, y3):
        pass

    def sqrt_func(self, x, y):
        a, xs = 0, []
        while a <= 10:
            xs.append(a)
            a += 0.01
        ys = [sqrt(el) for el in xs]
        xs = [el + x for el in xs]
        ys = [el + y for el in ys]

        self.plotWidget.plot(xs, ys, pen=self.color)

        if x == 0:
            if y < 0:
                eq = 'y = sqrt(x) - {}'.format(-y)
            elif y == 0:
                eq = 'y = sqrt(x)'
            else:
                eq = 'y = sqrt(x) + {}'.format(y)
        elif x < 0:
            if y < 0:
                eq = 'y = sqrt(x + {0}) - {1}'.format(-x, -y)
            elif y == 0:
                eq = 'y = sqrt(x + {})'.format(-x)
            else:
                eq = 'y = sqrt(x + {0}) + {1}'.format(-x, y)
        else:
            if y < 0:
                eq = 'y = sqrt(x - {0}) - {1}'.format(x, -y)
            elif y == 0:
                eq = 'y = sqrt(x - {})'.format(x)
            else:
                eq = 'y = sqrt(x - {0}) + {1}'.format(x, y)

        self.funcEdit.setText(eq)

    def module_func(self, x, y):
        xs = range(-10, 11)
        ys = [abs(el) for el in xs]
        xs = [el + x for el in xs]
        ys = [el + y for el in ys]

        self.plotWidget.plot(xs, ys, pen=self.color)

        if x == 0:
            if y < 0:
                eq = 'y = |x| - {}'.format(-y)
            elif y == 0:
                eq = 'y = |x|'
            else:
                eq = 'y = |x| + {}'.format(y)
        elif x < 0:
            if y < 0:
                eq = 'y = |x + {0}| - {1}'.format(-x, -y)
            elif y == 0:
                eq = 'y = |x + {}|'.format(-x)
            else:
                eq = 'y = |x + {0}| + {1}'.format(-x, y)
        else:
            if y < 0:
                eq = 'y = |x - {0}| - {1}'.format(x, -y)
            elif y == 0:
                eq = 'y = |x - {}|'.format(x)
            else:
                eq = 'y = |x - {0}| + {1}'.format(x, y)

        self.funcEdit.setText(eq)

    def cubic_func(self, x, y):
        a, xs = -2.5, []
        while a <= 2.5:
            xs.append(a)
            a += 0.01
        ys = [(el ** 3) for el in xs]
        xs = [el + x for el in xs]
        ys = [el + y for el in ys]

        self.plotWidget.plot(xs, ys, pen=self.color)

        if x == 0:
            if y < 0:
                eq = 'y = x ** 3 - {}'.format(-y)
            elif y == 0:
                eq = 'y = x ** 3'
            else:
                eq = 'y = x ** 3 + {}'.format(y)
        elif x < 0:
            if y < 0:
                eq = 'y = (x + {0}) ** 3 - {1}'.format(-x, -y)
            elif y == 0:
                eq = 'y = (x + {}) ** 3'.format(-x)
            else:
                eq = 'y = (x + {0}) ** 3 + {1}'.format(-x, y)
        else:
            if y < 0:
                eq = 'y = (x - {0}) ** 3 - {1}'.format(x, -y)
            elif y == 0:
                eq = 'y = (x - {}) ** 3'.format(x)
            else:
                eq = 'y = (x - {0}) ** 3 + {1}'.format(x, y)
        self.funcEdit.setText(eq)

    def sin_func(self, x, y):
        a, xs = -10, []
        while a <= 10:
            xs.append(a)
            a += 0.01
        ys = [sin(el) for el in xs]
        xs = [el + x for el in xs]
        ys = [el + y for el in ys]

        self.plotWidget.plot(xs, ys, pen=self.color)

        if x == 0:
            if y < 0:
                eq = 'y = sin(x) - {}'.format(-y)
            elif y == 0:
                eq = 'y = sin(x)'
            else:
                eq = 'y = sin(x) + {}'.format(y)
        elif x < 0:
            if y < 0:
                eq = 'y = sin(x + {0}) - {1}'.format(-x, -y)
            elif y == 0:
                eq = 'y = sin(x + {})'.format(-x)
            else:
                eq = 'y = sin(x + {0}) + {1}'.format(-x, y)
        else:
            if y < 0:
                eq = 'y = sin(x - {0}) - {1}'.format(x, -y)
            elif y == 0:
                eq = 'y = sin(x - {})'.format(x)
            else:
                eq = 'y = sin(x - {0}) + {1}'.format(x, y)

        self.funcEdit.setText(eq)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ptf = PlotToFunc()
    sys.exit(app.exec_())
