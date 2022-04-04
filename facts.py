
class Facts(object):
    def __init__(self):
        self._list_facts = {}

    # Getter
    def get_list_facts(self):
        return self._list_facts

    def clear_list_facts(self):
        self._list_facts.clear()


    def add_values_to_facts(self,name_cell,value):
        self.get_list_facts()[name_cell] = value



