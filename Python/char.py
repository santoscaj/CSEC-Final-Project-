# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from myExcel import myExcel
xlsheet = myExcel()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_characterWindow(object):
    def setupUi(self, characterWindow):
        characterWindow.setObjectName(_fromUtf8("characterWindow"))
        characterWindow.resize(784, 471)
        self.frame = QtGui.QFrame(characterWindow)
        self.frame.setGeometry(QtCore.QRect(20, 70, 731, 351))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.btn_1 = QtGui.QPushButton(self.frame)
        self.btn_1.setGeometry(QtCore.QRect(0, 70, 81, 81))
        self.btn_1.setText(_fromUtf8(""))
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.btn_1.setToolTip(xlsheet.getRandomName(1))
        self.btn_2 = QtGui.QPushButton(self.frame)
        self.btn_2.setGeometry(QtCore.QRect(80, 70, 81, 81))
        self.btn_2.setText(_fromUtf8(""))
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.btn_3 = QtGui.QPushButton(self.frame)
        self.btn_3.setGeometry(QtCore.QRect(160, 70, 81, 81))
        self.btn_3.setText(_fromUtf8(""))
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.btn_4 = QtGui.QPushButton(self.frame)
        self.btn_4.setGeometry(QtCore.QRect(240, 70, 81, 81))
        self.btn_4.setText(_fromUtf8(""))
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.btn_5 = QtGui.QPushButton(self.frame)
        self.btn_5.setGeometry(QtCore.QRect(320, 70, 81, 81))
        self.btn_5.setText(_fromUtf8(""))
        self.btn_5.setObjectName(_fromUtf8("btn_5"))
        self.btn_6 = QtGui.QPushButton(self.frame)
        self.btn_6.setGeometry(QtCore.QRect(400, 70, 81, 81))
        self.btn_6.setText(_fromUtf8(""))
        self.btn_6.setObjectName(_fromUtf8("btn_6"))
        self.btn_7 = QtGui.QPushButton(self.frame)
        self.btn_7.setGeometry(QtCore.QRect(480, 70, 81, 81))
        self.btn_7.setText(_fromUtf8(""))
        self.btn_7.setObjectName(_fromUtf8("btn_7"))
        self.btn_8 = QtGui.QPushButton(self.frame)
        self.btn_8.setGeometry(QtCore.QRect(560, 70, 81, 81))
        self.btn_8.setText(_fromUtf8(""))
        self.btn_8.setObjectName(_fromUtf8("btn_8"))
        self.btn_9 = QtGui.QPushButton(self.frame)
        self.btn_9.setGeometry(QtCore.QRect(640, 70, 81, 81))
        self.btn_9.setText(_fromUtf8(""))
        self.btn_9.setObjectName(_fromUtf8("btn_9"))
        self.btn_10 = QtGui.QPushButton(self.frame)
        self.btn_10.setGeometry(QtCore.QRect(320, 150, 81, 81))
        self.btn_10.setText(_fromUtf8(""))
        self.btn_10.setObjectName(_fromUtf8("btn_10"))
        self.btn_11 = QtGui.QPushButton(self.frame)
        self.btn_11.setGeometry(QtCore.QRect(640, 150, 81, 81))
        self.btn_11.setText(_fromUtf8(""))
        self.btn_11.setObjectName(_fromUtf8("btn_11"))
        self.btn_12 = QtGui.QPushButton(self.frame)
        self.btn_12.setGeometry(QtCore.QRect(560, 150, 81, 81))
        self.btn_12.setText(_fromUtf8(""))
        self.btn_12.setObjectName(_fromUtf8("btn_12"))
        self.btn_13 = QtGui.QPushButton(self.frame)
        self.btn_13.setGeometry(QtCore.QRect(240, 150, 81, 81))
        self.btn_13.setText(_fromUtf8(""))
        self.btn_13.setObjectName(_fromUtf8("btn_13"))
        self.btn_14 = QtGui.QPushButton(self.frame)
        self.btn_14.setGeometry(QtCore.QRect(160, 150, 81, 81))
        self.btn_14.setText(_fromUtf8(""))
        self.btn_14.setObjectName(_fromUtf8("btn_14"))
        self.btn_15 = QtGui.QPushButton(self.frame)
        self.btn_15.setGeometry(QtCore.QRect(0, 150, 81, 81))
        self.btn_15.setText(_fromUtf8(""))
        self.btn_15.setObjectName(_fromUtf8("btn_15"))
        self.btn_16 = QtGui.QPushButton(self.frame)
        self.btn_16.setGeometry(QtCore.QRect(80, 150, 81, 81))
        self.btn_16.setText(_fromUtf8(""))
        self.btn_16.setObjectName(_fromUtf8("btn_16"))
        self.btn_17 = QtGui.QPushButton(self.frame)
        self.btn_17.setGeometry(QtCore.QRect(480, 150, 81, 81))
        self.btn_17.setText(_fromUtf8(""))
        self.btn_17.setObjectName(_fromUtf8("btn_17"))
        self.btn_18 = QtGui.QPushButton(self.frame)
        self.btn_18.setGeometry(QtCore.QRect(400, 150, 81, 81))
        self.btn_18.setText(_fromUtf8(""))
        self.btn_18.setObjectName(_fromUtf8("btn_18"))
        self.btn_19 = QtGui.QPushButton(self.frame)
        self.btn_19.setGeometry(QtCore.QRect(320, 230, 81, 81))
        self.btn_19.setText(_fromUtf8(""))
        self.btn_19.setObjectName(_fromUtf8("btn_19"))
        self.btn_20 = QtGui.QPushButton(self.frame)
        self.btn_20.setGeometry(QtCore.QRect(640, 230, 81, 81))
        self.btn_20.setText(_fromUtf8(""))
        self.btn_20.setObjectName(_fromUtf8("btn_20"))
        self.btn_21 = QtGui.QPushButton(self.frame)
        self.btn_21.setGeometry(QtCore.QRect(560, 230, 81, 81))
        self.btn_21.setText(_fromUtf8(""))
        self.btn_21.setObjectName(_fromUtf8("btn_21"))
        self.btn_22 = QtGui.QPushButton(self.frame)
        self.btn_22.setGeometry(QtCore.QRect(240, 230, 81, 81))
        self.btn_22.setText(_fromUtf8(""))
        self.btn_22.setObjectName(_fromUtf8("btn_22"))
        self.btn_23 = QtGui.QPushButton(self.frame)
        self.btn_23.setGeometry(QtCore.QRect(160, 230, 81, 81))
        self.btn_23.setText(_fromUtf8(""))
        self.btn_23.setObjectName(_fromUtf8("btn_23"))
        self.btn_24 = QtGui.QPushButton(self.frame)
        self.btn_24.setGeometry(QtCore.QRect(0, 230, 81, 81))
        self.btn_24.setText(_fromUtf8(""))
        self.btn_24.setObjectName(_fromUtf8("btn_24"))
        self.btn_25 = QtGui.QPushButton(self.frame)
        self.btn_25.setGeometry(QtCore.QRect(80, 230, 81, 81))
        self.btn_25.setText(_fromUtf8(""))
        self.btn_25.setObjectName(_fromUtf8("btn_25"))
        self.btn_26 = QtGui.QPushButton(self.frame)
        self.btn_26.setGeometry(QtCore.QRect(480, 230, 81, 81))
        self.btn_26.setText(_fromUtf8(""))
        self.btn_26.setObjectName(_fromUtf8("btn_26"))
        self.btn_27 = QtGui.QPushButton(self.frame)
        self.btn_27.setGeometry(QtCore.QRect(400, 230, 81, 81))
        self.btn_27.setText(_fromUtf8(""))
        self.btn_27.setObjectName(_fromUtf8("btn_27"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 20, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(characterWindow)
        QtCore.QMetaObject.connectSlotsByName(characterWindow)

    def retranslateUi(self, characterWindow):
        characterWindow.setWindowTitle(_translate("characterWindow", "Form", None))
        self.label.setText(_translate("characterWindow", "Select your character!  Someone easy to remember for you", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    characterWindow = QtGui.QWidget()
    ui = Ui_characterWindow()
    ui.setupUi(characterWindow)
    characterWindow.show()
    sys.exit(app.exec_())

