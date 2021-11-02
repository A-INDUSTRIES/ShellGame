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

        self.setStyleSheet("QLabel {color: red;}")

        self.g_layout.addWidget(self.lbl_aind)
        self.g_layout.addWidget(self.line)
        self.g_layout.addWidget(self.lbl_pres)
        
        self.animgroup = QtCore.QParallelAnimationGroup()

        self.lineanim_size = QtCore.QPropertyAnimation(self.line, b"size")
        self.lineanim_size.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.lineanim_size.setStartValue(QtCore.QSize(0, 3))
        self.lineanim_size.setEndValue(QtCore.QSize(522, 3))
        self.lineanim_size.setDuration(1000)

        self.posanim = QtCore.QPropertyAnimation(self.lbl_pres, b"pos")
        self.posanim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)

        self.animgroup.addAnimation(self.lineanim_size)
        self.animgroup.start()


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Startup()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)