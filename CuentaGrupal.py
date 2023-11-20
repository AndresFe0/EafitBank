class CuentaGrupal:
    def __init__(self, nombre_de_cuenta, dueno_cuenta):
        self._valor = 0
        self._nombre_cuenta = nombre_de_cuenta
        self._dueno_cuenta = dueno_cuenta
        self._usuarios = [dueno_cuenta]
        self._inversion_usuarios = {dueno_cuenta: 0}
        self._deudas_del_grupo = {dueno_cuenta: [0,0]}  # [0]-> valor| [1]-> plazo

    def estado_agregacion(self):
        pass

    def agregar_usuario(self, usuario):
        pass

    def comprobar_inversion(self, usuario):
        pass

    def pagar_al_disolver(self):
        pass

    def imprimir_usuarios(self):
        x = 1
        for i in self._usuarios:
            print(f"{x}usuario: {i.nombre_apellido}")
            x += 1

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def nombre_cuenta(self):
        return self._nombre_cuenta

    @nombre_cuenta.setter
    def nombre_cuenta(self, nombre_cuenta):
        self._nombre_cuenta = nombre_cuenta

    @property
    def dueno_cuenta(self):
        return self._dueno_cuenta

    @dueno_cuenta.setter
    def dueno_cuenta(self, dueno_cuenta):
        self._dueno_cuenta = dueno_cuenta

    @property
    def usuarios(self):
        return self._usuarios

    @usuarios.setter
    def usuarios(self, usuarios):
        self._usuarios = usuarios

    @property
    def inversion_usuarios(self):
        return self._inversion_usuarios

    @inversion_usuarios.setter
    def inversion_usuarios(self, inversion_usuarios):
        self._inversion_usuarios = inversion_usuarios

    @property
    def deudas_grupo(self):
        return self._deudas_del_grupo

    @deudas_grupo.setter
    def deudas_grupo(self, deudas_grupo):
        self._deudas_del_grupo = deudas_grupo

    def __str__(self):
        return (f"Dueno Cuenta = {self._dueno_cuenta.nombre_apellido}\n"
                f"Nombre_grupo = {self._nombre_cuenta}\n"
                f"Inversion = {self.inversion_usuarios}\n"
                f"Deudas = {self.deudas_grupo}")
