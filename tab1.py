import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class tabdemo(QTabWidget):
    def __init__(self, parent=None):
        super(tabdemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("Security")
        self.setGeometry(300, 200, 400, 400)
#Tabs
    def tab1UI(self):
        # enc
        layout = QFormLayout()
        layout.addRow("", QLabel("Encryption"))
        self.plaint = QLineEdit()
        layout.addRow("Plain Text", self.plaint)
        self.key1t = QLineEdit()
        layout.addRow("Key", self.key1t)
        buttons = QHBoxLayout()
        self.b1t = QPushButton("Encryption")
        self.b1t.clicked.connect(lambda: self.trans(
            self.b1t, self.plaint, self.key1t))
        buttons.addWidget(self.b1t)
        layout.addRow(buttons)
        # dec
        layout.addRow("", QLabel("Decryption"))
        self.cyphert = QLineEdit()
        layout.addRow("Cypher Text", self.cyphert)
        self.key2t = QLineEdit()
        layout.addRow("Key", self.key2t)
        buttons = QHBoxLayout()
        self.b2t = QPushButton("Decryption")
        self.b2t.clicked.connect(lambda: self.trans(
            self.b2t, self.cyphert, self.key2t))
        buttons.addWidget(self.b2t)
        layout.addRow(buttons)

        self.setTabText(0, "Transposition")
        self.tab1.setLayout(layout)

    def tab2UI(self):
        # enc
        layout = QFormLayout()
        layout.addRow("", QLabel("Encryption"))
        self.plaina = QLineEdit()
        layout.addRow("Plain Text", self.plaina)
        self.key1a = QLineEdit()
        layout.addRow("Key", self.key1a)
        buttons = QHBoxLayout()
        self.b1a = QPushButton("Encryption")
        self.b1a.clicked.connect(lambda: self.affine(
            self.b1a, self.plaina, self.key1a))
        buttons.addWidget(self.b1a)
        layout.addRow(buttons)
        # dec
        layout.addRow("", QLabel("Decryption"))
        self.cyphera = QLineEdit()
        layout.addRow("Cypher Text", self.cyphera)
        self.key2a = QLineEdit()
        layout.addRow("Key", self.key2a)
        buttons = QHBoxLayout()
        self.b2a = QPushButton("Decryption")
        self.b2a.clicked.connect(lambda: self.affine(
            self.b2a, self.cyphera, self.key2a))
        buttons.addWidget(self.b2a)
        layout.addRow(buttons)

        self.setTabText(1, "Affine")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QFormLayout()
        # Enc
        radios2 = QHBoxLayout()
        self.with1 = QRadioButton("With spaces")
        self.with1.setChecked(True)
        radios2.addWidget(self.with1)
        self.without1 = QRadioButton("Without space")
        radios2.addWidget(self.without1)
        layout.addRow(QLabel("Select"), radios2)
        self.p1rsa = QLineEdit()
        layout.addRow("P", self.p1rsa)
        self.q1rsa = QLineEdit()
        layout.addRow("q", self.q1rsa)
        self.e1rsa = QLineEdit()
        layout.addRow("E", self.e1rsa)
        self.plainr = QLineEdit()
        layout.addRow("Plain", self.plainr)

        buttons = QHBoxLayout()
        self.b1r = QPushButton("Encryption")
        self.b1r.clicked.connect(lambda: self.rsa(
            self.b1r, self.plainr, self.p1rsa, self.q1rsa, self.e1rsa))
        buttons.addWidget(self.b1r)
        layout.addRow(buttons)
# Dec
        radios2 = QHBoxLayout()
        self.with2 = QRadioButton("With spaces")
        self.with2.setChecked(True)
        radios2.addWidget(self.with2)
        self.without2 = QRadioButton("Without space")
        radios2.addWidget(self.without2)
        layout.addRow(QLabel("Select"), radios2)
        self.p2rsa = QLineEdit()
        layout.addRow("P", self.p2rsa)
        self.q2rsa = QLineEdit()
        layout.addRow("q", self.q2rsa)
        self.e2rsa = QLineEdit()
        layout.addRow("E", self.e2rsa)
        self.cypherr = QLineEdit()
        layout.addRow("Cypher", self.cypherr)

        buttons = QHBoxLayout()
        self.b2r = QPushButton("Decryption")
        self.b2r.clicked.connect(lambda: self.rsa(
            self.b2r, self.cypherr, self.p2rsa, self.q2rsa, self.e2rsa))
        buttons.addWidget(self.b2r)
        layout.addRow(buttons)
        self.setTabText(2, "Rsa")
        self.tab3.setLayout(layout)

# Rsa Action
    def rsa(self, b, text, p, q, e):
        if not text.text() or not p.text() or not q.text() or not e.text():
            showdialog("Error", "Text is Required ... ", QMessageBox.Critical)
        else:
            # Enc action
            if b.text() == "Encryption":
                # if with spaces
                #------------------- Rsa Enc Method with spaces ---------------------
                if self.with1.isChecked():
                    showdialog("Rsa Enc Method with spaces ", text.text() +
                               "   " + p.text() + "   " + q.text() + "   " + e.text(), QMessageBox.Warning)
                 # if Without spaces
                #------------------- Rsa Enc Method without spaces ---------------------
                if self.without1.isChecked():
                    showdialog("Rsa Enc Method without spaces ", text.text() +
                               "   " + p.text() + "   " + q.text() + "   " + e.text(), QMessageBox.Warning)
             # Dec action
            else:
                # if with spaces
                #------------------- Rsa Dec Method with spaces ---------------------
                if self.with2.isChecked():
                    showdialog("Rsa Dec Method with spaces ", text.text() +
                               "   " + p.text() + "   " + q.text() + "   " + e.text(), QMessageBox.Warning)
                 # if Without spaces
                #------------------- Rsa DEc Method without spaces ---------------------
                if self.without2.isChecked():
                    showdialog("Rsa Dec Method without spaces ", text.text() +
                               "   " + p.text() + "   " + q.text() + "   " + e.text(), QMessageBox.Warning)

# Affine Action
    def affine(self, b, text, key):
        # Enc action
        if not text.text() or not key.text():
            showdialog("Error", "Text is Required ... ", QMessageBox.Critical)
        else:
            if b.text() == "Encryption":

                 #----------------------- Affine enc method -------------------------
                showdialog("Affine enc method ", text.text() + "   " +
                           key.text(), QMessageBox.Warning)

            # Dec action
            else:
                #------------------------ Affine dec method ---------------------------
                showdialog("Affine dec method", text.text() + "   " +
                           key.text(), QMessageBox.Warning)

# Trans Action
    def trans(self, b, text, key):
        # Enc action
        if not text.text() or not key.text():
            showdialog("Error", "Text is Required ... ", QMessageBox.Critical)
        else:
            if b.text() == "Encryption":

                #----------------------- trans enc method -------------------------
                showdialog("trans enc method ", text.text() + "   " +
                           key.text(), QMessageBox.Warning)

            # Dec action
            else:
                #------------------------ trans dec method ---------------------------
                showdialog("trans dec method", text.text() + "   " +
                           key.text(), QMessageBox.Warning)


# dialog message
def showdialog(text, info, icon):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setText(text)
    msg.setInformativeText(info)
    msg.setWindowTitle("Message")
    #msg.setGeometry(300, 300, 300, 150)
    retval = msg.exec_()
    print "value of pressed message box button:", retval


def main():
    app = QApplication(sys.argv)
    ex = tabdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
