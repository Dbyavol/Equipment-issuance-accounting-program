# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Newuser(object):
    def setupUi(self, Newuser):
        Newuser.setObjectName("Newuser")
        Newuser.resize(350, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Newuser.sizePolicy().hasHeightForWidth())
        Newuser.setSizePolicy(sizePolicy)
        Newuser.setMinimumSize(QtCore.QSize(350, 500))
        Newuser.setMaximumSize(QtCore.QSize(400, 500))
        font = QtGui.QFont()
        font.setPointSize(12)
        Newuser.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Newuser)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_7 = QtWidgets.QSplitter(Newuser)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.access_label = QtWidgets.QLabel(self.splitter_7)
        self.access_label.setObjectName("access_label")
        self.access_box = QtWidgets.QComboBox(self.splitter_7)
        self.access_box.setObjectName("access_box")
        self.access_box.addItem("")
        self.access_box.addItem("")
        self.gridLayout.addWidget(self.splitter_7, 6, 0, 1, 1)
        self.splitter_8 = QtWidgets.QSplitter(Newuser)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.splitter_8)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.splitter_8, 7, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(Newuser)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.patr_label = QtWidgets.QLabel(self.splitter_3)
        self.patr_label.setObjectName("patr_label")
        self.patr_line = QtWidgets.QLineEdit(self.splitter_3)
        self.patr_line.setClearButtonEnabled(True)
        self.patr_line.setObjectName("patr_line")
        self.gridLayout.addWidget(self.splitter_3, 2, 0, 1, 1)
        self.splitter_6 = QtWidgets.QSplitter(Newuser)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.phone_label = QtWidgets.QLabel(self.splitter_6)
        self.phone_label.setObjectName("phone_label")
        self.phone_line = QtWidgets.QLineEdit(self.splitter_6)
        self.phone_line.setClearButtonEnabled(True)
        self.phone_line.setObjectName("phone_line")
        self.gridLayout.addWidget(self.splitter_6, 5, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(Newuser)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.name_label = QtWidgets.QLabel(self.splitter_2)
        self.name_label.setObjectName("name_label")
        self.name_line = QtWidgets.QLineEdit(self.splitter_2)
        self.name_line.setClearButtonEnabled(True)
        self.name_line.setObjectName("name_line")
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(Newuser)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.group_label = QtWidgets.QLabel(self.splitter_4)
        self.group_label.setObjectName("group_label")
        self.group_line = QtWidgets.QLineEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_line.setFont(font)
        self.group_line.setClearButtonEnabled(True)
        self.group_line.setObjectName("group_line")
        self.gridLayout.addWidget(self.splitter_4, 3, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Newuser)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.surname_label = QtWidgets.QLabel(self.splitter)
        self.surname_label.setObjectName("surname_label")
        self.surname_line = QtWidgets.QLineEdit(self.splitter)
        self.surname_line.setClearButtonEnabled(True)
        self.surname_line.setObjectName("surname_line")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_5 = QtWidgets.QSplitter(Newuser)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.email_label = QtWidgets.QLabel(self.splitter_5)
        self.email_label.setObjectName("email_label")
        self.email_line = QtWidgets.QLineEdit(self.splitter_5)
        self.email_line.setClearButtonEnabled(True)
        self.email_line.setObjectName("email_line")
        self.gridLayout.addWidget(self.splitter_5, 4, 0, 1, 1)

        self.retranslateUi(Newuser)
        QtCore.QMetaObject.connectSlotsByName(Newuser)

    def retranslateUi(self, Newuser):
        _translate = QtCore.QCoreApplication.translate
        Newuser.setWindowTitle(_translate("Newuser", "Добавить нового пользователя"))
        self.access_label.setText(_translate("Newuser", "Уровень доступа"))
        self.access_box.setItemText(0, _translate("Newuser", "admin"))
        self.access_box.setItemText(1, _translate("Newuser", "user"))
        self.patr_label.setText(_translate("Newuser", "Отчество"))
        self.phone_label.setText(_translate("Newuser", "Телефон"))
        self.name_label.setText(_translate("Newuser", "Имя"))
        self.group_label.setText(_translate("Newuser", "Группа"))
        self.surname_label.setText(_translate("Newuser", "Фамилия"))
        self.email_label.setText(_translate("Newuser", "Почта"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Newuser = QtWidgets.QDialog()
    ui = Ui_Newuser()
    ui.setupUi(Newuser)
    Newuser.show()
    sys.exit(app.exec_())
