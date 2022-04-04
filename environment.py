import random

from agent import *


class Environment(object):

    # Constructor
    def __init__(self, level=1):
        self._level = level
        self._env = []
        self._matrice_size = 2 + level
        self._agent = None

    # Getter
    def get_level(self):
        return self._level

    def get_env(self):
        return self._env

    def get_agent(self):
        return self._agent

    def get_matrice_size(self):
        return self._matrice_size

    # Setter
    def set_level(self,lvl):
        self._level = lvl
    # Done
    def create_env(self,lvl):
        self.set_level(lvl)
        lvl += 1
        # Creation of a list of Cells
        for x in range(0, 2 + self.get_level()):
            for y in range(0, 2 + self.get_level()):
                self.get_env().append(Cell(x, y))
        # Add neighbours of each Cell
        self.find_neighbours_of_cell(self.get_env())
        # The Agent always start at position (0,0) on the env
        # Set random Fire,Rubble and one people  on the environment
        self.add_random_elements_on_env()

        self.show_env()
        while self.get_agent().get_victim_saved() == False :
            self.get_agent().get_sensor().UseAllSensor()
            next_cell = self.get_agent().Filtrage()
            self.get_agent().Choix_regle(next_cell)
            self.get_agent().get_facts().clear_list_facts()



    # Done
    def add_random_elements_on_env(self):
        nb_elem_on_env = 0
        list_cells_free = [i for i in range(1, len(self.get_env()))]
        random_cell = random.randint(1, len(self.get_env()) - 1)
        # Set the agent on the environment
        self._agent = Agent(self.get_env()[0])
        self.get_env()[0].set_etat("A", True)
        # Set the victim on the environment
        self.get_env()[random_cell].set_etat("V", True)
        self.get_env()[random_cell].set_weight(-1)
        for elem in range(len(self.get_env()[random_cell].get_listneighbours())):
            self.get_env()[random_cell].get_listneighbours()[elem][1].add_values_to_etat(self.get_env()[random_cell], "H")
            self.get_env()[random_cell].get_listneighbours()[elem][1].set_weight(0)
        list_cells_free.remove(random_cell)
        while nb_elem_on_env < 3 + self.get_level():
            # choose an element of the list (not (0,0))
            random_cell = random.choice(list_cells_free)
            chance = random.randint(0, 1)
            if chance == 0:
                # Rubble
                self.get_env()[random_cell].set_etat("D", True)
                self.get_env()[random_cell].set_weight(5)
                for elem in range(len(self.get_env()[random_cell].get_listneighbours())):
                    self.get_env()[random_cell].get_listneighbours()[elem][1].add_values_to_etat(
                        self.get_env()[random_cell], "P")
                    self.get_env()[random_cell].get_listneighbours()[elem][1].set_weight(3)
                nb_elem_on_env += 1
                list_cells_free.remove(random_cell)
            else:
                # Fire
                self.get_env()[random_cell].set_etat("F", True)
                self.get_env()[random_cell].set_weight(4)
                for elem in range(len(self.get_env()[random_cell].get_listneighbours())):
                    self.get_env()[random_cell].get_listneighbours()[elem][1].add_values_to_etat(
                        self.get_env()[random_cell], "C")
                    self.get_env()[random_cell].get_listneighbours()[elem][1].set_weight(2)
                nb_elem_on_env += 1
                list_cells_free.remove(random_cell)

        for elem in range(1,len(self.get_env())):
            if len(self.get_env()[elem].get_weight()) == 0:
                self.get_env()[elem].set_weight(1)




    # Done
    def find_neighbours_of_cell(self, env):
        for cell in range(0, len(env)):
            x = env[cell].get_x()
            y = env[cell].get_y()
            for index, neighbours in enumerate(env):
                #down
                if 0 <= x - 1 == neighbours.get_x() and neighbours.get_y() == y:
                    env[cell].add_neighbour(("up",env[index]))
                #up
                if self.get_matrice_size() > x + 1 == neighbours.get_x() and neighbours.get_y() == y:
                    env[cell].add_neighbour(("down",env[index]))
                #left
                if 0 <= y - 1 == neighbours.get_y() and neighbours.get_x() == x:
                    env[cell].add_neighbour(("left",env[index]))
                #right
                if self.get_matrice_size() > y + 1 == neighbours.get_y() and neighbours.get_x() == x:
                    env[cell].add_neighbour(("right",env[index]))

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
                if y == "H":
                    list_etat.append("H")
            list_etat_for_all_cells.append(list_etat)

        Matrix_final = []
        for elem in range(0, len(list_etat_for_all_cells), self.get_matrice_size()):
            Matrix_final.append(list_etat_for_all_cells[elem:elem + self.get_matrice_size()])

        s = [[str(e) for e in row] for row in Matrix_final]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]

        # Affichage
        if (self.get_level() == 1):
            print('\n'"TP3 AGENT LOGIQUE - Simulateur d'un robot qui sauve des vies")
        print(f"Tableau niveau {self.get_level()}")
        print("A - Agent, F - Feu, D - Décombres, P - Poussière, C - Chaleur, V - Victime")
        print('\n'.join(table))


if __name__ == '__main__':
    env = Environment()
    env.create_env(1)
