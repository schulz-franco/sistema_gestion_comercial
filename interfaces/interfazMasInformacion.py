# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazMasInformacion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_interfaz_mas_informacion(object):
    def setupUi(self, interfaz_mas_informacion):
        interfaz_mas_informacion.setObjectName("interfaz_mas_informacion")
        interfaz_mas_informacion.resize(146, 116)
        self.verticalLayout = QtWidgets.QVBoxLayout(interfaz_mas_informacion)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(interfaz_mas_informacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 20))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.info_codigo = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_codigo.sizePolicy().hasHeightForWidth())
        self.info_codigo.setSizePolicy(sizePolicy)
        self.info_codigo.setObjectName("info_codigo")
        self.horizontalLayout.addWidget(self.info_codigo)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(interfaz_mas_informacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(60, 20))
        self.label_7.setMaximumSize(QtCore.QSize(60, 20))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.info_nombre = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_nombre.sizePolicy().hasHeightForWidth())
        self.info_nombre.setSizePolicy(sizePolicy)
        self.info_nombre.setMinimumSize(QtCore.QSize(0, 20))
        self.info_nombre.setMaximumSize(QtCore.QSize(16777215, 20))
        self.info_nombre.setObjectName("info_nombre")
        self.horizontalLayout_4.addWidget(self.info_nombre)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(interfaz_mas_informacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(60, 20))
        self.label_5.setMaximumSize(QtCore.QSize(60, 20))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.info_apellido = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_apellido.sizePolicy().hasHeightForWidth())
        self.info_apellido.setSizePolicy(sizePolicy)
        self.info_apellido.setMinimumSize(QtCore.QSize(0, 20))
        self.info_apellido.setMaximumSize(QtCore.QSize(16777215, 20))
        self.info_apellido.setObjectName("info_apellido")
        self.horizontalLayout_3.addWidget(self.info_apellido)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(interfaz_mas_informacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(60, 20))
        self.label_3.setMaximumSize(QtCore.QSize(60, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.info_edad = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_edad.sizePolicy().hasHeightForWidth())
        self.info_edad.setSizePolicy(sizePolicy)
        self.info_edad.setMinimumSize(QtCore.QSize(0, 20))
        self.info_edad.setMaximumSize(QtCore.QSize(16777215, 20))
        self.info_edad.setObjectName("info_edad")
        self.horizontalLayout_2.addWidget(self.info_edad)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(interfaz_mas_informacion)
        QtCore.QMetaObject.connectSlotsByName(interfaz_mas_informacion)

    def retranslateUi(self, interfaz_mas_informacion):
        _translate = QtCore.QCoreApplication.translate
        interfaz_mas_informacion.setWindowTitle(_translate("interfaz_mas_informacion", "Empleado"))
        self.label.setText(_translate("interfaz_mas_informacion", "Codigo:"))
        self.info_codigo.setText(_translate("interfaz_mas_informacion", "info_codigo"))
        self.label_7.setText(_translate("interfaz_mas_informacion", "Nombre:"))
        self.info_nombre.setText(_translate("interfaz_mas_informacion", "info_nombre"))
        self.label_5.setText(_translate("interfaz_mas_informacion", "Apellido:"))
        self.info_apellido.setText(_translate("interfaz_mas_informacion", "info_apellido"))
        self.label_3.setText(_translate("interfaz_mas_informacion", "Edad:"))
        self.info_edad.setText(_translate("interfaz_mas_informacion", "info_edad"))