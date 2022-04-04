class Cell(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._etat = {"A" : False,"D" : False,"F" : False, "V" : False}
        self._listneighbours = []
        # V : -1 / H : 0 / case vide : 1 / C : 2 / P : 3 / F : 4 / D : 5
        self._weight = []

    # Getter
    def get_etat(self):
        return self._etat

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_listneighbours(self):
        return self._listneighbours

    def get_weight(self):
        return self._weight

    # Setter
    def set_etat(self, key, value):
        self.get_etat()[key] = value

    def set_weight(self,value):
        self._weight.append(value)

    # Add values

    def add_values_to_etat(self,name_cell,value):
        self.get_etat()[name_cell] = value

    def add_neighbour(self, cell):
        self._listneighbours.append(cell)

