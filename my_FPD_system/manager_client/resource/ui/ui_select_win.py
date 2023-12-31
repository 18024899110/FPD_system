# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_select_win(object):
    def setupUi(self, select_win):
        select_win.setObjectName("select_win")
        select_win.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(select_win)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(select_win)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame = QtWidgets.QFrame(select_win)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.name_text = QtWidgets.QLineEdit(self.frame)
        self.name_text.setObjectName("name_text")
        self.verticalLayout.addWidget(self.name_text)
        self.name_btn = QtWidgets.QPushButton(self.frame)
        self.name_btn.setObjectName("name_btn")
        self.verticalLayout.addWidget(self.name_btn)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(select_win)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.house_num = QtWidgets.QComboBox(self.frame_2)
        self.house_num.setObjectName("house_num")
        self.house_num.addItem("")
        self.house_num.addItem("")
        self.house_num.addItem("")
        self.house_num.addItem("")
        self.house_num.addItem("")
        self.house_num.addItem("")
        self.house_num.addItem("")
        self.house_num.addItem("")
        self.verticalLayout_3.addWidget(self.house_num)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.room_num = QtWidgets.QLineEdit(self.frame_2)
        self.room_num.setObjectName("room_num")
        self.verticalLayout_3.addWidget(self.room_num)
        self.house_room_btn = QtWidgets.QPushButton(self.frame_2)
        self.house_room_btn.setObjectName("house_room_btn")
        self.verticalLayout_3.addWidget(self.house_room_btn)
        self.verticalLayout_2.addWidget(self.frame_2)

        self.retranslateUi(select_win)
        self.name_text.textChanged['QString'].connect(select_win.name_check)
        self.room_num.textChanged['QString'].connect(select_win.house_room_check)
        self.name_btn.clicked.connect(select_win.name_select)
        self.house_room_btn.clicked.connect(select_win.house_room_select)
        QtCore.QMetaObject.connectSlotsByName(select_win)

    def retranslateUi(self, select_win):
        _translate = QtCore.QCoreApplication.translate
        select_win.setWindowTitle(_translate("select_win", "Form"))
        self.label_2.setText(_translate("select_win", "请输入姓名或者住址进行查询"))
        self.label.setText(_translate("select_win", "姓名"))
        self.name_btn.setText(_translate("select_win", "查询"))
        self.label_3.setText(_translate("select_win", "单元号"))
        self.house_num.setItemText(0, _translate("select_win", "A1"))
        self.house_num.setItemText(1, _translate("select_win", "A2"))
        self.house_num.setItemText(2, _translate("select_win", "B1"))
        self.house_num.setItemText(3, _translate("select_win", "B2"))
        self.house_num.setItemText(4, _translate("select_win", "C1"))
        self.house_num.setItemText(5, _translate("select_win", "C2"))
        self.house_num.setItemText(6, _translate("select_win", "D1"))
        self.house_num.setItemText(7, _translate("select_win", "D2"))
        self.label_4.setText(_translate("select_win", "房号"))
        self.house_room_btn.setText(_translate("select_win", "查询"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_win = QtWidgets.QWidget()
    ui = Ui_select_win()
    ui.setupUi(select_win)
    select_win.show()
    sys.exit(app.exec_())
