from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppVisits

if __name__ == "__main__":
    servicio = VisitaServicio()
    app = AppVisits(servicio)
    app.mainloop()