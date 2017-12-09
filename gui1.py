import sys
from PyQt4 import QtGui



class myForm(QtGui.QWidget):
    def __init__(self):
        super(myForm, self).__init__()

        # This is Layout vbox and hbox
        # button1 = QtGui.QPushButton("Button1")
        # button2 = QtGui.QPushButton("Button2")
        # button3 = QtGui.QPushButton("Button3")

        # label1 = QtGui.QLabel("Label1")
        # label2 = QtGui.QLabel("Label2")
        # label3 = QtGui.QLabel("Label3")

        # layout1 = QtGui.QVBoxLayout()
        # layout1.addWidget(button1)
        # layout1.addWidget(button2)
        # layout1.addWidget(button3)

        # layout2 = QtGui.QVBoxLayout()
        # layout2.addWidget(label1)
        # layout2.addWidget(label2)
        # layout2.addWidget(label3)

        # mainlayout=QtGui.QHBoxLayout()
        # mainlayout.addLayout(layout2)
        # mainlayout.addLayout(layout1)

        # Grid layout
        # label1=QtGui.QLabel("Email")
        # label2=QtGui.QLabel("Address")
        # label3=QtGui.QLabel("Password")
        # label4=QtGui.QLabel("Gender")

        # email=QtGui.QLineEdit()
        # address=QtGui.QLineEdit()
        # password=QtGui.QLineEdit()
        # gender=QtGui.QComboBox()
        # gender.addItems(['male','female'])

        # mainlayout=QtGui.QGridLayout()

        # mainlayout.addWidget(label1,0,0)
        # mainlayout.addWidget(label2,1,0)
        # mainlayout.addWidget(label3,2,0)
        # mainlayout.addWidget(label4,3,0)

        # mainlayout.addWidget(email,0,1)
        # mainlayout.addWidget(address,1,1)
        # mainlayout.addWidget(password,2,1)
        # mainlayout.addWidget(gender,3,1)

        # Button Click 
        # email = QtGui.QLineEdit()
        # address = QtGui.QLineEdit()
        # password = QtGui.QLineEdit()
        # gender = QtGui.QComboBox()
        # gender.addItems(['male', 'female'])
        # button = QtGui.QPushButton("Click")
        # self.label = QtGui.QLabel("Done")

        # mainwindow = QtGui.QFormLayout()
        # mainwindow.addRow("Email : ", email)
        # mainwindow.addRow("address : ", address)
        # mainwindow.addRow("password : ", password)
        # mainwindow.addRow("gender : ", gender)
        # mainwindow.addRow(button)
        # mainwindow.addRow(self.label)

        # # button action click 
        # button.clicked.connect(self.buttonAction)
        # self.label1=QtGui.QLabel("1")
        # self.label2=QtGui.QLabel("2")
        # self.label3=QtGui.QLabel("3")
        # button = QtGui.QPushButton("Click")
        # button.clicked.connect(self.handlerClick)
        # button.released.connect(self.handlerRelease)
        # button.pressed.connect(self.handlerPress)


        # mainwindow=QtGui.QVBoxLayout()
        # mainwindow.addWidget(self.label1)
        # mainwindow.addWidget(self.label2)
        # mainwindow.addWidget(self.label3)
        # mainwindow.addWidget(button)


        # Slider
        mainwindow=QtGui.QVBoxLayout()
        self.lcd=QtGui.QLCDNumber()

        self.slider=QtGui.QSlider()
        self.slider.valueChanged.connect(self.lcd.display)



        mainwindow.addWidget(self.lcd)
        mainwindow.addWidget(self.slider)



        self.setLayout(mainwindow)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("My First App")
        self.show()

    def buttonAction(self):
        print("Done Click")
        self.label.setText("Done Click")
        #Button handler Actions 
    def handlerPress(self):
        self.label1.setText("press")
    def handlerRelease(self):
        self.label2.setText("Release")
    def handlerClick(self):
        self.label3.setText("Click")




app = QtGui.QApplication(sys.argv)

mainwindow = myForm()

status = app.exec_()

sys.exit(status)
