class ServicioVisitante:
    def __init__(self):
        self.visitantes = []

    def crear(self, visitante):
        for v in self.visitantes:
            if v.cedula == visitante.cedula:
                raise ValueError("Ya existe registro")
        self.visitantes.append(visitante)

    def listar_todo(self):
        return self.visitantes

    def eliminar(self, cedula):
        self.visitantes = [
            v for v in self.visitantes
            if str(v.cedula).strip().lstrip("0") != str(cedula).strip().lstrip("0")
        ]

    def actualizar(self, cedula_original, nombre, motivo):
        print("Buscando:", cedula_original)

        for v in self.visitantes:
            print("Comparando con:", v.cedula)

            if str(v.cedula).strip().lstrip("0") == str(cedula_original).strip().lstrip("0"):
                v.nombre = nombre
                v.motivo = motivo
                print("ACTUALIZADO")
                return True

        print("NO ENCONTRADO")
        return False