from tkinter import *
from ListaSimple import ListaSimple
from tkinter import filedialog
import xml.etree.ElementTree as ET
from matriz import matriz
import subprocess

window = Tk()
ls = ListaSimple()
listbox = Listbox(window)
ma = matriz()

def operacones_lista():
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.push(4)
    ls.push(5)
    #ls.print()

def ayuda_convertir_lista(arreglo):
    aux = []
    for i in arreglo:
        aux.append(i.strip())
        contador = 0
        for i in aux:
            if i == '':
                aux.pop(contador)
            contador = contador + 1

    principal = []

    for i in aux:
        principal.append(list(i))

    #print(principal)
    return principal

def archivo_xml():
    file_path = filedialog.askopenfilename(title = "Abrir")
    xml_doc = ET.parse(file_path)
    raiz = xml_doc.getroot()
    for padre in raiz:
        for hijo in padre:
            if hijo.tag == "nombre":
                print("Nombre: " + hijo.text)
            elif hijo.tag == "filas":
                print("Filas: " + hijo.text)
            elif hijo.tag == "columnas":
                print("Columnas: " + hijo.text)
            elif hijo.tag == "imagen":
                print("Imagen:")
                arreglo = hijo.text.split('\n')
                #split // strip
                arreglo_aux = []
                arreglo_aux = ayuda_convertir_lista(arreglo)
                m = 0
                for i in arreglo_aux:
                    n = 0
                    for j in i:
                        if j == '*':
                            ma.insertar(n, m, j)
                        n = n + 1
                    m = m + 1
                #print(arreglo_aux)
                ma.recorrer()

def datos_estudiante():
        print("Kevyn Josué Girón Jiménez")
        print("201700653")
        print("Introduccion a la Programacion y Computacion 2 seccion 'A' ")
        print("Ingenieria en Ciencias y Sistemas")
        print("4to Semestre")
        
    
def objeto_listbox():
    if len(listbox.curselection()) != 0:
        print(listbox.get(listbox.curselection()[0]))
        ls.search(listbox.get(listbox.curselection()[0]))

def insert_listbox():
    for a in ls.save_in_list():
        listbox.insert(END, a)
   

def ventana(titulo):
    
    window.title(titulo)
    window.resizable(0,0) #Bloquear que la ventana no pueda cambiar de tamaño
    #botones
    #-------Boton 1
    btn = Button(window, text = "Cargar archivos", width = 25, command = archivo_xml)
    btn.grid(column = 0, row = 0, padx = 5, pady = 5)
    #-------Boton 2
    btn2 = Button(window, text = "Operaciones", width = 25, command = objeto_listbox)
    btn2.grid(column = 1, row = 0, padx = 5, pady = 5)
    #-------Boton 3
    btn3 = Button(window, text = "Reportes", width = 25, command = insert_listbox)
    btn3.grid(column = 2, row = 0, padx = 5, pady = 5)
    #-------Boton 3
    btn4 = Button(window, text = "Ayuda", width = 25, command = datos_estudiante)
    btn4.grid(column = 3, row = 0, padx = 5, pady = 5)
    #Listbox - Scrollbar
    
    """
    for line in range(1, 101):
        listbox.insert(END, "Number " + str(line)) """
    listbox.grid(column = 0, row = 1, padx = 5, pady = 5)

    #labels
    #------label 1
    #lbl1 = Label(window, textvariable = var, width = 10)
    #lbl1.grid(column = 0, row = 3, padx = 5, pady = 5)
    #------label 2
    #lbl2 = Label(window, text = "", width = 10)
    #lbl2.grid(column = 2, row = 0, padx = 5, pady = 5)
    #---------------------------------------------------------------------------------------------------------
    window.mainloop()

def main():
    ventana("Menu Principal")

#operacones_lista()
main()
#archivo_xml()
