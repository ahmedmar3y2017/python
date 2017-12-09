import sys
from PyQt4 import QtCore, QtGui, uic


class MyWidget(QtGui.QWidget):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self)
    


class TabWidget(QtGui.QTabWidget):
  def __init__(self, parent=None):
    super(TabWidget, self).__init__(parent)
    self.setTabsClosable(True)
    self.tabCloseRequested.connect(self.removeTab)
    self.inside = MyWidget()

  def tabInserted(self, index):
    self.tabBar().setVisible(self.count() > 1)

  def tabRemoved(self, index):
    self.tabBar().setVisible(self.count() > 1)


class MainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QMainWindow.__init__(self, parent)


def main():
  qApp = QtGui.QApplication(sys.argv)

  tab = TabWidget()

  button = QtGui.QPushButton('Hello')

  @button.clicked.connect
  def clicked():
    tab.addTab(QtGui.QLabel('Hello'), 'Hello')

  tab.addTab(button, 'Button')

  layout = QtGui.QHBoxLayout()
  layout.addWidget(tab)

  window = QtGui.QWidget()
  window.setLayout(layout)
  window.resize(600, 400)
  window.show()

  qApp.exec_()


if __name__ == "__main__":
  main()
