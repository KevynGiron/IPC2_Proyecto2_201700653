from NodoMatriz import NodoMatriz, NodoEncabezado
from encabezado import listaEncabezado

class matriz:
    
    def __init__(self):
        self.efilas = listaEncabezado()
        self.ecolumnas = listaEncabezado()

    def insertar(self, fila, columna, valor):
        nuevo = NodoMatriz(fila, columna, valor)

        #insesion filas
        eFila = self.efilas.getEncabezado(fila)
        if eFila == None:
            eFila = NodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.efilas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while(actual.derecha != None):
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha

                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual

        #insersion columnas
        eColumna = self.ecolumnas.getEncabezado(columna)
        if eColumna == None:
            eColumna = NodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.ecolumnas.setEncabezado(eColumna)
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo

                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba =actual

    def recorrer(self):
        eFila = self.efilas.primero
        while eFila != None:
            actual = eFila.accesoNodo
            print("\nFila " + str(actual.fila))
            print("Columna | Valor: ")
            while actual != None:
                print(str(actual.columna) + "       | " + str(actual.valor))
                actual = actual.derecha
            eFila = eFila.siguiente

    def graficar(self, m, n):
        relleno = '<TD BGCOLOR = "#000000">   </TD>'
        blanco = '<TD>   </TD>'
        code = ''
        eFila = self.efilas.primero
        for a in range(0, m):
            #code = code + '<TR>'
            actual = eFila.accesoNodo
            for b in range(0, n):
