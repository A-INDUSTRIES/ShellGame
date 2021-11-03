from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets, QtCore, QtGui

import sys

class Startup(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtGui.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()

        self.g_layout = QtWidgets.QVBoxLayout(self)
        self.g_layout.setAlignment(QtCore.Qt.AlignHCenter)

        self.lbl_aind = QtWidgets.QLabel("AINDUSTRIES")
        self.lbl_pres = QtWidgets.QLabel("Presents to you...")
        self.lbl_aind.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.lbl_aind.setFont(QtGui.QFont("Nimbus Mono PS", 60))
        self.lbl_pres.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.lbl_pres.setFont(QtGui.QFont("DejaVu Sans, Extralight", 21))

        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setStyleSheet("QFrame {background-color: red;}")

        self.setStyleSheet("QLabel {color: red}")

        self.g_layout.addWidget(self.lbl_aind)
        self.g_layout.addWidget(self.line)
        self.g_layout.addWidget(self.lbl_pres)
        
        self.animgroup = QtCore.QParallelAnimationGroup()

        self.lineanim_size = QtCore.QPropertyAnimation(self.line, b"size")
        self.lineanim_size.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.lineanim_size.setStartValue(QtCore.QSize(0, 3))
        self.lineanim_size.setEndValue(QtCore.QSize(538, 3))
        self.lineanim_size.setDuration(1000)

        self.lineanim_pos = QtCore.QPropertyAnimation(self.line, b"pos")
        self.lineanim_pos.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.lineanim_pos.setStartValue(QtCore.QPoint(670, 370))
        self.lineanim_pos.setEndValue(QtCore.QPoint(415, 370))
        self.lineanim_pos.setDuration(1000)

        self.posanim = QtCore.QPropertyAnimation(self.lbl_pres, b"pos")
        self.posanim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.posanim.setStartValue(QtCore.QPoint(415,370))
        self.posanim.setEndValue(QtCore.QPoint(415,390))
        self.posanim.setDuration(1000)

        self.sizeanim = QtCore.QPropertyAnimation(self.lbl_pres, b"size")
        self.sizeanim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.sizeanim.setStartValue(QtCore.QSize(537, 0))
        self.sizeanim.setEndValue(QtCore.QSize(537, 60))
        self.sizeanim.setDuration(1000)

        self.animgroup.addAnimation(self.lineanim_size)
        self.animgroup.addAnimation(self.posanim)
        self.animgroup.addAnimation(self.sizeanim)
        self.animgroup.addAnimation(self.lineanim_pos)
        self.animgroup.start()

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.setInterval(1250)
        self.timer.timeout.connect(self.main)
        self.timer.start()

    def main(self):
        self.main_window = MainWindow()
        self.main_window.showFullScreen()
        self.close()

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Startup()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)