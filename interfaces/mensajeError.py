# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mensajeError.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 77)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame#frame {\n"
"border: none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.msgError = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgError.sizePolicy().hasHeightForWidth())
        self.msgError.setSizePolicy(sizePolicy)
        self.msgError.setStyleSheet("")
        self.msgError.setText("")
        self.msgError.setAlignment(QtCore.Qt.AlignCenter)
        self.msgError.setObjectName("msgError")
        self.horizontalLayout.addWidget(self.msgError)
        self.verticalLayout.addWidget(self.frame)
        self.btn_aceptar_error = QtWidgets.QPushButton(Dialog)
        self.btn_aceptar_error.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_aceptar_error.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_aceptar_error.setObjectName("btn_aceptar_error")
        self.verticalLayout.addWidget(self.btn_aceptar_error)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Advertencia"))
        self.btn_aceptar_error.setText(_translate("Dialog", "Aceptar"))
