class info_matrices:

    def __init__(self, nombre, fila, columna, imagen):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.imagen = imagen

    def get_nombre(self):
        return self.nombre

    def get_fila(self):
        return self.fila

    def get_columna(self):
        return self.columna

    def get_imagen(self):
        return self.imagen

    def set_nombre(self, dato):
        self.nombre = dato

    def set_fila(self, dato):
        self.fila = dato
    
    def set_columna(self, dato):
        self.columna = dato

    def set_imagen(self, dato):
        self.imagen = dato