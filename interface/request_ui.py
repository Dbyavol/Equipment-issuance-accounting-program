# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Request.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewRequest(object):
    def setupUi(self, NewRequest):
        NewRequest.setObjectName("NewRequest")
        NewRequest.resize(400, 450)
        NewRequest.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(12)
        NewRequest.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(NewRequest)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(NewRequest)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.name_line = QtWidgets.QLineEdit(NewRequest)
        self.name_line.setClearButtonEnabled(True)
        self.name_line.setObjectName("name_line")
        self.gridLayout.addWidget(self.name_line, 0, 1, 1, 1)
        self.last_name_label = QtWidgets.QLabel(NewRequest)
        self.last_name_label.setObjectName("last_name_label")
        self.gridLayout.addWidget(self.last_name_label, 1, 0, 1, 1)
        self.last_name_line = QtWidgets.QLineEdit(NewRequest)
        self.last_name_line.setClearButtonEnabled(True)
        self.last_name_line.setObjectName("last_name_line")
        self.gridLayout.addWidget(self.last_name_line, 1, 1, 1, 1)
        self.email_label = QtWidgets.QLabel(NewRequest)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 1)
        self.email_line = QtWidgets.QLineEdit(NewRequest)
        self.email_line.setClearButtonEnabled(True)
        self.email_line.setObjectName("email_line")
        self.gridLayout.addWidget(self.email_line, 2, 1, 1, 1)
        self.phone_label = QtWidgets.QLabel(NewRequest)
        self.phone_label.setObjectName("phone_label")
        self.gridLayout.addWidget(self.phone_label, 3, 0, 1, 1)
        self.phone_line = QtWidgets.QLineEdit(NewRequest)
        self.phone_line.setClearButtonEnabled(True)
        self.phone_line.setObjectName("phone_line")
        self.gridLayout.addWidget(self.phone_line, 3, 1, 1, 1)
        self.cab_label = QtWidgets.QLabel(NewRequest)
        self.cab_label.setObjectName("cab_label")
        self.gridLayout.addWidget(self.cab_label, 4, 0, 1, 1)
        self.cab_box = QtWidgets.QComboBox(NewRequest)
        self.cab_box.setEditable(False)
        self.cab_box.setObjectName("cab_box")
        self.gridLayout.addWidget(self.cab_box, 4, 1, 1, 1)
        self.hardware_label = QtWidgets.QLabel(NewRequest)
        self.hardware_label.setObjectName("hardware_label")
        self.gridLayout.addWidget(self.hardware_label, 5, 0, 1, 1)
        self.hardware_box = QtWidgets.QComboBox(NewRequest)
        self.hardware_box.setEditable(False)
        self.hardware_box.setObjectName("hardware_box")
        self.gridLayout.addWidget(self.hardware_box, 5, 1, 1, 1)
        self.count_label = QtWidgets.QLabel(NewRequest)
        self.count_label.setObjectName("count_label")
        self.gridLayout.addWidget(self.count_label, 6, 0, 1, 1)
        self.count_box = QtWidgets.QSpinBox(NewRequest)
        self.count_box.setWrapping(False)
        self.count_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.count_box.setProperty("value", 1)
        self.count_box.setObjectName("count_box")
        self.gridLayout.addWidget(self.count_box, 6, 1, 1, 1)
        self.date1_label = QtWidgets.QLabel(NewRequest)
        self.date1_label.setObjectName("date1_label")
        self.gridLayout.addWidget(self.date1_label, 7, 0, 1, 1)
        self.date1_edit = QtWidgets.QDateEdit(NewRequest)
        self.date1_edit.setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.date1_edit.setMinimumDate(QtCore.QDate(2023, 6, 1))
        self.date1_edit.setCalendarPopup(True)
        self.date1_edit.setObjectName("date1_edit")
        self.gridLayout.addWidget(self.date1_edit, 7, 1, 1, 1)
        self.date2_label = QtWidgets.QLabel(NewRequest)
        self.date2_label.setObjectName("date2_label")
        self.gridLayout.addWidget(self.date2_label, 8, 0, 1, 1)
        self.date2_edit = QtWidgets.QDateEdit(NewRequest)
        self.date2_edit.setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.date2_edit.setMinimumDate(QtCore.QDate(2023, 6, 1))
        self.date2_edit.setCalendarPopup(True)
        self.date2_edit.setObjectName("date2_edit")
        self.gridLayout.addWidget(self.date2_edit, 8, 1, 1, 1)
        self.comment_label = QtWidgets.QLabel(NewRequest)
        self.comment_label.setObjectName("comment_label")
        self.gridLayout.addWidget(self.comment_label, 9, 0, 1, 1)
        self.comment_line = QtWidgets.QLineEdit(NewRequest)
        self.comment_line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comment_line.setDragEnabled(False)
        self.comment_line.setClearButtonEnabled(True)
        self.comment_line.setObjectName("comment_line")
        self.gridLayout.addWidget(self.comment_line, 9, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewRequest)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 1, 1, 1)

        self.retranslateUi(NewRequest)
        self.buttonBox.accepted.connect(NewRequest.accept) # type: ignore
        self.buttonBox.rejected.connect(NewRequest.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NewRequest)

    def retranslateUi(self, NewRequest):
        _translate = QtCore.QCoreApplication.translate
        NewRequest.setWindowTitle(_translate("NewRequest", "Выдача оборудования"))
        self.name_label.setText(_translate("NewRequest", "Имя"))
        self.last_name_label.setText(_translate("NewRequest", "Фамилия"))
        self.email_label.setText(_translate("NewRequest", "Почта"))
        self.phone_label.setText(_translate("NewRequest", "Телефон"))
        self.cab_label.setText(_translate("NewRequest", "Аудитория"))
        self.hardware_label.setText(_translate("NewRequest", "Плата"))
        self.count_label.setText(_translate("NewRequest", "Количество"))
        self.date1_label.setText(_translate("NewRequest", "Дата выдачи"))
        self.date2_label.setText(_translate("NewRequest", "Дата возврата"))
        self.comment_label.setText(_translate("NewRequest", "Комментарий"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewRequest = QtWidgets.QDialog()
    ui = Ui_NewRequest()
    ui.setupUi(NewRequest)
    NewRequest.show()
    sys.exit(app.exec_())
