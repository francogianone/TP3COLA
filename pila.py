class pila():
    
    def __init__(self):  
        self.elements = []
    def __eq__(self, stack_aux):
        if isinstance(stack_aux, pila):
            return self.__elements == stack_aux.__elements
        else:
            return False
    def push(self, dato):
        self.elements.append(dato)
    def pop(self):
        if self.size() > 0:
            dato = self.elements.pop()
            return dato  
    def size(self):
        return len(self.elements)
    def on_top(self):
        if self.size() > 0:
            return self.elements[-1]

