import random
import numpy as np
from cell import *


class Environment(object):

    # Constructor
    def __init__(self, level=1):
        self._level = level
        self._env = []
        self._matrice_size = 2 + level

    # Getter
    def get_level(self):
        return self._level

    def get_env(self):
        return self._env

    def get_matrice_size(self):
        return self._matrice_size

    # Done
    def create_env(self):
        # Creation of a list of Cells
        for x in range(0, 2 + self.get_level()):
            for y in range(0, 2 + self.get_level()):
                self.get_env().append(Cell(x, y))
        # Add neighbours of each Cell
        self.find_neighbours_of_cell(self.get_env())
        # Set random Fire,Rubble and one people  on the environment
        # The Agent always start at position (0,0) on the env
        self.add_random_elements_on_env()

    # Done
    def add_random_elements_on_env(self):
        nb_elem_on_env = 0
        list_cells_free = [i for i in range(len(self.get_env()))]
        random_cell = random.randint(1, len(self.get_env()) - 1)
        #Set the victim on the environment
        self.get_env()[random_cell].set_etat("V",True)
        list_cells_free.remove(random_cell)
        while nb_elem_on_env < 3 + self.get_level():
            # choose an element of the list (not (0,0))
            random_cell = random.choice(list_cells_free)
            chance = random.randint(0, 1)
            if chance == 0:
                # Rubble
                self.get_env()[random_cell].set_etat("D",True)
                for elem in range(len(self.get_env()[random_cell].get_listneighbours())):
                    self.get_env()[random_cell].get_listneighbours()[elem].add_values_to_etat(self.get_env()[random_cell],"P")
                nb_elem_on_env += 1
                list_cells_free.remove(random_cell)
            else:
                # Fire
                self.get_env()[random_cell].set_etat("F",True)
                for elem in range(len(self.get_env()[random_cell].get_listneighbours())):
                    self.get_env()[random_cell].get_listneighbours()[elem].add_values_to_etat(self.get_env()[random_cell],"C")
                nb_elem_on_env += 1
                list_cells_free.remove(random_cell)


    # Done
    def find_neighbours_of_cell(self, env):
        for cell in range(0, len(env)):
            x = env[cell].get_x()
            y = env[cell].get_y()
            for index, neighbours in enumerate(env):
                if 0 <= x - 1 == neighbours.get_x() and neighbours.get_y() == y:
                    env[cell].add_neighbour(env[index])
                if self.get_matrice_size() > x + 1 == neighbours.get_x() and neighbours.get_y() == y:
                    env[cell].add_neighbour(env[index])
                if 0 <= y - 1 == neighbours.get_y() and neighbours.get_x() == x:
                    env[cell].add_neighbour(env[index])
                if self.get_matrice_size() > y + 1 == neighbours.get_y() and neighbours.get_x() == x:
                    env[cell].add_neighbour(env[index])

    # Done
    def show_env(self):
        list_etat_for_all_cells = []
        for elem in range(0, len(self.get_env())):
            list_etat = []
            for x, y in self.get_env()[elem].get_etat().items():
                if y == True:
                    list_etat.append(x)
                if y == "P":
                    list_etat.append("P")
                if y == "C":
                    list_etat.append("C")
            list_etat_for_all_cells.append(list_etat)


        Matrix_final = []
        for elem in range(0, len(list_etat_for_all_cells), self.get_matrice_size()):
            Matrix_final.append(list_etat_for_all_cells[elem:elem + self.get_matrice_size()])

        s = [[str(e) for e in row] for row in Matrix_final]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]

        #Affichage
        if(self.get_level()  ==1):
            print('\n'"TP3 AGENT LOGIQUE - Simulateur d'un robot qui sauve des vies")
        print(f"Tableau niveau {self.get_level()}")
        print("A - Agent, F - Feu, D - Décombres, P - Poussière, C - Chaleur, V - Victime")
        print('\n'.join(table))






if __name__ == '__main__':
    env = Environment(2)
    env.create_env()
    env.show_env()
