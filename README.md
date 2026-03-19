# 2526-POO-SEMANA14-ANA-PANCHI
Aplicación de escritorio con interfaz gráfica utilizando Tkinter en Python, aplicando arquitectura modular por capas (Modelos, Servicios, UI y Main).

Sistema de Registro de Visitantes
##Descripción

Este proyecto es una aplicación desarrollada en Python que permite gestionar el registro de visitantes mediante una interfaz gráfica.
El sistema permite agregar, listar y eliminar visitantes de manera sencilla.

##Funcionalidades
✔ Registrar visitantes (cédula, nombre, motivo)
✔ Listar todos los visitantes en una tabla
✔ Eliminar visitantes seleccionados
✔ Limpiar campos del formulario
✔ Actualizar informacion de visitante seleccionado

## Estructura del proyecto

visitas_app/
│
├── modelos/
│ └── visitante.py
│
├── servicios/
│ └── visita_servicio.py
│
├── ui/
│ └── app_tkinter.py
│
└── main.py

## Validaciones
- No se permiten campos vacíos.
- No se permiten cédulas duplicadas.
- Se debe seleccionar un registro para eliminar o actualizar.

## Actualización de visitantes
Para actualizar un visitante es obligatorio seleccionar un registro antes de actualizar.

## Eliminación de visitantes
La eliminación se realiza usando la selección de la tabla.

## Selección de registros
Al hacer clic en una fila de la tabla:
- Los datos se cargan automáticamente en los campos.
- Se habilita la edición del registro.