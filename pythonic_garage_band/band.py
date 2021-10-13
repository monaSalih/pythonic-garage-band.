from abc import abstractclassmethod
class Musician:
    members = []
    def __init__(self, name):
        self.name = name
        Musician.members.append(self)
    @abstractclassmethod
    def __str__(self):
        pass
    @abstractclassmethod
    def __repr__(self):
        pass
    @abstractclassmethod
    def get_instrument(self):
        pass
    @abstractclassmethod
    def play_solo(self):
        pass

class Band:
    def __init__(self,name,members,inst=''):
        self.name=name
        self.members=members
    def play_solo(self):
        return self.inst

class Guitarist(Band):
    def __init__(self,name,inst=''):
        self.name=name
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def get_instrument(self):
        return "guitar"

class Drummer(Band):
    def __init__(self,name,inst='rattle boom crash'):
        self.name=name
    def __str__(self):
       return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        return "drums"


class Bassist(Band):
    def __init__(self,name,inst='bom bom buh bom'):
        self.name=name
    def __str__(self):
       return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        return "bass"

        
        


    
    