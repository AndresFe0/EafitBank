from CuentaAhorros import CuentaAhorros
from CuentaGrupal import CuentaGrupal
import datetime


class Usuario:
    num = 0

    @classmethod
    def generar_valor(cls):
        cls.num += 1
        return cls.num

    def __init__(self, nombre_apellido: str, contrasena: str ):
        self._nombre_apellido = nombre_apellido
        self._contrasena = contrasena
        self._porcentaje_mi_cuenta_grupal = 0.03  # Porcentaje mensual
        self._porcentaje_otra_cuenta_grupal = 0.05  # Porcentaje mensual
        self._cuenta_ahorros = CuentaAhorros()
        self._mi_cuenta_grupal = None
        self._cuentas_grupales = []
        self._historia = ""
        self._deudas = {}

    def ingresar_dinero_otra_cuenta_grupal(self, valor, grupo):
        self.agregar_historial_antes("Ingreso dinero a una cuenta grupal", valor)
        if self._cuenta_ahorros.valor > valor:
            self._cuenta_ahorros.valor -= valor
            grupo.valor += valor
            grupo.inversion_usuarios[self] += valor
        else:
            print("No tiene dinero suficiente...")
        self.agregar_historial_despues()

    def ingresar_dinero_mi_cuenta_grupal(self, valor):
        self.agregar_historial_antes("Ingreso dinero a mi cuenta grupal", valor)
        if self._cuenta_ahorros.valor > valor:
            self._cuenta_ahorros.valor -= valor
            self._mi_cuenta_grupal.valor += valor
            self._mi_cuenta_grupal.inversion_usuarios[self] += valor
            self.agregar_historial_despues()
        else:
            print("No tiene dinero suficiente...")

    def comprobar_si_hay_menos_dinero_que_valor(self, valor):
        if self._cuenta_ahorros.valor < valor:
            return False
        else:
            return True

    def ingresar_dinero_cuenta_ahorro(self, value):
        self.agregar_historial_antes("Ingreso dinero a cuenta de ahorros personal", value)
        new_value = self._cuenta_ahorros.valor + value
        self._cuenta_ahorros.valor = new_value
        self.agregar_historial_despues()

    def crear_mi_grupo_de_ahorro(self, nombre_del_grupo):
        self._mi_cuenta_grupal = CuentaGrupal(nombre_del_grupo, self)
        print(f"se ha creado una cuenta grupal exitosamente: con el nombre-->{nombre_del_grupo}")

    def invitar_mi_grupo_ahorros(self, usuario):
        if len(self._mi_cuenta_grupal.usuarios) > 2:
            print(f"La persona {usuario.nombre_apellido} no puede ingresar ya que no hay cupos")
        elif len(usuario.cuentas_grupales) >= 3:
            print(f"La persona {usuario.nombre_apellido} esta en mas de tres grupos de ahorro")
        else:
            self.mi_cuenta_grupal.usuarios.append(usuario)
            self.mi_cuenta_grupal.inversion_usuarios[usuario] = 0
            usuario.cuentas_grupales.append(self._mi_cuenta_grupal)


    def solicitar_prestamo_grupo(self, cuenta_grupal, valor, plazo):
        if valor > cuenta_grupal.inversion_usuarios[self]:
            print("No puede pedir prestamo, ya que esta pidiendo mas dinero del que ha aportado...")
        else:
            self.agregar_historial_antes("Solicitud prestamo mis grupos", valor)
            cuenta_grupal.deudas_grupo[self][0] += valor
            cuenta_grupal.deudas_grupo[self][1] += plazo
            cuenta_grupal.valor -= valor
            self._cuenta_ahorros.valor += valor
            self.deudas[self.generar_valor()] = cuenta_grupal
            self.agregar_historial_despues()

    # def solicitar_prestamo_otro_grupo(self, cuenta_grupal, valor):
    #     if valor > cuenta_grupal.inversion_usuarios[self]:
    #         print("No puede pedir prestamo, ya que esta pidiendo mas dinero del que ha aportado...")
    #     else:
    #         self.agregar_historial_antes("Solicitud prestamo otro grupo", valor)
    #         cuenta_grupal.deudas_del_grupo[self] += valor
    #         cuenta_grupal.valor -= valor
    #         self._cuenta_ahorros.valor += valor
    #         self.agregar_historial_despues()

    def comprobar_deudas(self):
        for clave, valor in self.deudas.items():
            print(f"{clave}.En el grupo de: {valor.dueno_cuenta}, con el nombre de: {valor.nombre_cuenta}, se debe: {valor.deudas_grupo[self][0]}, en un plazo de {valor.deudas_grupo[self][1]}\n")

    def pagar_deuda(self):
        self.comprobar_deudas()
        eleccion = int(input("elija la deuda a pagar"))
        if self._deudas[eleccion] in self.cuentas_grupales:
            meses = int(input("Ingrese numero de meses que desea pagar"))
            deuda = self._deudas[eleccion].deudas_del_grupo[self][0]
            total_a_pagar = deuda + deuda*(self._porcentaje_mi_cuenta_grupal*meses)
            if total_a_pagar > self.cuenta_ahorros.valor:
                print("No posee todo el dinero a pagar")
            else:
                self.agregar_historial_antes("Pago deuda", total_a_pagar)
                self._cuenta_ahorros -= total_a_pagar
                self._deudas[eleccion].deudas_grupo[self][0] -= total_a_pagar
                self._deudas[eleccion].deudas_grupo[self][1] -= meses
                self._deudas[eleccion].valor += total_a_pagar
                self.agregar_historial_despues()
        else:
            meses = int(input("Ingrese numero de meses que desea pagar"))
            deuda = self._deudas[eleccion].deudas_grupo[self][0]
            total_a_pagar = deuda + deuda * (self._porcentaje_otra_cuenta_grupal * meses)
            if total_a_pagar > self.cuenta_ahorros.valor:
                print("No posee todo el dinero a pagar")
            else:
                self.agregar_historial_antes("Pago deuda", total_a_pagar)
                self._cuenta_ahorros.valor -= total_a_pagar
                self._deudas[eleccion].deudas_grupo[self][0] -= deuda
                self._deudas[eleccion].deudas_grupo[self][1] -= meses
                self._deudas[eleccion].valor += total_a_pagar
                self.agregar_historial_despues()

    def agregar_historial_antes(self, tipo_movimiento, monto):
        date = datetime.datetime.now()
        modify_date = date.strftime("%Y-%m-%d %H:%M")
        self.historia += f"-Tipo_movimiento: {tipo_movimiento}\n    *Fecha y hora: {modify_date}\n    *Saldo antes: {self._cuenta_ahorros.valor}\n    *Monto: {monto}\n    "

    def agregar_historial_despues(self):
        self._historia += f"*Saldo final: {self.cuenta_ahorros.valor}\n"

    @property
    def nombre_apellido(self):
        return self._nombre_apellido
    
    @nombre_apellido.setter
    def nombre_apellido(self, nombre_apellido):
        self._nombre_apellido = nombre_apellido
        
    @property
    def contrasena(self):
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, contrasena):
        self.contrasena = contrasena
        
    @property
    def porcentaje_mi_cuenta(self):
        return self._porcentaje_mi_cuenta_grupal
    
    @porcentaje_mi_cuenta.setter
    def porcentaje_mi_cuenta(self, porcentaje_mi_cuenta):
        self._porcentaje_mi_cuenta_grupal = porcentaje_mi_cuenta
        
    @property
    def porcentaje_otras_cuentas_grupales(self):
        return self._porcentaje_otra_cuenta_grupal

    @porcentaje_otras_cuentas_grupales.setter
    def porcentaje_otras_cuentas_grupales(self, porcentaje_otra_cuenta_grupal):
        self._porcentaje_otra_cuenta_grupal = porcentaje_otra_cuenta_grupal

    @property
    def cuenta_ahorros(self):
        return self._cuenta_ahorros

    @cuenta_ahorros.setter
    def cuenta_ahorros(self, cuenta_ahorros):
        self._cuenta_ahorros = cuenta_ahorros

    @property
    def mi_cuenta_grupal(self):
        return self._mi_cuenta_grupal

    @mi_cuenta_grupal.setter
    def mi_cuenta_grupal(self, mi_cuenta_grupal):
        self._mi_cuenta_grupal = mi_cuenta_grupal

    @property
    def cuentas_grupales(self):
        return self._cuentas_grupales

    @cuentas_grupales.setter
    def cuentas_grupales(self, cuentas_grupales):
        self._cuentas_grupales.append(cuentas_grupales)

    @property
    def deudas(self):
        return self._deudas

    @deudas.setter
    def deudas(self, deudas):
        self._deudas = deudas

    @property
    def historia(self):
        return self._historia

    @historia.setter
    def historia(self, historia):
        self._historia = historia



if __name__ == "__main__":
    us = Usuario("adpda", "dadsa")
    us.ingresar_dinero_cuenta_ahorro(232)
    #print(us.cuenta_ahorros.valor)
