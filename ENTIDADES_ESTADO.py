# Importa la librería de interfaz gráfica de Python
import tkinter as tk
from tkinter import messagebox, ttk

# ----------------------------------------------------------------
# MODELO DE DATOS
# ----------------------------------------------------------------

# Lista de diccionarios que funciona como base de datos de usuarios.
usuarios_registrados = [
    {"usuario": "ADMIN", "contrasena": "ADMIN", "rol": "administrador"},
    {"usuario": "INVITADO", "contrasena": "0000", "rol": "usuario"}
]


entidades_registradas = [
    {"id": 1, "nombre": "Ministerio de Salud Pública", "tipo": "Salud", "direccion": "6Av. 3-45 zona 11, Guatemala", "telefono": "2444-7474", "url": "https://www.mspas.gob.gt/"},
    {"id": 2, "nombre": "Policía Nacional Civil", "tipo": "Seguridad", "direccion": "Zona 1, Guatemala", "telefono": "110", "url": "https://www.pnc.gob.gt/"},
    {"id": 3, "nombre": "Ministerio de Educación", "tipo": "Educación", "direccion": "Zona 10, Guatemala", "telefono": "2411-9595", "url": "https://www.mineduc.gob.gt/"}
]
# Variable global para llevar el conteo del siguiente ID disponible.
siguiente_id = 4

# ----------------------------------------------------------------
# LÓGICA DE LA APLICACIÓN (Usuarios)
# ----------------------------------------------------------------

def validar_login(usuario, contrasena):
    """
    Función que valida las credenciales ingresadas.
    """
    for u in usuarios_registrados:
        if u["usuario"] == usuario and u["contrasena"] == contrasena:
            return u["rol"]
    return None

def registrar_usuario(usuario, contrasena, codigo=""):
    """
    Función que registra un nuevo usuario en el sistema.
    Si el código de administrador es correcto, asigna el rol correspondiente.
    """
    CODIGO_ADMIN = "UMG2025" 
    for u in usuarios_registrados:
        if u["usuario"] == usuario:
            return False
    
    rol_asignado = "administrador" if codigo == CODIGO_ADMIN else "usuario"
    usuarios_registrados.append({
        "usuario": usuario,
        "contrasena": contrasena,
        "rol": rol_asignado
    })
    return True

# ----------------------------------------------------------------
# VISTA (INTERFAZ GRÁFICA)
# ----------------------------------------------------------------

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Directorio de Entidades del Estado")
        # Se aumenta el ancho de la ventana para la nueva columna
        self.root.geometry("1000x600") 
        
        self._frame = None
        self.cambiar_frame(FrameInicial)

    def cambiar_frame(self, clase_frame):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = clase_frame(self.root, self)
        self._frame.pack(fill="both", expand=True, padx=10, pady=10)

