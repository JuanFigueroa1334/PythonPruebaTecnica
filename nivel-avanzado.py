import tkinter as tk
from tkinter import messagebox
import sqlite3
import requests


def crear_bd():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)", ("admin", "1234"))
    conn.commit()
    conn.close()

def validar_usuario(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def llamadoapi_rickandmorty():
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        personajes = [personaje['name'] for personaje in data['results']]
        return personajes
    else:
        return "Error"
def listado_rickandmorty():
    personajes = llamadoapi_rickandmorty()
    vista_result = tk.Toplevel()
    vista_result.title("Personajes")
    vista_result.geometry("390x550")

    lista = tk.Listbox(vista_result)
    for personaje in personajes:
        lista.insert(tk.END, personaje)
    lista.pack(expand=True, fill=tk.BOTH)

def login():
    usuario = entrada_usuario.get()
    clave = entrada_clave.get()
    if validar_usuario(usuario, clave):
        messagebox.showinfo("Exitoso", "Ingreso")
        listado_rickandmorty()
    else:
        messagebox.showerror("Error", "Datos incorrectos")
crear_bd()
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("650x380")
tk.Label(ventana, text="Usuario:").pack(pady=5)
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()
tk.Label(ventana, text="Clave:").pack(pady=5)
entrada_clave = tk.Entry(ventana, show="*")
entrada_clave.pack()
tk.Button(ventana, text="Login", command=login).pack(pady=20)

ventana.mainloop()
