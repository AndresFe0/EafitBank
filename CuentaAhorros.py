class CuentaAhorros:
    def __init__(self):
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

    def __str__(self):
        return f"cuenta de ahorros con: {self._valor}"
