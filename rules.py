from cell import *
from activator import *

class Rules(object):
    def __init__(self,agent):
        self._agent = agent

    # Getter
    def get_agent(self):
        return self._agent


    def rules(self,param):
        
        if(param == "-1"):
            self.get_agent().get_activator().extinguisher()
            print("Le robot a éteint le feu")

        if(param == "V"):
            self.get_agent().get_activator().help()
            print("Le robot vient de sauver la victime")
            
        if(param == "H"):
            # avancer avant sur la case
            self.get_agent().get_activator().help()
        













