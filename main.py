import tkinter as tk
from clase1 import clase1

def ventana(dimensiones):
    window = tk.Tk()
    window.geometry(dimensiones)
    window.mainloop()

def main():
    ventana("400x300")

main()