
class character():
    """set's up each of the characters"""
    def __init__(self, name, title, health, kits):
        self.name = name
        self.title = title
        self.health = health
        self.kits = kits
        

    def getname(self):
        return self.name
    def gethealth(self):
        return self.health
    def getability(self):
        return self.kits

    def change_health(self, new_health):
        self.health = self.health + new_health

    def change_kits(self, new_kits):
        self.kits = self.kits + new_kits



        
    #return super().__init__(*args, **kwargs)