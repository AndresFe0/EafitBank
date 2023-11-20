from Menuu import Menuu
from EafitBank import EafitBank
from Usuario import Usuario
from CuentaAhorros import CuentaAhorros
from functools import partial

menu = Menuu()
banco = EafitBank()
us1 = Usuario("Andres Felipe Prieto", "1234")
us2 = Usuario("Juan Alfonso Restrepo", "0515")
us3 = Usuario("Gilberto Ortiz Rendon", "2311")
us4 = Usuario("Roberto Castañeda", "788")
us5 = Usuario("Julian Alvarez Rendon", "61dws")
us6 = Usuario("David Mejia Ortiz", "3510")
us7 = Usuario("Jorge Carrascal", "0000")
us8 = Usuario("Luis Diaz", "C2-B0")


banco.agregar_usuario(us1)
banco.agregar_usuario(us2)
banco.agregar_usuario(us3)
banco.agregar_usuario(us4)
banco.agregar_usuario(us5)
banco.agregar_usuario(us6)
banco.agregar_usuario(us7)
banco.agregar_usuario(us8)



mi_usuario = None

mi_usuario = banco.acceder_cuenta("Andres Felipe Prieto", "1234")
banco.ingresar_dinero_cuenta_ahorro(mi_usuario, 2000)
mi_usuario.crear_mi_grupo_de_ahorro("viaje")
banco.ingresar_dinero_mi_cuenta_grupal(mi_usuario, 500)
banco.invitar_grupo(mi_usuario, "Juan Alfonso Restrepo")
banco.invitar_grupo(mi_usuario, "Gilberto Ortiz Rendon")
banco.invitar_grupo(mi_usuario, "Roberto Castañeda")
banco.invitar_grupo(mi_usuario, "Julian Alvarez Rendon")
mi_usuario.mi_cuenta_grupal.imprimir_usuarios()
us2.crear_mi_grupo_de_ahorro("Rolex")
banco.invitar_grupo(us2, "Andres Felipe Prieto")
banco.invitar_grupo(us2, "Juan Alfonso Restrepo")
banco.invitar_grupo(us2, "Gilberto Ortiz Rendon")
us3.crear_mi_grupo_de_ahorro("hola")
banco.invitar_grupo(us3, "Andres Felipe Prieto")
us4.crear_mi_grupo_de_ahorro("goood")
us5.crear_mi_grupo_de_ahorro("sadad")
banco.invitar_grupo(us4, "Andres Felipe Prieto")

banco.ingresar_dinero_cuenta_ahorro(us2, 1000)

banco.ingresar_dinero_otra_cuenta_grupal(us2, 300)
print(mi_usuario.mi_cuenta_grupal)
print(mi_usuario.cuenta_ahorros.valor)
banco.pedir_prestamo_mi_grupo(mi_usuario, 200)
print(mi_usuario.mi_cuenta_grupal)
print(mi_usuario.cuenta_ahorros.valor)
banco.disolver_cuenta(mi_usuario)
print(mi_usuario.cuenta_ahorros.valor)
mi_usuario.pagar_deuda()
print(mi_usuario.cuenta_ahorros.valor)
print(mi_usuario.mi_cuenta_grupal)
#
# while True:
#     menu.menu_inicio()
#
#     eleccion = int(input("eleccion-->"))
#     if eleccion not in [1,2,3]:
#         print("valor incorrecto...")
#     if eleccion == 3:
#         break
#     if eleccion == 1:
#         banco.agregar_usuario(Usuario(input("Nombre->"), input("contrasena->")))
#     if eleccion == 2:
#         usuario = str(input("Nombre->"))
#         contrasena = str(input("Contraseña->"))
#         # mi_usuario = banco.acceder_cuenta(usuario, contrasena)
#         mi_usuario = banco.acceder_cuenta("Andres Felipe Prieto", "1234")
#         if mi_usuario:
#             while True:
#                 menu.menu_despues_de_inicio()
#                 eleccion = int(input("que desea realizar->"))
#                 if 0 <= eleccion <= 8:
#
#                     if eleccion == 0:
#                         banco.ingresar_dinero_cuenta_ahorro(mi_usuario, int(input("Dinero a depositar->")))
#                     elif eleccion == 1:
#                         mi_usuario.crear_mi_grupo_de_ahorro(input("Ingrese el nombre del grupo->"))
#                     elif eleccion == 2:
#                         banco.ingresar_dinero_otra_cuenta_grupal(mi_usuario, int(input("Ingrese el monto que desea meter en una cuenta de grupo->")))
#                     elif eleccion == 3:
#                         banco.ingresar_dinero_mi_cuenta_grupal(mi_usuario, int(input("Ingrese el monto que desea meter en su cuenta de grupo->")))
#                     elif eleccion == 4:
#                         banco.invitar_grupo(mi_usuario, input("ingrese el nombre del usuario que desea invitar->"))
#                     elif eleccion == 5:
#                         banco.pedir_prestamo_mi_grupo(mi_usuario, int(input("Cuanto desea ingresar->")))
#                     elif eleccion == 6:
#                         banco.pedir_prestamo_otro_grupo(mi_usuario, int(input("Cuanto desea ingresar->")))
#                     elif eleccion == 7:
#                         banco.disolver_cuenta(mi_usuario)
#                     elif eleccion == 8:
#                         break
#
#
#

