from abc import abstractclassmethod
class Musician:
    members = []

    def init(self, name):

        self.name = name
        Musician.members.append(self)

    @abstractclassmethod
    def str(self):
        pass

    @abstractclassmethod
    def repr(self):
        pass

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass

class Band:
    def init(self,name,members,inst=''):
        self.name=name
        self.members=members
    def play_solo(self):
        return self.inst

class Guitarist(Band):
    def init(self,name,inst=''):
        self.name=name
    def str(self):
        return f"My name is {self.name} and I play guitar"
    def repr(self):
        return f"Guitarist instance. Name = {self.name}"
    def get_instrument(self):
        return "guitar"

class Drummer(Band):
    def init(self,name,inst='rattle boom crash'):
        self.name=name
    def str(self):
       return f"My name is {self.name} and I play drums"
    def repr(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        return "drums"


class Bassist(Band):
    def init(self,name,inst='bom bom buh bom'):
        self.name=name
    def str(self):
       return f"My name is {self.name} and I play bass"
    def repr(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        return "bass"