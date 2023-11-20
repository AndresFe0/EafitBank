from Usuario import Usuario
from functools import *

class EafitBank:
    cero = 1
    @classmethod
    def generar_valor(cls):
        cls.cero += 1
        return cls.cero
    @classmethod
    def degenerar_valor(cls):
        cls.cero = 1

    def __init__(self):
        self._valor = 0
        self._usuarios = []
        self._cuentas_grupales = []

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def indetificar_usuarios_sobresalientes(self):
        pass

    def acceder_cuenta(self, usuario, contrasena):
        for user in self._usuarios:
            if user.nombre_apellido == usuario:
                if user.contrasena == contrasena:
                    return user
                else:
                    print("Contraseña equivocada..")
                    return False

        print("El usuario no existe, intente de nuevo")
        return False

    def retornar_usuario(self, nombre):
        for i in self._usuarios:
            if nombre == i.nombre_apellido:
                return i

    def existe_usuario(self, nombre_usuario):
        if nombre_usuario in list(map(lambda x: x.nombre_apellido, self._usuarios)):
            return True
        else:
            print("El Usuario no exite")
            return False

    def agregar_usuario_grupo_ahorros(self, usuario_de_la_cuenta:Usuario, nombre_usuario_invitar):
        if self.existe_usuario(nombre_usuario_invitar):
            usuario_invitar = self.retornar_usuario(nombre_usuario_invitar)
            if len(usuario_invitar.cuentas_grupales) < 4:
                if len(usuario_de_la_cuenta.mi_cuenta_grupal.usuarios) < 4:
                    print("Usuario agregado correctamente")
                    usuario_de_la_cuenta.invitar_mi_grupo_ahorros(self.retornar_usuario(nombre_usuario_invitar))
                    usuario_invitar.cuentas_grupales.append(usuario_de_la_cuenta.mi_cuenta_grupal)
                else:
                    print("El grupo no tiene mas espacios disponibles")
            else:
                print(f"El usuario a añadir: {nombre_usuario_invitar}, no puede ser añadido a mas cuentas grupales")

    def ingresar_dinero_cuenta_ahorro(self, usuario, valor):
        self._valor += valor*0.01
        usuario.ingresar_dinero_cuenta_ahorro(valor-valor*0.01)

    def ingresar_dinero_mi_cuenta_grupal(self, usuario, valor):
        if usuario.comprobar_si_hay_menos_dinero_que_valor(valor):
            usuario.ingresar_dinero_mi_cuenta_grupal(valor-valor*0.01)
        else:
            print("Esta tratando de ingresar mas dinero del que tiene en su cuenta de ahorros")

    def ingresar_dinero_otra_cuenta_grupal(self, usuario, valor):
        if usuario.comprobar_si_hay_menos_dinero_que_valor(valor):
            print("Elija a cual grupo desea realizar deposito de dinero:")
            for i in usuario.cuentas_grupales:
                print(f"    -{i.nombre_cuenta}")
            cuenta = input("nombre de la cuenta->")
            for i in usuario.cuentas_grupales:
                if i.nombre_cuenta == cuenta:
                    self._valor += valor * 0.01
                    usuario.ingresar_dinero_otra_cuenta_grupal(valor-valor*0.01, i)
                    break
                else:
                    print("La cuenta no existe!!")
        else:
            print("Esta tratando de ingresar mas dinero del que tiene en su cuenta de ahorros")

    def invitar_grupo(self, usuario, nombre_usuario):
        for i in self._usuarios:
            if i.nombre_apellido == nombre_usuario:
                usuario.invitar_mi_grupo_ahorros(i)
                break

    def pedir_prestamo_mi_grupo(self, usuario, monto):
        plazo = int(input("Numero de meses a pagar -->"))
        if plazo > 2:
            grupos = {}
            print(f"SUS GRUPOS:\n1.Tu grupo: {usuario.mi_cuenta_grupal.nombre_cuenta}\n")
            grupos[1] = usuario.mi_cuenta_grupal
            for i in usuario.cuentas_grupales:
                num = self.generar_valor()
                print(f"{num}.Grupo de: {i.dueno_cuenta}, llamado: {i.nombre_cuenta}\n")
                grupos[num] = i
            self.degenerar_valor()
            eleccion = int(input("Elija su grupo --> "))
            grupo_final = grupos[eleccion]
            usuario.solicitar_prestamo_grupo(grupo_final, monto, plazo)
        else:
            print("los meses a pagar debe ser mayor a 2 meses")

    def pedir_prestamo_otro_grupo(self, usuario, monto):
        otros_grupos = {}
        x = 1
        amigos_usuarios = []
        plazo = int(input("Numero de meses a pagar -->"))
        if plazo > 2:
            for i in usuario.cuentas_grupales:
                for j in i.usuarios:
                    if j not in amigos_usuarios:
                        amigos_usuarios.append(j)
            for i in self._cuentas_grupales:
                if usuario not in i.usuarios and self.al_menos_un_elemento_en_comun(amigos_usuarios, i):
                    print(f"{x}.Grupo de: {i.dueno_cuenta}, llamado: {i.nombre_cuenta}\n")
                    otros_grupos[x] = i.usuarios
                    x += 1

            if len(otros_grupos) == 0:
                print("No hay grupos al que puedas pedir dinero")
            else:
                eleccion = int(input("Elija el grupo --> "))
                grupo_final = otros_grupos[eleccion]
                usuario.solicitar_prestamo_grupo(grupo_final, monto, plazo)
        else:
            print("los meses a pagar debe ser mayor a 2 meses")

    def disolver_cuenta(self, usuario):
        deudas = 0
        for clave, valor in usuario.mi_cuenta_grupal.deudas_grupo.items():
            deudas += valor[0]
        if deudas == 0:
            total_menos_comision = usuario.mi_cuenta_grupal.valor - usuario.mi_cuenta_grupal.valor * 0.05
            self._valor += usuario.mi_cuenta_grupal.valor * 0.05
            for clave, valor in usuario.mi_cuenta_grupal.inversion_usuarios.items():
                porcentaje = (valor/usuario.mi_cuenta_grupal.valor)
                clave.cuenta_ahorros.valor += total_menos_comision*porcentaje

            for i in usuario.mi_cuenta_grupal.usuarios:
                for j in i.cuentas_grupales:
                    if j == usuario.mi_cuenta_grupal:
                        i.cuentas_grupales.remove(j)


            usuario.mi_cuenta_grupal = None



        else:
            print("Todavia hay deudas!!")

    def al_menos_un_elemento_en_comun(self, x, y):
        conjunto_x = set(x)
        conjunto_y = set(y)

        if conjunto_x.intersection(conjunto_y):
            return True
        else:
            return False


    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def usuarios(self):
        return self._usuarios

    @usuarios.setter
    def usuarios(self, usuarios):
        self._usuarios = usuarios

    @property
    def cuentas_grupales(self):
        return self._cuentas_grupales

    @cuentas_grupales.setter
    def cuentas_grupales(self, cuentas_grupales):
        self._cuentas_grupales = cuentas_grupales

