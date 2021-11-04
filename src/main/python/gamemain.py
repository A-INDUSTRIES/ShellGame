from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets, QtCore, QtGui

import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self, appctxt):
        super().__init__()
        self.appctxt = appctxt
        self.glay = QtWidgets.QGridLayout(self)
        self.glay.setMargin(0)
        self.img = QtWidgets.QLabel()
        self.screen = QtWidgets.QApplication.instance().primaryScreen().size()
        self.img.setPixmap(QtGui.QPixmap(self.appctxt.get_resource("background.jpg")).scaled(self.screen.width(), self.screen.height()))
        self.glay.addWidget(self.img, 1,1,1,1)
        self.__init_sys_layout()

    def __init_sys_layout(self):
        """Creating another layout to avoid conflict with background"""
        self.sys_layout = QtWidgets.QGridLayout()
        self.glay.addLayout(self.sys_layout, 1,1,1,1)

        """Nul spacer added to layout to force size and
        ensure 16:9 ratio so each 1:1 space is actually a square"""
        self.spacer = QtWidgets.QSpacerItem(0,0)
        self.sys_layout.addItem(self.spacer, 1,1,90,160)

        self.btn_start = QtWidgets.QPushButton(" start")
        self.btn_start.setFixedSize(80,25)
        self.btn_start.setIcon(QtGui.QIcon(QtGui.QPixmap(self.appctxt.get_resource("winxp.png"))))
        self.btn_start.setStyleSheet("""
        QPushButton {
            background-color: green;
            border-top-right-radius: 11px;
            border-bottom-right-radius: 11px;
            font: bold italic;
            color: white;
            } 
        
        QPushButton:pressed {
            background-color: darkgreen;
            }""")

        self.sys_layout.addWidget(self.btn_start, 90,1,1,1)


#For testing purposes:
if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = MainWindow(appctxt)
    window.showFullScreen()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)