# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerwindow(object):
    def setupUi(self, registerwindow):
        registerwindow.setObjectName("registerwindow")
        registerwindow.resize(598, 527)
        registerwindow.setMinimumSize(QtCore.QSize(0, 0))
        registerwindow.setMaximumSize(QtCore.QSize(10000, 10000))
        registerwindow.setWindowOpacity(1.0)
        registerwindow.setAutoFillBackground(False)
        registerwindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(registerwindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(registerwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resetbtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetbtn.sizePolicy().hasHeightForWidth())
        self.resetbtn.setSizePolicy(sizePolicy)
        self.resetbtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.resetbtn.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"border-width:1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"border-style:outset}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgb(255, 207, 207);\n"
"\n"
"}")
        self.resetbtn.setCheckable(True)
        self.resetbtn.setObjectName("resetbtn")
        self.horizontalLayout.addWidget(self.resetbtn)
        self.sign_text = QtWidgets.QLabel(self.frame_2)
        self.sign_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sign_text.setObjectName("sign_text")
        self.horizontalLayout.addWidget(self.sign_text)
        self.exitbtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbtn.sizePolicy().hasHeightForWidth())
        self.exitbtn.setSizePolicy(sizePolicy)
        self.exitbtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.exitbtn.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"border-width:1px;\n"
