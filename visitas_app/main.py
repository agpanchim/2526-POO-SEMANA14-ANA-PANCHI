from servicios.visita_servicio import ServicioVisitante
from ui.app_tkinter import AppVisits

if __name__ == "__main__":
    servicio = ServicioVisitante()
    app = AppVisits(servicio)
    app.mainloop()