# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazNuevoProducto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_nuevo_producto(object):
    def setupUi(self, nuevo_producto):
        nuevo_producto.setObjectName("nuevo_producto")
        nuevo_producto.resize(400, 202)
        self.verticalLayout = QtWidgets.QVBoxLayout(nuevo_producto)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(nuevo_producto)
        self.frame.setStyleSheet("QFrame#frame{\n"
"border: none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_codigo = QtWidgets.QLineEdit(self.frame)
        self.input_codigo.setMinimumSize(QtCore.QSize(0, 30))
        self.input_codigo.setObjectName("input_codigo")
        self.verticalLayout_2.addWidget(self.input_codigo)
        self.input_desc = QtWidgets.QLineEdit(self.frame)
        self.input_desc.setMinimumSize(QtCore.QSize(0, 30))
        self.input_desc.setObjectName("input_desc")
        self.verticalLayout_2.addWidget(self.input_desc)
        self.input_precio = QtWidgets.QLineEdit(self.frame)
        self.input_precio.setMinimumSize(QtCore.QSize(0, 30))
        self.input_precio.setObjectName("input_precio")
        self.verticalLayout_2.addWidget(self.input_precio)
        self.input_stock = QtWidgets.QLineEdit(self.frame)
        self.input_stock.setMinimumSize(QtCore.QSize(0, 30))
        self.input_stock.setObjectName("input_stock")
        self.verticalLayout_2.addWidget(self.input_stock)
        self.verticalLayout.addWidget(self.frame)
        self.btn_nuevo_producto = QtWidgets.QPushButton(nuevo_producto)
        self.btn_nuevo_producto.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_nuevo_producto.setFont(font)
        self.btn_nuevo_producto.setObjectName("btn_nuevo_producto")
        self.verticalLayout.addWidget(self.btn_nuevo_producto)

        self.retranslateUi(nuevo_producto)
        QtCore.QMetaObject.connectSlotsByName(nuevo_producto)

    def retranslateUi(self, nuevo_producto):
        _translate = QtCore.QCoreApplication.translate
        nuevo_producto.setWindowTitle(_translate("nuevo_producto", "Nuevo producto"))
        self.input_codigo.setPlaceholderText(_translate("nuevo_producto", "Codigo"))
        self.input_desc.setPlaceholderText(_translate("nuevo_producto", "Descripcion"))
        self.input_precio.setPlaceholderText(_translate("nuevo_producto", "Precio unitario"))
        self.input_stock.setPlaceholderText(_translate("nuevo_producto", "Stock"))
        self.btn_nuevo_producto.setText(_translate("nuevo_producto", "Agregar"))