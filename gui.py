import sys
from PyQt4 import QtGui


app=QtGui.QApplication(sys.argv)

w1=QtGui.QWidget()
w1.resize(250,150)
w1.setToolTip("This is ToolTip")
w1.move(300,300)
w1.setWindowTitle("First One ")
w1.show()



w2=QtGui.QWidget()
w2.setWindowTitle("second One ")
w2.show()
status=app.exec_()

sys.exit(status)