"    background-color: rgb(255, 255, 255);\n"
"border-style:outset}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgb(255, 207, 207);\n"
"\n"
"}")
        self.exitbtn.setCheckable(True)
        self.exitbtn.setObjectName("exitbtn")
        self.horizontalLayout.addWidget(self.exitbtn)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(registerwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.age_num = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.age_num.sizePolicy().hasHeightForWidth())
        self.age_num.setSizePolicy(sizePolicy)
        self.age_num.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.age_num.setInputMethodHints(QtCore.Qt.ImhNone)
        self.age_num.setObjectName("age_num")
        self.gridLayout.addWidget(self.age_num, 5, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setStyleSheet("border-width:1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:1px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setStyleSheet("border-width:1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:1px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.name_num = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_num.sizePolicy().hasHeightForWidth())
        self.name_num.setSizePolicy(sizePolicy)
        self.name_num.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.name_num.setText("")
        self.name_num.setObjectName("name_num")
        self.gridLayout.addWidget(self.name_num, 6, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("border-width:1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:1px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.room_num = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.room_num.sizePolicy().hasHeightForWidth())
        self.room_num.setSizePolicy(sizePolicy)
        self.room_num.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.room_num.setObjectName("room_num")
        self.gridLayout.addWidget(self.room_num, 4, 3, 1, 1)
        self.accounttext = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accounttext.sizePolicy().hasHeightForWidth())
        self.accounttext.setSizePolicy(sizePolicy)
        self.accounttext.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.accounttext.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.accounttext.setMaxLength(6)
        self.accounttext.setClearButtonEnabled(True)
        self.accounttext.setObjectName("accounttext")
        self.gridLayout.addWidget(self.accounttext, 0, 3, 1, 1)
        self.confirmpwtext = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmpwtext.sizePolicy().hasHeightForWidth())
        self.confirmpwtext.setSizePolicy(sizePolicy)
        self.confirmpwtext.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.confirmpwtext.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.confirmpwtext.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpwtext.setClearButtonEnabled(True)
        self.confirmpwtext.setObjectName("confirmpwtext")
        self.gridLayout.addWidget(self.confirmpwtext, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setStyleSheet("border-width:1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:1px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setStyleSheet("border-width:1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:1px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.sex_group = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sex_group.sizePolicy().hasHeightForWidth())
        self.sex_group.setSizePolicy(sizePolicy)
        self.sex_group.setTitle("")
        self.sex_group.setObjectName("sex_group")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sex_group)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.male = QtWidgets.QRadioButton(self.sex_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.male.sizePolicy().hasHeightForWidth())
        self.male.setSizePolicy(sizePolicy)
        self.male.setMaximumSize(QtCore.QSize(80, 16777215))
        self.male.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.male.setObjectName("male")
        self.horizontalLayout_3.addWidget(self.male)
        self.female = QtWidgets.QRadioButton(self.sex_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.female.sizePolicy().hasHeightForWidth())
        self.female.setSizePolicy(sizePolicy)
        self.female.setMaximumSize(QtCore.QSize(80, 16777215))
        self.female.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.female.setObjectName("female")
        self.horizontalLayout_3.addWidget(self.female)
        self.gridLayout.addWidget(self.sex_group, 8, 3, 1, 1)
        self.building_num = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.building_num.sizePolicy().hasHeightForWidth())
        self.building_num.setSizePolicy(sizePolicy)
        self.building_num.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.building_num.setMaxVisibleItems(50)
        self.building_num.setMaxCount(2147483642)
        self.building_num.setObjectName("building_num")
        self.gridLayout.addWidget(self.building_num, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setStyleSheet("border-width:1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:1px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_4.setStyleSheet("border-width:1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:1px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.pwtext = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwtext.sizePolicy().hasHeightForWidth())
        self.pwtext.setSizePolicy(sizePolicy)
        self.pwtext.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.pwtext.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.pwtext.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwtext.setClearButtonEnabled(True)
        self.pwtext.setObjectName("pwtext")
        self.gridLayout.addWidget(self.pwtext, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setStyleSheet("border-width:1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:1px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(registerwindow)
        self.frame_4.setStyleSheet("border-width:1px;\n"
"border-color: rgb(159, 159, 159);\n"
"border-style:outset;\n"
"border-radius:5px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setStyleSheet("border-style:solid;\n"
"border-width:0px;\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.email_text = QtWidgets.QLineEdit(self.frame_4)
        self.email_text.setObjectName("email_text")
        self.gridLayout_2.addWidget(self.email_text, 0, 2, 1, 1)
        self.send_email_btn = QtWidgets.QPushButton(self.frame_4)
        self.send_email_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.send_email_btn.setObjectName("send_email_btn")
        self.gridLayout_2.addWidget(self.send_email_btn, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setStyleSheet("border-style:solid;\n"
"border-width:0px;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 2)
        self.my_check_code_text = QtWidgets.QLineEdit(self.frame_4)
        self.my_check_code_text.setObjectName("my_check_code_text")
        self.gridLayout_2.addWidget(self.my_check_code_text, 1, 2, 1, 1)
        self.IC_btn = QtWidgets.QPushButton(self.frame_4)
        self.IC_btn.setObjectName("IC_btn")
        self.gridLayout_2.addWidget(self.IC_btn, 1, 3, 1, 1)
        self.IC_status = QtWidgets.QLabel(self.frame_4)
        self.IC_status.setStyleSheet("border-style:solid;\n"
"border-width:0px;")
        self.IC_status.setAlignment(QtCore.Qt.AlignCenter)
        self.IC_status.setObjectName("IC_status")
        self.gridLayout_2.addWidget(self.IC_status, 2, 1, 1, 3)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(registerwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.manager_key_text = QtWidgets.QLineEdit(self.frame_5)
        self.manager_key_text.setObjectName("manager_key_text")
        self.horizontalLayout_4.addWidget(self.manager_key_text)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(registerwindow)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.registbtn = QtWidgets.QPushButton(self.frame_3)
        self.registbtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.registbtn.sizePolicy().hasHeightForWidth())
        self.registbtn.setSizePolicy(sizePolicy)
        self.registbtn.setMaximumSize(QtCore.QSize(200, 100000))
        self.registbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registbtn.setStyleSheet("QPushButton{\n"
"background-color: rgb(156, 156, 156);\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"border-weight:2px;\n"
"border-color: rgb(255, 255, 127);\n"
"font: 75 14pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(255, 201, 201);\n"
"}\n"
"\n"
"QPushButton:enabled{\n"
"    background-color: rgb(182, 0, 0);\n"
"}\n"
"\n"
"")
        self.registbtn.setObjectName("registbtn")
        self.horizontalLayout_2.addWidget(self.registbtn)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(registerwindow)
        self.registbtn.clicked.connect(registerwindow.registerme)
        self.resetbtn.clicked.connect(registerwindow.resetme)
        self.exitbtn.clicked.connect(registerwindow.exitme)
        self.accounttext.textChanged['QString'].connect(registerwindow.check)
        self.pwtext.textChanged['QString'].connect(registerwindow.check)
        self.confirmpwtext.textChanged['QString'].connect(registerwindow.check)
        self.male.toggled['bool'].connect(registerwindow.boy_or_girl)
        self.female.toggled['bool'].connect(registerwindow.boy_or_girl)
        self.building_num.currentTextChanged['QString'].connect(registerwindow.check)
        self.room_num.textChanged['QString'].connect(registerwindow.check)
        self.age_num.textChanged['QString'].connect(registerwindow.check)
        self.name_num.textChanged['QString'].connect(registerwindow.check)
        self.email_text.textChanged['QString'].connect(registerwindow.check)
        self.send_email_btn.clicked.connect(registerwindow.send_email)
        self.IC_btn.clicked.connect(registerwindow.email_check)
        QtCore.QMetaObject.connectSlotsByName(registerwindow)

    def retranslateUi(self, registerwindow):
        _translate = QtCore.QCoreApplication.translate
        registerwindow.setWindowTitle(_translate("registerwindow", "注册界面"))
        self.resetbtn.setText(_translate("registerwindow", "重置"))
        self.sign_text.setText(_translate("registerwindow", "请填完所有内容"))
        self.exitbtn.setText(_translate("registerwindow", "退出"))
        self.age_num.setPlaceholderText(_translate("registerwindow", "请输入您的年龄"))
        self.label_8.setText(_translate("registerwindow", "性别"))
        self.label_2.setText(_translate("registerwindow", "密码"))
        self.name_num.setPlaceholderText(_translate("registerwindow", "请输入您的姓名"))
        self.label_3.setText(_translate("registerwindow", "单元号"))
        self.room_num.setPlaceholderText(_translate("registerwindow", "请输入您的房号"))
        self.accounttext.setPlaceholderText(_translate("registerwindow", "请输入至多6位账号"))
        self.confirmpwtext.setPlaceholderText(_translate("registerwindow", "请确认密码"))
        self.label_7.setText(_translate("registerwindow", "姓名"))
        self.label_6.setText(_translate("registerwindow", "年龄"))
        self.male.setText(_translate("registerwindow", "男"))
        self.female.setText(_translate("registerwindow", "女"))
        self.building_num.setPlaceholderText(_translate("registerwindow", "请选择您的单元号"))
        self.label_5.setText(_translate("registerwindow", "房号"))
        self.label_4.setText(_translate("registerwindow", "确认密码"))
        self.pwtext.setPlaceholderText(_translate("registerwindow", "密码至少6位，至多10位，请使用英文和数字"))
        self.label.setText(_translate("registerwindow", "账号"))
        self.label_9.setText(_translate("registerwindow", "邮箱"))
        self.send_email_btn.setText(_translate("registerwindow", "发送"))
        self.label_10.setText(_translate("registerwindow", "验证码"))
        self.IC_btn.setText(_translate("registerwindow", "验证"))
        self.IC_status.setText(_translate("registerwindow", "请完成邮箱验证"))
        self.label_11.setText(_translate("registerwindow", "管理员密匙"))
        self.manager_key_text.setPlaceholderText(_translate("registerwindow", "普通用户无需输入"))
        self.registbtn.setText(_translate("registerwindow", "注  册"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerwindow = QtWidgets.QWidget()
    ui = Ui_registerwindow()
    ui.setupUi(registerwindow)
    registerwindow.show()
    sys.exit(app.exec_())
