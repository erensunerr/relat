import ui, sys, relat
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
# -*- coding: utf-8 -*-


class TheMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()



class QApplication(QtWidgets.QApplication):
    pass

app = QApplication(sys.argv)
MainWindow = TheMainWindow()
MainWindow.setWindowTitle("Heyy")
isFull = False

class Ui_MainWindow(ui.Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.addRelat.clicked.connect(bF_addRelat)
        self.addNode.clicked.connect(bF_addNode)
        self.pickColor.clicked.connect(bF_pickColor)
        self.actionSave.triggered.connect(tF_save)
        self.actionNew.triggered.connect(tF_new)
        self.actionSave_as.triggered.connect(tF_saveAs)
        self.actionOpen.triggered.connect(tF_open)
        self.actionOpen_Help.triggered.connect(tF_help)
        self.actionFullscreen.triggered.connect(self.asdFullsc)

    def retranslateUi(self, MainWindow):
        super().retranslateUi( MainWindow)

    def asdFullsc(self,a):
        global MainWindow, isFull
        if not(isFull):
            MainWindow.showFullScreen()
            isFull = True
        else:
            MainWindow.showMaximized()
            isFull = False

class graphManager():
    def __init__():
        pass

    def addRelat(relat):
        pass

    def addNode(node):
        pass

    def delNode(node):
        pass

    def delRelat(relat):
        pass


def bF_addRelat():
    print('Add relationship button has been clicked.')
    #add relationship button
    pass

def bF_pickColor():
    print('Pick color button has been clicked.')
    color = QtWidgets.QColorDialog.getColor().name().upper()
    print("The selected color is:",color)
    #pick color button

def bF_addNode():
    print('Add node button has been clicked.')
    #add node button
    pass

def tF_save():
    print('Save toolbar function has been clicked.')
    #save toolbar button
    pass

def tF_open():
    print('Open toolbar function has been clicked.')
    #new toolbar button
    pass

def tF_new():
    print('New toolbar function has been clicked.')
    #new toolbar button
    pass

def tF_saveAs():
    print('Save as toolbar function has been clicked.')
    #save as toolbar function
    pass

def tF_help():
    print('Help toolbar function has been clicked.')
    #help toolbar function
    pass


mainWinUi = Ui_MainWindow()
mainWinUi.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
