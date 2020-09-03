class Player: 
    def __init__(self,name,current_room,inventory):
        self.name= name 
        self.current_room=current_room
        self.inventory=inventory;
        #this class is connected to room and item without being dependent

