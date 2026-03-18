class VisitaServicio:
    """
    Clase de servicio que maneja el CRUD de visitantes.
    """

    def __init__(self):

        self.visitantes = []

    def crear(self, visitante):

        # Validar que no exista la misma cédula
        if any(v.cedula == visitante.cedula for v in self.visitantes):
            raise ValueError("El visitante ya existe")

        self.visitantes.append(visitante)

    def listar_todo(self):

        return self.visitantes

    def eliminar(self, cedula):

        self.visitantes = [
            v for v in self.visitantes if v.cedula != cedula
        ]

    def actualizar(self, cedula, nuevo_nombre, nuevo_motivo):

        for v in self.visitantes:
            if v.cedula == cedula:
                v.nombre = nuevo_nombre
                v.motivo = nuevo_motivo
                return True
        return False