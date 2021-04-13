from NodoSimple import Nodo

class ListaSimple():

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def push(self, dato):
        if self.is_empty():
            self.head = self.tail = Nodo(dato)
        else:
            aux = self.tail
            self.tail = aux.next = Nodo(dato)

    def search(self, dato):
        aux = self.head
        while (aux != None):
            if (aux.data == dato):
                print("Dato encontrado: " + str(aux.data))
                break
            aux = aux.next

    def save_in_list(self):
        lista = []
        aux = self.head
        while (aux != None):
            lista.append(aux.data)
            aux = aux.next
        return lista

    def print(self):
        aux = self.head
        while (aux != None):
            print(aux.data)
            aux = aux.next
    