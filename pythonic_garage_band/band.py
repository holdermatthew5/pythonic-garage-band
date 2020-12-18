class Band:

    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = [self.members[0].play_solo(), self.members[1].play_solo(), self.members[2].play_solo()]
        return solos
    
    def to_list():
        return Band.instances

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

class Musician:
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    
    def play_solo(self):
        return self.solo
    
    def get_instrument(self):
        return self.instrument

class Guitarist(Musician):
    
    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"
        self.solo = "face melting guitar solo"
        
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

class Bassist(Musician):
    
    def __init__(self, name):
        self.name = name
        self.instrument = "bass"
        self.solo = "bom bom buh bom"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

class Drummer(Musician):
    
    def __init__(self, name):
        self.name = name
        self.instrument = "drums"
        self.solo = "rattle boom crash"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"