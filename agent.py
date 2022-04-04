

from activator import *
from sensor import *
from facts import *
from rules import *


class Agent(object):

    def __init__(self, position):
        # Current cell
        self._position = position
        self._activator = Activator(self)
        self._sensor = Sensor(self)
        self._facts = Facts()
        self._rules = Rules(self)
        self._victim_saved = False
        self._isAlive = True

    # Getter
    def get_sensor(self):
        return self._sensor

    def get_facts(self):
        return self._facts

    def get_position(self):
        return self._position

    def get_activator(self):
        return self._activator

    def get_victim_saved(self):
        return self._victim_saved

    def get_isALive(self):
        return self._isAlive

    # Setter

    def set_isAlive(self,value):
        self._isAlive = False

    def set_position(self, cell):
        self._position = cell

    def set_victim_saved(self, value):
        self._victim_saved = value

    def moteur_inference(self):
        print("Moteur_inference")
        self.Filtrage()
        self.Choix_regle()
        self.Appliquer_regle()

    # Done
    def Filtrage(self):
        list_facts = self.get_facts().get_list_facts()
        poids_min = []
        # On filtre afin de récupérer la cellule voisine avec le poids le plus faible
        print(list_facts)
        for keys, items in list_facts.items():
            for elem in range(0,len(items)):
                poids_min.append(items[elem])
        for keys, items in list_facts.items():
            if min(items) == min(poids_min):
                min_key = keys
                break
        next_cell = (min(poids_min),min_key)
        return next_cell

    def Choix_regle(self, next_cell):
        # On choisi d'executer la règle qui correspond au poids minimum
        # Victime
        cell_weight = next_cell[0]
        cell = next_cell[1]
        print(cell_weight)
        print(cell)

        # -1 correspond à la victime
        if cell_weight == -1:
            if cell[0] == "up":
                self.get_activator().up()
                print("Le robot monte")
            elif cell[0] == "down":
                self.get_activator().down()
                print("Le robot descend")
            elif cell[0] == "right":
                self.get_activator().right()
                print("Le robot va à droite")
            elif cell[0] == "left":
                self.get_activator().left()
                print("Le robot va à gauche")
            self.get_activator().help()
            print("Le robot vient de sauver la victime")
            self.set_victim_saved(True)

        # 0 correspond aux hurlements
        if cell_weight == 0:
            if cell[0] == "up":
                self.get_activator().up()
                print("Le robot monte car il a entendu des hurlements de la victime")
            elif cell[0] == "down":
                self.get_activator().down()
                print("Le robot descend car il a entendu des hurlements de la victime")
            elif cell[0] == "right":
                self.get_activator().right()
                print("Le robot va à droite car il a entendu des hurlements de la victime")
            elif cell[0] == "left":
                self.get_activator().left()
                print("Le robot va à gauche car il a entendu des hurlements de la victime")

        # 1 correspond à une case vide
        if cell_weight == 1:
            if cell[0] == "up":
                self.get_activator().up()
                print("Le robot monte")
            elif cell[0] == "down":
                self.get_activator().down()
                print("Le robot descend")
            elif cell[0] == "right":
                self.get_activator().right()
                print("Le robot va à droite")
            elif cell[0] == "left":
                self.get_activator().left()
                print("Le robot va à gauche")

        # 1 correspond à une case chaleur
        if cell_weight == 2:
            if cell[0] == "up":
                self.get_activator().up()
                print("Le robot monte")
            elif cell[0] == "down":
                self.get_activator().down()
                print("Le robot descend")
            elif cell[0] == "right":
                self.get_activator().right()
                print("Le robot va à droite")
            elif cell[0] == "left":
                self.get_activator().left()
                print("Le robot va à gauche")

        # 3 correspond à une case poussière
        if cell_weight == 3:
            if cell[0] == "up":
                self.get_activator().up()
                print("Le robot monte")
            elif cell[0] == "down":
                self.get_activator().down()
                print("Le robot descend")
            elif cell[0] == "right":
                self.get_activator().right()
                print("Le robot va à droite")
            elif cell[0] == "left":
                self.get_activator().left()
                print("Le robot va à gauche")

        # 4 correspond à une case incendie
        if cell_weight == 4:
            self.get_activator().extinguisher()
            print("Le robot vient d'éteindre un incendie")
            if cell[0] == "up":
                self.get_activator().up()
                print("Le robot monte ")
            elif cell[0] == "down":
                self.get_activator().down()
                print("Le robot descend")
            elif cell[0] == "right":
                self.get_activator().right()
                print("Le robot va à droite")
            elif cell[0] == "left":
                self.get_activator().left()
                print("Le robot va à gauche")

        # 5 correspond à une case débris
        if cell_weight == 5:
            if cell[0] == "up":
                self.get_activator().up()
                print("Le robot monte ")
            elif cell[0] == "down":
                self.get_activator().down()
                print("Le robot descend")
            elif cell[0] == "right":
                self.get_activator().right()
                print("Le robot va à droite")
            elif cell[0] == "left":
                self.get_activator().left()
                print("Le robot va à gauche")
            print("le robot est mort")
            self.set_isAlive(False)


"""
    def Appliquer_regle(self):
        print("Appliquer_regle")
"""