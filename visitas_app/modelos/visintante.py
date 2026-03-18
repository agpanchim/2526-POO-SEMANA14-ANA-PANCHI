class Visitante:
    """
    Clase modelo que representa un visitante.
    """

    def __init__(self, cedula: str, nombre: str, motivo: str):
        """
        Constructor de la clase.
        Inicializa los atributos usando encapsulamiento.
        """
        self._cedula = cedula
        self._nombre = nombre
        self._motivo = motivo

    # ===== CÉDULA =====
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value: str):
        self._cedula = value

    # ===== NOMBRE =====
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    # ===== MOTIVO =====
    @property
    def motivo(self):
        return self._motivo

    @motivo.setter
    def motivo(self, value: str):
        self._motivo = value