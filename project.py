import sys
# from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from math import sqrt
from qtproject import Ui_MainWindow


class GraphToFunc(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('qtproject.ui', self)
        self.setupUi(self)
        self.setWindowTitle('Нахождение функции по описанию графика')
        self.startButton.clicked.connect(self.run)
        self.show()

    def set_color(self):
        if self.white.isChecked():
            self.color = 'w'
        elif self.red.isChecked():
            self.color = 'r'
        elif self.green.isChecked():
            self.color = 'g'
        elif self.blue.isChecked():
            self.color = 'b'

    def run(self):
        self.set_color()
        if self.radioButton.isChecked():
            self.line_segment()
        elif self.radioButton_2.isChecked():
            self.sqrt_func()
        elif self.radioButton_3.isChecked():
            self.module_func()
        elif self.radioButton_4.isChecked():
            self.square_func()

    def line_segment(self):
        x1, okBtnPressed = QInputDialog.getInt(
            self, "Введите x1", "Чему равен x1?"
        )
        y1, okBtnPressed = QInputDialog.getInt(
            self, "Введите y1", "Чему равен y1?"
        )
        x2, okBtnPressed = QInputDialog.getInt(
            self, "Введите x2", "Чему равен x2?"
        )
        y2, okBtnPressed = QInputDialog.getInt(
            self, "Введите y2", "Чему равен y2?"
        )

        self.plotWidget.clear()
        self.plotWidget.plot((x1, x2), (y1, y2), pen=self.color)

        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        eq = 'y = {0}x + {1}'.format(k, b)
        self.lineEdit.setText(eq)

    def sqrt_func(self):
        x, okBtnPressed = QInputDialog.getInt(
            self, "Введите сдвиг по оси x", "Чему равен сдвиг по оси x?"
        )
        y, okBtnPressed = QInputDialog.getInt(
            self, "Введите сдвиг по оси y", "Чему равен сдвиг по оси y?"
        )

        xs = range(11)
        ys = [sqrt(el) for el in xs]
        xs = [el + x for el in xs]
        ys = [el + y for el in ys]

        self.plotWidget.clear()
        self.plotWidget.plot(xs, ys, pen=self.color)

        eq = 'y = sqrt(x + {0}) + {1}'.format(-x, y)
        self.lineEdit.setText(eq)

    def module_func(self):
        x, okBtnPressed = QInputDialog.getInt(
            self, "Введите сдвиг по оси x", "Чему равен сдвиг по оси x?"
        )
        y, okBtnPressed = QInputDialog.getInt(
            self, "Введите сдвиг по оси y", "Чему равен сдвиг по оси y?"
        )

        xs = range(-10, 11)
        ys = [abs(el) for el in xs]
        xs = [el + x for el in xs]
        ys = [el + y for el in ys]

        self.plotWidget.clear()
        self.plotWidget.plot(xs, ys, pen=self.color)

        eq = 'y = |x + {0}| + {1}'.format(-x, y)
        self.lineEdit.setText(eq)

    def square_func(self):
        x, okBtnPressed = QInputDialog.getInt(
            self, "Введите сдвиг по оси x", "Чему равен сдвиг по оси x?"
        )
        y, okBtnPressed = QInputDialog.getInt(
            self, "Введите сдвиг по оси y", "Чему равен сдвиг по оси y?"
        )

        xs = range(-10, 11)
        ys = [(el ** 2) for el in xs]
        xs = [el + x for el in xs]
        ys = [el + y for el in ys]

        self.plotWidget.clear()
        self.plotWidget.plot(xs, ys, pen=self.color)

        eq = 'y = (x + {0}) ** 2 + {1}'.format(-x, y)
        self.lineEdit.setText(eq)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gtf = GraphToFunc()
    sys.exit(app.exec_())