class FrameInicial(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        tk.Label(self, text="Bienvenido al Sistema", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Iniciar Sesión", command=self.ir_a_login, width=30).pack(pady=15)
        tk.Button(self, text="Registrarse", command=self.ir_a_registro, width=30).pack(pady=15)
        tk.Button(self, text="Salir", command=self.app.root.quit, width=20).pack(pady=20)
    def ir_a_login(self): self.app.cambiar_frame(FrameLogin)
    def ir_a_registro(self): self.app.cambiar_frame(FrameRegistro)

class FrameLogin(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        self.intentos = 0
        tk.Label(self, text="Inicio de Sesión", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self, text="Usuario:").pack()
        self.entry_usuario = tk.Entry(self, width=30)
        self.entry_usuario.pack()
        tk.Label(self, text="Contraseña:").pack()
        self.entry_contrasena = tk.Entry(self, show="*", width=30)
        self.entry_contrasena.pack()
        tk.Button(self, text="Ingresar", command=self.intentar_login, width=20).pack(pady=20)
        tk.Button(self, text="Volver", command=self.volver).pack()
    def intentar_login(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        rol = validar_login(usuario, contrasena)
        if rol == "administrador":
            self.app.cambiar_frame(FrameAdmin)
        elif rol == "usuario":
            messagebox.showinfo("Acceso Correcto", f"Bienvenido, {usuario}.")
            self.app.cambiar_frame(FrameUsuario)
        else:
            self.intentos += 1
            restantes = 3 - self.intentos
            messagebox.showwarning("Error de Login", f"Credenciales incorrectas. Le quedan {restantes} intentos.")
            if self.intentos >= 3:
                messagebox.showerror("Bloqueado", "Ha superado el número de intentos.")
                self.app.root.quit()
    def volver(self): self.app.cambiar_frame(FrameInicial)

class FrameRegistro(tk.Frame):
    # (Sin cambios)
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        tk.Label(self, text="Registro de Nuevo Usuario", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self, text="Nuevo Usuario:").pack()
        self.entry_usuario = tk.Entry(self, width=30)
        self.entry_usuario.pack()
        tk.Label(self, text="Nueva Contraseña:").pack()
        self.entry_contrasena = tk.Entry(self, show="*", width=30)
        self.entry_contrasena.pack()
        tk.Label(self, text="Código de Administrador (opcional):").pack()
        self.entry_codigo = tk.Entry(self, width=30)
        self.entry_codigo.pack()
        tk.Button(self, text="Registrar", command=self.intentar_registro, width=20).pack(pady=20)
        tk.Button(self, text="Volver", command=self.volver).pack()
    def intentar_registro(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        codigo = self.entry_codigo.get()
        if not usuario or not contrasena:
            messagebox.showwarning("Campo Vacío", "Usuario y contraseña son obligatorios.")
            return
        if registrar_usuario(usuario, contrasena, codigo):
            messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente.")
            self.volver()
        else:
            messagebox.showerror("Error", "El nombre de usuario ya existe.")
    def volver(self): self.app.cambiar_frame(FrameInicial)

# --- CLASE MODIFICADA ---
class VentanaFormularioEntidad(tk.Toplevel):
    def __init__(self, parent, entidad_a_modificar=None):
        super().__init__(parent)
        self.parent = parent
        self.entidad_actual = entidad_a_modificar

        self.transient(self.parent)
        self.grab_set()
        self.geometry("300x280") # Un poco más alta para el nuevo campo
        
        frame_form = tk.Frame(self)
        frame_form.pack(padx=10, pady=10)

        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.grid(row=0, column=1)
        tk.Label(frame_form, text="Tipo:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_tipo = tk.Entry(frame_form, width=30)
        self.entry_tipo.grid(row=1, column=1)
        tk.Label(frame_form, text="Dirección:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_direccion = tk.Entry(frame_form, width=30)
        self.entry_direccion.grid(row=2, column=1)
        tk.Label(frame_form, text="Teléfono:").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_telefono = tk.Entry(frame_form, width=30)
        self.entry_telefono.grid(row=3, column=1)
        
        # --- NUEVO WIDGET ---
        tk.Label(frame_form, text="URL:").grid(row=4, column=0, sticky="w", pady=5)
        self.entry_url = tk.Entry(frame_form, width=30)
        self.entry_url.grid(row=4, column=1)
        # --- FIN NUEVO WIDGET ---

        tk.Button(self, text="Guardar", command=self.guardar).pack(pady=10)

        if self.entidad_actual:
            self.title("Modificar Entidad")
            self.entry_nombre.insert(0, self.entidad_actual["nombre"])
            self.entry_tipo.insert(0, self.entidad_actual["tipo"])
            self.entry_direccion.insert(0, self.entidad_actual["direccion"])
            self.entry_telefono.insert(0, self.entidad_actual["telefono"])
            self.entry_url.insert(0, self.entidad_actual.get("url", "")) # .get para evitar error si no existe
        else:
            self.title("Agregar Nueva Entidad")

    def guardar(self):
        nombre = self.entry_nombre.get()
        tipo = self.entry_tipo.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()
        url = self.entry_url.get() # Se obtiene el valor del nuevo campo

        # No se valida la URL como obligatoria
        if not nombre or not tipo or not direccion or not telefono:
            messagebox.showwarning("Campos incompletos", "Debe llenar todos los campos excepto la URL.", parent=self)
            return
            
        if self.entidad_actual:
            # --- Lógica de Modificación ---
            self.entidad_actual["nombre"] = nombre
            self.entidad_actual["tipo"] = tipo
            self.entidad_actual["direccion"] = direccion
            self.entidad_actual["telefono"] = telefono
            self.entidad_actual["url"] = url # Se guarda la URL
            messagebox.showinfo("Éxito", "Entidad actualizada correctamente.", parent=self)
        else:
            # --- Lógica de Creación (Agregar) ---
            global siguiente_id
            nueva_entidad = {
                "id": siguiente_id,
                "nombre": nombre,
                "tipo": tipo,
                "direccion": direccion,
                "telefono": telefono,
                "url": url # Se guarda la URL
            }
            entidades_registradas.append(nueva_entidad)
            siguiente_id += 1
            messagebox.showinfo("Éxito", "Entidad agregada correctamente.", parent=self)
        
        self.parent.actualizar_tabla()
        self.destroy()

# --- CLASE MODIFICADA ---
class FrameAdmin(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        
        tk.Label(self, text="Panel de Administrador", font=("Helvetica", 16)).pack(pady=10)
        
        # --- Definición de columnas modificada ---
        columnas = ("ID", "Nombre", "Tipo", "Direccion", "Telefono", "URL")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Direccion", text="Dirección")
        self.tree.heading("Telefono", text="Teléfono")
        self.tree.heading("URL", text="Página Web") # Nuevo encabezado
        
        self.tree.column("ID", width=30)
        self.tree.column("Nombre", width=150)
        self.tree.column("Tipo", width=100)
        self.tree.column("Direccion", width=150)
        self.tree.column("Telefono", width=100)
        self.tree.column("URL", width=200) # Nuevo ancho de columna
        # --- Fin modificación de tabla ---

        self.tree.pack(fill="both", expand=True)
        self.actualizar_tabla()

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)
        tk.Button(frame_botones, text="Agregar Entidad", command=self.agregar_entidad).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Modificar Entidad", command=self.modificar_entidad).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Eliminar Entidad", command=self.eliminar_entidad).pack(side="left", padx=5)
        tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=10)

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        # --- Inserción de datos modificada ---
        for entidad in entidades_registradas:
            valores = (
                entidad["id"], 
                entidad["nombre"], 
                entidad["tipo"], 
                entidad["direccion"], 
                entidad["telefono"],
                entidad.get("url", "") # Se usa .get para evitar errores si una entidad antigua no tiene "url"
            )
            self.tree.insert("", "end", values=valores)
    
    def agregar_entidad(self):
        VentanaFormularioEntidad(self)
    
    def modificar_entidad(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Por favor, seleccione una entidad para modificar.")
            return
        item_seleccionado = self.tree.item(seleccion[0])
        id_a_modificar = item_seleccionado['values'][0]
        entidad_encontrada = None
        for entidad in entidades_registradas:
            if entidad["id"] == id_a_modificar:
                entidad_encontrada = entidad
                break
        if entidad_encontrada:
            VentanaFormularioEntidad(self, entidad_encontrada)
        else:
            messagebox.showerror("Error", "No se encontró la entidad.")
    
    def eliminar_entidad(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Por favor, seleccione una entidad para eliminar.")
            return
        item_seleccionado = self.tree.item(seleccion[0])
        id_a_eliminar = item_seleccionado['values'][0]
        confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar '{item_seleccionado['values'][1]}'?")
        if confirmar:
            entidad_encontrada = None
            for entidad in entidades_registradas:
                if entidad["id"] == id_a_eliminar:
                    entidad_encontrada = entidad
                    break
            if entidad_encontrada:
                entidades_registradas.remove(entidad_encontrada)
                self.actualizar_tabla()
                messagebox.showinfo("Eliminado", "La entidad ha sido eliminada.")
            else:
                messagebox.showerror("Error", "No se encontró la entidad a eliminar.")
    
    def cerrar_sesion(self):
        self.app.cambiar_frame(FrameInicial)

# --- CLASE MODIFICADA ---
class FrameUsuario(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)
        self.app = app
        
        tk.Label(self, text="Directorio de Entidades", font=("Helvetica", 16)).pack(pady=10)
        
        # --- Definición de columnas modificada ---
        columnas = ("ID", "Nombre", "Tipo", "Direccion", "Telefono", "URL")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Direccion", text="Dirección")
        self.tree.heading("Telefono", text="Teléfono")
        self.tree.heading("URL", text="Página Web") # Nuevo encabezado
        
        self.tree.column("ID", width=30)
        self.tree.column("Nombre", width=150)
        self.tree.column("Tipo", width=100)
        self.tree.column("Direccion", width=150)
        self.tree.column("Telefono", width=100)
        self.tree.column("URL", width=200) # Nuevo ancho de columna
        # --- Fin modificación de tabla ---

        self.tree.config(selectmode="none") 
        self.tree.pack(fill="both", expand=True)
        self.actualizar_tabla()
        
        tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=20)

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        # --- Inserción de datos modificada ---
        for entidad in entidades_registradas:
            valores = (
                entidad["id"], 
                entidad["nombre"], 
                entidad["tipo"], 
                entidad["direccion"], 
                entidad["telefono"],
                entidad.get("url", "") # Se usa .get para seguridad
            )
            self.tree.insert("", "end", values=valores)
        
    def cerrar_sesion(self):
        self.app.cambiar_frame(FrameInicial)

# ----------------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ----------------------------------------------------------------

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = App(ventana_principal)

    ventana_principal.mainloop()
