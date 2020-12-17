class Band:

    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def play_solos(self, member):
        return member.play_solo
    
    def to_list(self):
        return self.instances

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

class Musician:
    pass

class Guitarist:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

class Bassist:
    pass

class Drummer:
    pass