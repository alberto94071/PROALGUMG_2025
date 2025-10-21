# Directorio de Entidades del Estado - Proyecto de Algoritmos

Este es un proyecto universitario para el curso de Algoritmos, desarrollado en Python con una interfaz gráfica (GUI) usando Tkinter.

## Descripción

El software es un sistema de escritorio que permite gestionar un directorio de entidades del estado. El programa cuenta con un sistema de inicio de sesión y diferenciación de roles (Administrador y Usuario), permitiendo un control de acceso a la información.

## 🚀 Características

* **Sistema de Login:** Verificación de credenciales con un límite de 3 intentos.
* **Registro de Usuarios:** Permite la creación de nuevas cuentas de "usuario".
* **Registro de Administradores:** Sistema de registro protegido por un código secreto (`UMG2025`).
* **Panel de Administrador:** Permite gestionar las entidades (CRUD):
    * **C**rear nuevas entidades.
    * **R**eer (visualizar) el listado completo.
    * **U**pdate (modificar) entidades existentes.
    * **D**elete (eliminar) entidades.
* **Panel de Usuario:** Vista de **solo lectura** del directorio de entidades.
* **Gestión de Datos:** La aplicación maneja campos como ID, Nombre, Tipo, Dirección, Teléfono y URL del sitio web.

## 💻 Cómo Ejecutar

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1.  Asegúrate de tener **Python 3** instalado en tu sistema.
2.  Descarga o clona este repositorio:
    ```bash
    git clone [https://github.com/](https://github.com/)[tu-usuario]/[tu-repositorio].git
    ```
3.  Navega a la carpeta del proyecto:
    ```bash
    cd [ubicación-de-la-carpeta]
    ```
4.  Ejecuta el script principal de Python:
    ```bash
    python ENTIDADES_ESTADO.py
    ```
    (No se requieren instalaciones adicionales, ya que **Tkinter** viene incluido con Python).

## 🔑 Credenciales de Prueba

Puedes usar las siguientes credenciales para probar la aplicación:

* **Administrador:**
    * **Usuario:** `ADMIN`
    * **Contraseña:** `ADMIN`
* **Usuario Normal:**
    * **Usuario:** `INVITADO`
    * **Contraseña:** `0000`

Para registrar un nuevo administrador, usa el código: `UMG2025`

## Autores
 ```bash
* JEIMY VANESA GÓMEZ LÓPEZ - 0903-25-#####
* CESIA DANIELA LÓPEZ MORALES - 0903-25-#####.
* JOAQUIN DANIEL MALDONADO VELÁSQUEZ - 0903-25-#####.
* IVANA MARCELA MALIN DE LEÓN - 0903-25-#####.
* RONY ALBERTO MÉNDEZ FUENTES - 0903-25-29637.
```
