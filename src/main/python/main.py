from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets, QtCore, QtGui

from gamemain import MainWindow

import sys

class Startup(QtWidgets.QWidget):
    def __init__(self, appctxt):
        super().__init__()
        self.appctxt = appctxt
        self.setWindowFlags(QtGui.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()

        self.g_layout = QtWidgets.QVBoxLayout(self)
        self.g_layout.setAlignment(QtCore.Qt.AlignHCenter)

        self.lbl_aind = QtWidgets.QLabel("AINDUSTRIES")
        self.lbl_pres = QtWidgets.QLabel("Presents:")
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

        self.txtchange = QtCore.QTimer()
        self.txtchange.setSingleShot(True)
        self.txtchange.setInterval(2000)
        self.txtchange.timeout.connect(self.txtchange_)
        self.txtchange.start()

        self.animgroup.addAnimation(self.lineanim_size)
        self.animgroup.addAnimation(self.posanim)
        self.animgroup.addAnimation(self.sizeanim)
        self.animgroup.addAnimation(self.lineanim_pos)
        self.animgroup.start()

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.setInterval(4500)
        self.timer.timeout.connect(self.main)
        self.timer.start()

    def main(self):
        self.main_window = MainWindow(self.appctxt)
        self.main_window.showFullScreen()
        self.close()
    
    def txtchange_(self):
        self.op = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.op)

        self.txt_change = QtCore.QPropertyAnimation(self.op, b"opacity")
        self.txt_change.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.txt_change.setStartValue(1)
        self.txt_change.setEndValue(0)
        self.txt_change.setDuration(500)

        self.txt_changeb = self.txt_change
        self.txt_changeb.setStartValue(0)
        self.txt_changeb.setEndValue(1)

        self.seq = QtCore.QSequentialAnimationGroup()
        self.seq.addPause(0)
        self.seq.addAnimation(self.txt_change)
        self.seq.addAnimation(self.txt_changeb)
        self.timerc = QtCore.QTimer()
        self.timerc.setSingleShot(True)
        self.timerc.setInterval(100)
        self.timerc.timeout.connect(self.change_text_)
        self.timerc.start()
        self.seq.start()

    def change_text_(self):
        self.lbl_aind.setText("Cmd Prompt")
        self.lbl_pres.setText("")
        self.line.setStyleSheet("QFrame {background-color: rgba(1,1,1,0);}")

#For actual program launch:
if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = Startup(appctxt)
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)