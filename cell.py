class Cell(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._etat = {"D" : False,"F" : False, "V" : False}
        self._listneighbours = []

    # Getter
    def get_etat(self):
        return self._etat

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_listneighbours(self):
        return self._listneighbours

    # Setter
    def set_etat(self, key, value):
        self.get_etat()[key] = value

    # Add values

    def add_values_to_etat(self,name_cell,value):
        self.get_etat()[name_cell] = value

    def add_neighbour(self, cell):
        self._listneighbours.append(cell)

