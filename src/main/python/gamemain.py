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

        self.qss = self.appctxt.get_resource("gamemain.qss")
        with open(self.qss, "r") as f:
            self.setStyleSheet(f.read())
            f.close()

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
        self.taskbar.setObjectName("taskbar")
        self.taskbar.setFixedHeight(30)

        self.btn_start = QtWidgets.QPushButton(" start")
        self.btn_start.setObjectName("btn_start")
        self.btn_start.setFixedSize(90,30)
        self.btn_start.setIcon(QtGui.QIcon(QtGui.QPixmap(self.appctxt.get_resource("winxp.png"))))
        self.btn_start.clicked.connect(self._sh_menu)

        self.sys_layout.addWidget(self.taskbar, 90,1,1,160)
        self.sys_layout.addWidget(self.btn_start, 90,1,1,1)

    def __init_menu_layout(self):
        self.menu_layout = QtWidgets.QGridLayout()
        self.menu_layout.setMargin(0)

        self.menu_profile_pic = QtWidgets.QLabel()
        self.menu_profile_pic.setFixedSize(50,50)
        self.menu_profile_pic.setObjectName("menu_pp")
        self.menu_profile_pic.setStyleSheet("QLabel#menu_pp {background-image: url(" + self.appctxt.get_resource("usr-pic.png") + ")}")

        self.menu_usr_name = QtWidgets.QLabel("User")
        self.menu_usr_name.setObjectName("usr_name")
        self.menu_usr_name.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)

        self.menu_quick_app = QtWidgets.QWidget()
        self.menu_quick_app_layout = QtWidgets.QGridLayout()
        self.menu_quick_app.setLayout(self.menu_quick_app_layout)
        self.menu_quick_app.setObjectName("mqa")
        self.menu_quick_app_layout.setMargin(0)

        self.__init_quick_apps()

        self.menu_layout.addWidget(self.menu_profile_pic, 1,1,1,1)
        self.menu_layout.addWidget(self.menu_usr_name, 1,2,1,7)
        self.menu_layout.addWidget(self.menu_quick_app, 2,1,1,4)

        self.menu = QtWidgets.QWidget()
        self.menu.setLayout(self.menu_layout)
        self.menu.setHidden(True)
        self.menu.setObjectName("menu")

        self.sys_layout.addWidget(self.menu, 80,1,1,1)

    def __init_quick_apps(self):
        # mqa = menu_quick_app
        self.mqa_internet = QtWidgets.QPushButton("Internet\nInternet Explorer")
        self.mqa_internet.setObjectName("mqa_internet")
        self.mqa_internet.setIcon(QtGui.QIcon(QtGui.QPixmap(self.appctxt.get_resource("internet.png"))))
        self.mqa_internet.setIconSize(QtCore.QSize(35,35))
        self.menu_quick_app_layout.addWidget(self.mqa_internet, 1,1,2,2)

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