import sys
from PyQt4 import QtGui


class myForm(QtGui.QWidget):
    def __init__(self):
        super(myForm, self).__init__()
        # This is Layout vbox and hbox

        button1 = QtGui.QPushButton("Trsnsposition")
        button2 = QtGui.QPushButton("Affine")
        button3 = QtGui.QPushButton("Rsa")
         # button action click
        button1.clicked.connect(self.button1Action)
        button2.clicked.connect(self.button2Action)
        button3.clicked.connect(self.button3Action)



        mainwindow = QtGui.QVBoxLayout()

        mainwindow.addWidget(button1)
        mainwindow.addWidget(button2)
        mainwindow.addWidget(button3)

        self.setLayout(mainwindow)

        self.setGeometry(300, 200, 400, 400)
        #self.move(500,500)

        self.setWindowTitle("Security")

        self.show()

    def button1Action(self):
        print("Done Click1")

    def button2Action(self):
        print("Done Click2")

    def button3Action(self):
        print("Done Click3")

app = QtGui.QApplication(sys.argv)

window = myForm()
status = app.exec_()

sys.exit(status)
