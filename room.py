from item import Item

class Room:
    def __init__(self, name, description):
        self.name=name
        self.description=description
        self.n_to='null'
        self.s_to='null'
        self.e_to='null'
        self.w_to='null'
        self.inventory=[];