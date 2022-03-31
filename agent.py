
class Agent(object):

    def __init__(self,x,y,name="A"):
        self._name = name
        self._x = x
        self._y = y


    def moteur_inference(self):
        print("Moteur_inference")
        self.Filtrage()
        self.Choix_regle()
        self.Appliquer_regle()

    def Filtrage(self):
        print("Filtrage")

    def Choix_regle(self):
        print("Choix_regle")

    def Appliquer_regle(self):
        print("Appliquer_regle")

