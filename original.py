from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

import qrcode
import datetime
tiempo =datetime.datetime.now()
#print(tiempo)

hora = datetime.datetime.now().hour
minu = datetime.datetime.now().minute
seg = datetime.datetime.now().second


print ("        AZAMI S.A.S    "   )
print ("       NIT 32435465    "   )
print ("      TEL: 3142769220  "   )
print ("-" * 30)
print ("     TERMINAL NEIVA HUILA  "  )
print (" CAJERO: Bermeo Duero Valentina  ")

print("Fecha: {}/{}/{}".format(tiempo.day,tiempo.month,tiempo.year))
print("Hora: {}:{}:{}".format(tiempo.hour,tiempo.minute,tiempo.second))

class todo:

    def __init__(self):
        self.nombrecli = " "
        self.cedulacli = " "
        self.cantidad = 0
        self.precio = 0
        self.nombre = " "
        self.costo_total = 0
        self.iva_total = 0
        self.lista_productos = []
        self.monto = 0



    def datos(self):
        print('--------------------------')
        print('          CLIENTE   ')
        print('---------------------------')
        self.nombreplea = input( 'Digite el nombre del empleado: ')
        self.nombrecli = input( 'Digite el nombre del cliente: ')
        self.cedulacli = input( 'Digite la cedula del cliente: ')

    def calcular_costo_total(self):
        self.costo_total = self.cantidad * self.precio
    def calcular_iva_total(self):
        self.iva_total = self.costo_total * 0.19

    def so_datos(self):
        print('-------------------------')
        print( '         PRODUCTO  ')
        print('--------------------------')
        self.nombre = input( 'Digite el nombre del producto: ')
        self.precio = float(input('Digite el precio del producto:$ '))
        self.cantidad = int(input( 'Digite la cantidad del producto: '))

    def re_productos(self):
        while True:
            print('Facturar un producto?')
            print('1 = SI')
            print('2 = NO')
            va = int(input('Digite la opcion deseada: '))
            if va == 2:
                print("Inicia de nuevo")
                break
            else:
                Todo = todo()
                Todo.so_datos()
                Todo.calcular_costo_total()
                self.lista_productos.append(Todo)
        
        while True:
            print (" - " * 35)
            print('Pagar con tarjeta')
            print('1 - SI')
            print('2 - NO')
            va = int(input( 'Digite la opcion deseada: '))
            if va == 1:
               print("No es permitido, estamos trabajando en ello")
            else:
                print("okay")
                break

    def procesar_fac(self):

        for todo in self.lista_productos:
            self.monto += todo.costo_total

        print ("=" * 35)
        print (f' NOMBRE : {self.nombrecli}')
        print (f' CEDULA : {self.cedulacli}')   
        print(f'SUBTOTAL : {self.monto:.0f}')
        print('-' * 35)
        print(f'CANTIDAD PRODUCTO FACTURADOS: {len(self.lista_productos)}')
        print( 'LISTADO PRODUCTOS: ')
        print('-' * 30)
        for todo in self.lista_productos:
            print(f'NOMBRE: {todo.nombre} - PRECIO: {todo.precio:.0f} - CANTIDAD: {todo.cantidad} - TOTAL: {todo.costo_total:.0f} ')
        print(f'IVA FINAL : {self.monto * 0.19:.0f}')
        print(f'TOTAL : {self.monto + (self.monto *  0.19):.0f} ')
        print( '-' * 30)

    def Qr(self):
        input = (f'Nombre del empleado: ',self.nombreplea,'Nombre del cliente: ',self.nombrecli,'Total: ',self.monto)
        qr = qrcode.QRCode(version=3,border=5)

        qr.add_data(input)
        qr.make(fit=True)

        img = qr.make_image(fill='black',back_color='white')
        img.save('nombre.png')


        w, h = letter
        c = canvas.Canvas("factura.pdf", pagesize=letter)
        c.setFont("Helvetica",12)
        c.drawString(190,h-10," AZAMI S.A.S")
        c.drawString(187,h-25,"  NIT: 3234567-5")
        c.drawString(147,h-40,"RESPONSABLE DE IVA. EEU 1081 ")
        c.drawString(167,h-55,"  Agente Retenedor de ICA")
        c.drawString(180,h-70,"  TEL:  3142769220")
        c.drawString(180,h-85,"Servicios_Exito.com.co")
        c.drawString(157,h-100,"  TERMINAL EXITO HUILA ")
        c.drawString(158,h-115,"      DG 23 65 18 LC 123")
        c.drawString(120,h-135,"Aut.  DIAN 4567876542 FEC: 03/24/2022")
        c.drawString(120,h-150,"DESDE JK-22663      HASTA JK - 200000000")
        c.drawString(120,h-165,"DCTO/EQUIVALENTE POS:    JK - 82373 ")
        c.drawString(120,h-180,"VIGENCIA HASTA: 13/12/2023 ")
        c.drawString(120,h-195,f"FECHA:  {datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year}       Hora:{hora}:{minu}:{seg}")
        c.drawString(120,h-210,"CAJERO: BERMEO DUERO VALENTINA  ")
        c.drawString(100,h-225,"======================================")
        c.drawString(115,h-240,"Uds DESCRIPCION       PRECIO         TOTAL ")
        c.drawString(100,h-255,"======================================")
        
      
        for todo in self.lista_productos:
            c.drawString(125,h-270, f" {todo.cantidad}         {todo.nombre}                    {todo.precio:.0f}            {todo.costo_total:.0f}")
            h=h-15
        c.drawString(100,h-300,"======================================")
        c.drawString(185,h-315,f"                 SUBTOTAL  {self.monto:.0f}  ")
        c.drawString(185,h-330,f"                 IVA    {self.monto * 0.19:.0f} ")
        c.drawString(185,h-345,f"                 TOTAL   {self.monto + (self.monto *  0.19):.0f}   ")
        c.drawString(100,h-360,"======================================")
        c.drawString(140,h-375," DISCRIMINACION DE IMPUESTOS ")
        c.drawString(123,h-390,f" I BASE 19%   {self.monto:.0f}  IVA             {self.monto * 0.19:.0f}  ")
        c.drawString(152,h-405,f"   TOTAL   {self.monto:.0f}                  {self.monto *  0.19:.0f}   ")
        c.drawString(100,h-420,"======================================")
        c.drawString(185,h-435," FORMA DE PAGO ")
        c.drawString(155,h-450,f" EFECTIVO  {self.monto + (self.monto *  0.19):.0f}  ")
        c.drawString(100,h-465,"======================================")
        c.drawString(150,h-480," ! GRACIAS POR TU COMPRA ! ")
        c.drawString(145,h-495," ! Unete a nuestro programa de  ")
        c.drawString(149,h-510," fidelizacion Exito Servicios ! ")


        c.drawImage("QR_c.png",170, h-620, width=100, height=100)
        c.drawString(145,h-640,"     www.Exito_Ser.com.co ")
        c.drawString(149,h-655," Registrate con el codigo: 13 ")
        c.drawString(100,h-670,"======================================")
        c.drawString(180,h-685,f" Cliente: {self.nombrecli} ")
        c.drawString(180,h-700,f" Cedula:  {self.cedulacli} ")
        c.drawString(100,h-715,"======================================")
        c.drawString(120,h-730,"Tiquete POS impuesto por software ServiSoft ")
        c.drawString(122,h-745,"  Desarrollado por ING  NIT:600098764-0  ")
        c.drawString(100,h-760,"======================================")
        c.drawString(185,h-775," tiquete POS ")
        c.drawString(175,h-790," ServiSoft.com.co ")
        c.drawString(175,h-805," _                     _ ")
        

        c.save()

        
    def fin (self):
        print('=' * 30)
        print( "          EL EXITO.COM     ")
        print('=' * 30)
        #self.datos()
        self.re_productos()
        self.procesar_fac()
        print('-' * 30)

factura=todo()
factura.datos()
#factura = todo( lista_productos=[])
factura.Qr()
factura.fin()
