# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_client_img.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_show_client_img_win(object):
    def setupUi(self, show_client_img_win):
        show_client_img_win.setObjectName("show_client_img_win")
        show_client_img_win.resize(452, 361)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(show_client_img_win.sizePolicy().hasHeightForWidth())
        show_client_img_win.setSizePolicy(sizePolicy)
        show_client_img_win.setStyleSheet("#show_client_img_win{\n"
"border-width:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(show_client_img_win)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pic_shower = QtWidgets.QLabel(show_client_img_win)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pic_shower.sizePolicy().hasHeightForWidth())
        self.pic_shower.setSizePolicy(sizePolicy)
        self.pic_shower.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pic_shower.setScaledContents(True)
        self.pic_shower.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_shower.setObjectName("pic_shower")
        self.verticalLayout.addWidget(self.pic_shower)
        self.frame = QtWidgets.QFrame(show_client_img_win)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("border-width:2px;\n"
"border-style:solid;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(104, 148, 0);\n"
"border-radius:5px;\n"
"font: 9pt \"微软雅黑\";\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(show_client_img_win)
        self.pushButton_3.clicked.connect(show_client_img_win.return_to_enter_inter)
        self.pushButton.clicked.connect(show_client_img_win.agree_to_enter)
        self.pushButton_2.clicked.connect(show_client_img_win.disagree_to_enter)
        QtCore.QMetaObject.connectSlotsByName(show_client_img_win)

    def retranslateUi(self, show_client_img_win):
        _translate = QtCore.QCoreApplication.translate
        show_client_img_win.setWindowTitle(_translate("show_client_img_win", "Form"))
        self.pic_shower.setText(_translate("show_client_img_win", "TextLabel"))
        self.pushButton.setText(_translate("show_client_img_win", "同意进入"))
        self.pushButton_2.setText(_translate("show_client_img_win", "拒绝进入"))
        self.pushButton_3.setText(_translate("show_client_img_win", "返回"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show_client_img_win = QtWidgets.QWidget()
    ui = Ui_show_client_img_win()
    ui.setupUi(show_client_img_win)
    show_client_img_win.show()
    sys.exit(app.exec_())