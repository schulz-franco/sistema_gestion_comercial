import os
import sys

sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from interfaces.interfazGestor import Ui_MainWindow
from interfaces.mensajeError import Ui_Dialog
from interfaces.interfazGestorProductos import Ui_gestion_productos
from interfaces.interfazNuevoProducto import Ui_nuevo_producto
from interfaces.interfazMasInformacion import Ui_interfaz_mas_informacion
from interfaces.interfazPedirDatosCliente import Ui_pedir_datos_cliente

from sql.datos import Producto, Venta, Vendedor, Facturas

from control.operaciones_ventas import cerrar_venta
from control.operaciones_productos import cargar_tabla_productos, buscar
from control.cargar_cbo_empleados import cargar_comboVendedor
from control.carrito import agregar_al_carrito, cancelar_venta, ingresar_producto_seleccionado
from control.crear_db import iniciar_db
from control.gestion_productos import cargar_tabla, buscar_gp, eliminar, cargar_stock
from control.nuevo_producto import agregar_producto
from control.nuevo_empleado import agregar_empleado
from control.editar_producto import cargar, editar_producto
from control.gestion_ventas import conf_tabla_ventas, cargar_tabla_gestion_ventas, filtros_venta
from control.gestion_facturas import conf_tabla_facturas, cargar_tabla_facturas, filtros_factura
from control.gestion_empleados import conf_tabla_empleados, cargar_tabla_gestion_empleados, buscar_ge, eliminar_empleado, mostrar_informacion_empleado
from control.validacion import validacion

from generar_factura import exportar_factura
from exportar_excel import generar_excel

import datetime


