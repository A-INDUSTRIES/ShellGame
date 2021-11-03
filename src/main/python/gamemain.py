from PySide2 import QtWidgets, QtCore, QtGui

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
        self.sys_layout = QtWidgets.QGridLayout()
        self.glay.addLayout(self.sys_layout, 1,1,1,1)