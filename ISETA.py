import hashlib
import tkinter as tk
from tkinter import messagebox

# Definir la estructura del nodo del árbol binario
class Nodo:
    def __init__(self, hash_value):
        self.hash_value = hash_value
        self.izquierdo = None
        self.derecho = None

# Definir la clase del árbol binario de búsqueda
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, hash_value):
        if self.raiz is None:
            self.raiz = Nodo(hash_value)
        else:
            self._insertar_recursivo(self.raiz, hash_value)
    
    def _insertar_recursivo(self, nodo, hash_value):
        if hash_value < nodo.hash_value:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(hash_value)
            else:
                self._insertar_recursivo(nodo.izquierdo, hash_value)
        elif hash_value > nodo.hash_value:
            if nodo.derecho is None:
                nodo.derecho = Nodo(hash_value)
            else:
                self._insertar_recursivo(nodo.derecho, hash_value)
    
    def buscar(self, hash_value):
        return self._buscar_recursivo(self.raiz, hash_value)
    
    def _buscar_recursivo(self, nodo, hash_value):
        if nodo is None:
            return False
        if hash_value == nodo.hash_value:
            return True
        elif hash_value < nodo.hash_value:
            return self._buscar_recursivo(nodo.izquierdo, hash_value)
        else:
            return self._buscar_recursivo(nodo.derecho, hash_value)

def url_to_hash(url):
    # Codificar la URL a bytes
    url_bytes = url.encode('utf-8')
    
    # Crear un objeto hash usando SHA-256
    sha256_hash = hashlib.sha256()
    
    # Actualizar el objeto hash con los bytes de la URL
    sha256_hash.update(url_bytes)
    
    # Obtener el hash hexadecimal
    hex_digest = sha256_hash.hexdigest()
    
    return hex_digest

def comparacion(hash_value, arbol):
    # Buscar el hash en el árbol binario de búsqueda
    return arbol.buscar(hash_value)

def verificar_url():
    url = url_entry.get()
    hash_value = url_to_hash(url)
    result = comparacion(hash_value, arbol)
    if result:
        messagebox.showinfo("Resultado", "La web es verdadera")
    else:
        messagebox.showwarning("Resultado", "La web es falsa")

# Crear el árbol binario de búsqueda y llenar con hashes predefinidos
arbol = ArbolBinarioBusqueda()
hashes_predefinidos = [
    "724af556ca1044cbee2a2676cf35d8ff155192f47a6fcc06b8820f7348515379",
    "dbae2d0204aa489e234eb2f903a0127b17c712386428cab12b86c5f68aa75867",
    "0b2df0f635584f42c895f1d7b9cd105d3106accd9804d30556da88ae1bb0d62c",
    "d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86"
]
for hash_value in hashes_predefinidos:
    arbol.insertar(hash_value)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Verificador de URL")

# Etiqueta y campo de entrada para la URL
tk.Label(root, text="Ingrese la URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Botón para verificar la URL
verify_button = tk.Button(root, text="Verificar URL", command=verificar_url)
verify_button.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