class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fecha_hoy = datetime.date.today()

        iniciar_db()
        cargar_tabla_productos(self)
        cargar_comboVendedor(self)

        self.ui.actionProductos_3.triggered.connect(self.gestion_productos)
        self.ui.actionVentas_3.triggered.connect(self.gestion_ventas)
        self.ui.actionFacturas_3.triggered.connect(self.gestion_facturas)
        self.ui.actionEmpleados_2.triggered.connect(self.gestion_empleados)

        self.ui.action_exportar_productos.triggered.connect(self.excel_productos)
        self.ui.action_exportar_empleados.triggered.connect(self.excel_empleados)
        self.ui.action_exportar_ventas.triggered.connect(self.excel_ventas)
        self.ui.action_exportar_facturas.triggered.connect(self.excel_facturas)

        self.ui.checkIva.setChecked(1)
        self.ui.btnBuscar1.clicked.connect(self.buscar)
        self.ui.barraBusqueda.setFocus()
        self.ui.barraBusqueda.returnPressed.connect(self.ui.btnBuscar1.click)
        self.ui.selectProducto.returnPressed.connect(self.ui.btn_agregar_carrito.click)
        self.ui.btn_agregar_carrito.clicked.connect(self.agregar_carrito)
        self.ui.input1.returnPressed.connect(self.ui.btn_agregar_carrito.click)
        self.ui.input3.returnPressed.connect(self.ui.btn_agregar_carrito.click)
        self.ui.btnCerrarVenta.clicked.connect(self.cerrar_venta)
        self.ui.btnCancelar.clicked.connect(self.cancelar_venta)
        self.ui.btn_facturar.clicked.connect(self.ventana_datos_cliente)

        self.ui.tablaProductos.cellDoubleClicked.connect(self.ingresar_seleccionado)

        self.importe_total = 0

        self.showMaximized()

        self.gestion_ventas()
        self.gestion_ventas.close()

        self.show()

    def excel_productos(self):
        generar_excel(self, 'productos', Producto)

    def excel_empleados(self):
        generar_excel(self, 'empleados', Vendedor)

    def excel_ventas(self):
        generar_excel(self, 'ventas', Venta)

    def excel_facturas(self):
        generar_excel(self, 'facturas', Facturas)

    def ingresar_seleccionado(self):
        ingresar_producto_seleccionado(self)

    def ventana_editar_producto(self):
        self.editar_producto = QDialog()
        self.editar_producto.ui = Ui_nuevo_producto()
        self.editar_producto.ui.setupUi(self.editar_producto)
        self.editar_producto.setWindowTitle('Editar producto')
        self.editar_producto.ui.btn_nuevo_producto.setText('Actualizar')
        self.editar_producto.ui.btn_nuevo_producto.clicked.connect(self.editar_producto_accion)
        try:
            cargar(self)
            self.editar_producto.show()
        except:
            self.mostrarError('Debe seleccionar un producto de la tabla primero')

    def editar_producto_accion(self):
        editar_producto(self)
        buscar_gp(self.gestion_productos)
        cargar_tabla_productos(self)

    def ventana_nuevo_producto(self):
        self.nuevo_producto = QDialog()
        self.nuevo_producto.ui = Ui_nuevo_producto()
        self.nuevo_producto.ui.setupUi(self.nuevo_producto)
        self.nuevo_producto.ui.input_codigo.setFocus()
        self.nuevo_producto.ui.btn_nuevo_producto.clicked.connect(self.agregar_nuevo_producto)
        self.nuevo_producto.show()

    def agregar_nuevo_producto(self):
        agregar_producto(self)
        buscar_gp(self.gestion_productos)
        cargar_tabla_productos(self)

    def agregar_nuevo_empleado(self):
        agregar_empleado(self)
        buscar_ge(self.gestion_empleados)
        cargar_comboVendedor(self)

    def cargado_stock(self):
        try:
            if cargar_stock(self.gestion_productos) == False:
                self.mostrarError('Casilla en blanco o valores no numericos')
            buscar_gp(self.gestion_productos)
            cargar_tabla_productos(self)
        except:
            self.mostrarError('Producto no seleccionado o valores no numericos')

    def gestion_productos(self):
        self.gestion_productos = QDialog()
        self.gestion_productos.ui = Ui_gestion_productos()
        self.gestion_productos.ui.setupUi(self.gestion_productos)
        cargar_tabla(self.gestion_productos)
        self.gestion_productos.ui.btn_buscar.clicked.connect(self.buscar_gestion_productos)
        self.gestion_productos.ui.btn_nuevo.clicked.connect(self.ventana_nuevo_producto)
        self.gestion_productos.ui.btn_remover.clicked.connect(self.remover_gestion_productos)
        self.gestion_productos.ui.btn_editar.clicked.connect(self.ventana_editar_producto)
        self.gestion_productos.ui.btn_cargar_stock.clicked.connect(self.cargado_stock)
        self.gestion_productos.show()

    def remover_gestion_productos(self):
        try:
            eliminar(self.gestion_productos)
            buscar_gp(self.gestion_productos)
            cargar_tabla_productos(self)
        except:
            self.mostrarError('Primero debe seleccionar un producto')

    def buscar_gestion_productos(self):
        buscar_gp(self.gestion_productos)

    def gestion_ventas(self):
        self.gestion_ventas = QDialog()
        self.gestion_ventas.ui = Ui_gestion_productos()
        self.gestion_ventas.ui.setupUi(self.gestion_ventas)
        self.gestion_ventas.setWindowTitle('Registro de ventas')
        conf_tabla_ventas(self.gestion_ventas)
        cargar_tabla_gestion_ventas(self.gestion_ventas)
        self.gestion_ventas.ui.btn_buscar.clicked.connect(self.buscar_venta)
        self.gestion_ventas.show()

    def gestion_facturas(self):
        self.gestion_facturas = QDialog()
        self.gestion_facturas.ui = Ui_gestion_productos()
        self.gestion_facturas.ui.setupUi(self.gestion_facturas)
        self.gestion_facturas.setWindowTitle('Registro de facturacion')
        conf_tabla_facturas(self.gestion_facturas)
        cargar_tabla_facturas(self.gestion_facturas)
        self.gestion_facturas.ui.btn_buscar.clicked.connect(self.buscar_factura)
        self.gestion_facturas.show()

    def gestion_empleados(self):
        self.gestion_empleados = QDialog()
        self.gestion_empleados.ui = Ui_gestion_productos()
        self.gestion_empleados.ui.setupUi(self.gestion_empleados)
        self.gestion_empleados.setWindowTitle('Gestion de empleados')
        self.gestion_empleados.ui.btn_nuevo.clicked.connect(self.agregar_empleado)
        conf_tabla_empleados(self.gestion_empleados)
        cargar_tabla_gestion_empleados(self.gestion_empleados)
        self.gestion_empleados.ui.btn_buscar.clicked.connect(self.buscar_empleado)
        self.gestion_empleados.ui.btn_remover.clicked.connect(self.remover_gestion_empleados)
        self.gestion_empleados.ui.btn_cargar_stock.clicked.connect(self.informacion_empleado)
        self.gestion_empleados.show()

    def informacion_empleado(self):
        try:
            self.ventana_info_empleado = QDialog()
            self.ventana_info_empleado.ui = Ui_interfaz_mas_informacion()
            self.ventana_info_empleado.ui.setupUi(self.ventana_info_empleado)
            mostrar_informacion_empleado(self)
            self.ventana_info_empleado.show()
        except:
            self.mostrarError('Primero debe seleccionar un empleado')

    def remover_gestion_empleados(self):
        try:
            eliminar_empleado(self.gestion_empleados)
            cargar_comboVendedor(self)
        except:
            self.mostrarError('Primero debe seleccionar un empleado')

    def buscar_empleado(self):
        buscar_ge(self.gestion_empleados)

    def agregar_empleado(self):
        self.nuevo_empleado = QDialog()
        self.nuevo_empleado.ui = Ui_nuevo_producto()
        self.nuevo_empleado.ui.setupUi(self.nuevo_empleado)
        self.nuevo_empleado.setWindowTitle('Cargar nuevo empleado')
        self.nuevo_empleado.ui.input_codigo.setFocus()
        self.nuevo_empleado.ui.btn_nuevo_producto.clicked.connect(self.agregar_nuevo_empleado)
        self.nuevo_empleado.ui.input_desc.setPlaceholderText('Nombre')
        self.nuevo_empleado.ui.input_precio.setPlaceholderText('Apellido')
        self.nuevo_empleado.ui.input_stock.setPlaceholderText('Edad')
        self.nuevo_empleado.show()

    def buscar_venta(self):
        filtros_venta(self.gestion_ventas)

    def buscar_factura(self):
        filtros_factura(self.gestion_facturas)

    def buscar(self):
        buscar(self)

    def agregar_carrito(self):
        if self.ui.selectProducto.text() == '':
            self.mostrarError('Codigo de producto obligatorio')
        elif validacion(self.ui.input1.text()) == False or validacion(self.ui.input3.text()) == False:
            self.mostrarError('Solo se permiten valores numericos')
        else:
            try:
                self.importe_total = self.importe_total + agregar_al_carrito(self)
            except:
                self.mostrarError('Codigo invalido o sin stock')

    def mostrarError(self, mensaje):
        self.msgError = QDialog()
        self.msgError.ui = Ui_Dialog()
        self.msgError.ui.setupUi(self.msgError)
        self.msgError.ui.msgError.setText(mensaje)
        self.msgError.ui.btn_aceptar_error.clicked.connect(self.close)
        self.msgError.show()

    def close(self):
        self.msgError.close()

    def cerrar_venta(self):
        try:
            cerrar_venta(self)
        except:
            pass

    def cancelar_venta(self):
        cancelar_venta(self)

    def ventana_datos_cliente(self):
        filas = self.ui.carrito.rowCount()
        if filas != 0:
            self.ventana_datos_cliente = QDialog()
            self.ventana_datos_cliente.ui = Ui_pedir_datos_cliente()
            self.ventana_datos_cliente.ui.setupUi(self.ventana_datos_cliente)
            self.ventana_datos_cliente.ui.btn_generar.clicked.connect(self.generando_factura)
            self.ventana_datos_cliente.show()
        else:
            self.mostrarError('El carrito esta vacío')

    def generando_factura(self):
        if exportar_factura(self) == 'invalido':
            pass
        else:
            self.ventana_datos_cliente.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Application()
    application.show()
    sys.exit(app.exec_())
