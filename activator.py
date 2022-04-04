from agent import *
from cell import *


class Activator(object):
    def __init__(self, agent):
        self._agent = agent

    # Getter
    def get_agent(self):
        return self._agent

    # Done
    def up(self):
        current_cell = self.get_agent().get_position()
        for elem in range(0, len(current_cell.get_listneighbours())):
            if current_cell.get_listneighbours()[elem][1].get_x() == current_cell.get_x() - 1 and \
                    current_cell.get_listneighbours()[elem][1].get_y() == current_cell.get_y():
                current_cell.set_etat("A", False)
                self.get_agent().set_position(current_cell.get_listneighbours()[elem][1])
                current_cell.get_listneighbours()[elem][1].set_etat("A", True)
                break
            else:
                continue

    # Done
    def down(self):
        current_cell = self.get_agent().get_position()
        for elem in range(0, len(current_cell.get_listneighbours())):
            if current_cell.get_listneighbours()[elem][1].get_x() == current_cell.get_x() + 1 and \
                    current_cell.get_listneighbours()[elem][1].get_y() == current_cell.get_y():
                current_cell.set_etat("A", False)
                self.get_agent().set_position(current_cell.get_listneighbours()[elem][1])
                current_cell.get_listneighbours()[elem][1].set_etat("A", True)
                break
            else:
                continue

    # Done
    def left(self):
        current_cell = self.get_agent().get_position()
        for elem in range(0, len(current_cell.get_listneighbours())):
            if current_cell.get_listneighbours()[elem][1].get_y() == current_cell.get_y() - 1 and \
                    current_cell.get_listneighbours()[elem][1].get_x() == current_cell.get_x():
                current_cell.set_etat("A", False)
                self.get_agent().set_position(current_cell.get_listneighbours()[elem][1])
                current_cell.get_listneighbours()[elem][1].set_etat("A", True)
                break
            else:
                continue

    # Done
    def right(self):
        current_cell = self.get_agent().get_position()
        for elem in range(0, len(current_cell.get_listneighbours())):
            if current_cell.get_listneighbours()[elem][1].get_y() == current_cell.get_y() + 1 and \
                    current_cell.get_listneighbours()[elem][1].get_x() == current_cell.get_x():
                current_cell.set_etat("A", False)
                self.get_agent().set_position(current_cell.get_listneighbours()[elem][1])
                current_cell.get_listneighbours()[elem][1].set_etat("A", True)
                break
            else:
                continue

    # Done
    def extinguisher(self):
        current_cell = self.get_agent().get_position()
        for elem in range(0, len(current_cell.get_listneighbours())):
            if current_cell.get_listneighbours()[elem][1].get_etat()["F"]:
                current_cell.get_listneighbours()[elem][1].set_etat("F", False)
                for neighbours in range(0, len(current_cell.get_listneighbours()[elem][1].get_listneighbours())):
                    current_cell.get_listneighbours()[elem][1].get_listneighbours()[neighbours][1].set_etat(
                        current_cell.get_listneighbours()[elem], False)
                break
            else:
                continue

    # Done
    def help(self):
        current_cell = self.get_agent().get_position()
        for elem in range(0, len(current_cell.get_listneighbours())):
            if current_cell.get_listneighbours()[elem][1].get_etat()["V"]:
                current_cell.get_listneighbours()[elem][1].set_etat("V", False)
                self.get_agent().set_victim_saved(True)
                break
            else:
                continue

            

