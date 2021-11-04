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
        self.is_menu_shown = False
        self.__init_sys_layout()
        self.__init_menu_layout()

    def __init_sys_layout(self):
        """Creating another layout to avoid conflict with background"""
        self.sys_layout = QtWidgets.QGridLayout()
        self.glay.addLayout(self.sys_layout, 1,1,1,1)

        """Nul spacer added to layout to force size and
        ensure 16:9 ratio so each 1:1 space is actually a square"""
        self.spacer = QtWidgets.QSpacerItem(0,0)
        self.sys_layout.addItem(self.spacer, 1,1,90,160)

        self.taskbar = QtWidgets.QLabel("")
        self.taskbar.setFixedHeight(25)
        self.taskbar.setStyleSheet("""
        QLabel {
            background-color: qlineargradient(x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(29, 78, 175), 
            stop:0.5 rgb(35, 93, 217), stop:1 rgb(29, 78, 175));
        }""")

        self.btn_start = QtWidgets.QPushButton(" start")
        self.btn_start.setFixedSize(80,25)
        self.btn_start.setIcon(QtGui.QIcon(QtGui.QPixmap(self.appctxt.get_resource("winxp.png"))))
        self.btn_start.setStyleSheet("""
        QPushButton {
            background-color: qradialgradient(cx:0.7, cy:0.3, radius: 1,
                fx:1, fy:0, stop:0 rgb(53, 132, 60), stop:1 rgb(34, 86, 40));
            border-top-right-radius: 11px;
            border-bottom-right-radius: 11px;
            font: bold italic;
            color: white;
            } 
        
        QPushButton:pressed {
            background-color: qradialgradient(cx:0.7, cy:0.3, radius: 1,
                fx:1, fy:0, stop:0 rgb(29, 73, 34), stop:1 rgb(27, 68, 31));
            }""")
        self.btn_start.clicked.connect(self._sh_menu)

        self.sys_layout.addWidget(self.taskbar, 90,1,1,160)
        self.sys_layout.addWidget(self.btn_start, 90,1,1,1)

    def __init_menu_layout(self):
        self.menu_layout = QtWidgets.QGridLayout()

        self.menu_profile_pic = QtWidgets.QLabel()
        self.menu_profile_pic.setFixedSize(50,50)
        self.menu_profile_pic.setStyleSheet("""QLabel {border:1px solid white; border-radius:4px; 
        background-image: url(""" + str(self.appctxt.get_resource("usr_pic.png")) + """);}""")

        self.menu_layout.addWidget(self.menu_profile_pic)

        self.menu = QtWidgets.QWidget()
        self.menu.setLayout(self.menu_layout)
        self.menu.setHidden(True)
        self.menu.setObjectName("menu")
        self.menu.setStyleSheet("""QWidget#menu {background: qlineargradient(x1:0.5, y1:1, x2:0.5, y2:0, 
        stop:0 rgb(29, 78, 175), stop:0.5 rgb(35, 93, 217), stop:1 rgb(29, 78, 175))}""")

        self.sys_layout.addWidget(self.menu, 80,1,1,1)

    def _sh_menu(self):
        self.menu.setHidden(self.is_menu_shown)
        if self.is_menu_shown:
            self.is_menu_shown = False
        else:
            self.is_menu_shown = True


#For testing purposes:
if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = MainWindow(appctxt)
    window.showFullScreen()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)