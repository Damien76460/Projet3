from agent import *
from cell import *


class Sensor(object):
    def __init__(self, agent):
        self._agent = agent
        self._list_result_Sensor = []


    # Getter
    def get_agent(self):
        return self._agent

    def get_list_result_Sensor(self):
        return self._list_result_Sensor


    # Done
    def SensorHeat(self,current_cell):
        list_weight = current_cell[1].get_weight()
        for weight in range(0,len(list_weight)):
            if(list_weight[weight] == 1):
                self.get_list_result_Sensor().append(1)
            if(list_weight[weight] == 2):
                self.get_list_result_Sensor().append(2)
            if(list_weight[weight] == 4):
                self.get_list_result_Sensor().append(4)

    # Done
    def SensorDust(self,current_cell):
        list_weight = current_cell[1].get_weight()
        for weight in range(0,len(list_weight)):
            if(list_weight[weight] == 3):
                self.get_list_result_Sensor().append(3)
            if(list_weight[weight] == 5):
                self.get_list_result_Sensor().append(5)
    # Done
    def SensorCry(self,current_cell):
        list_weight = current_cell[1].get_weight()
        for weight in range(0,len(list_weight)):
            if(list_weight[weight] == 0):
                self.get_list_result_Sensor().append(0)
            if(list_weight[weight] == -1):
                self.get_list_result_Sensor().append(-1)

    # Done
    def UseAllSensor(self):
        current_cell = self.get_agent().get_position()
        print(current_cell)
        # Use all sensors to collect informations about the environment
        for elem in range(0, len(current_cell.get_listneighbours())):
            self.SensorHeat(current_cell.get_listneighbours()[elem])
            self.SensorDust(current_cell.get_listneighbours()[elem])
            self.SensorCry(current_cell.get_listneighbours()[elem])
            self.get_agent().get_facts().add_values_to_facts(current_cell.get_listneighbours()[elem],self.get_list_result_Sensor())
            self._list_result_Sensor = []


