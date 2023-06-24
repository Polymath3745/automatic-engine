# Parent class
class Soldier:
    def __init__(self, name, id, birthday, rank):
        self.m_name = name
        self.m_id = id
        self.m_birthday = birthday
        self.m_rank = rank

    
    # getters
    def get_name(self):
        return self.m_name
    
    def get_id(self):
        return self.m_id
    
    def get_birthday(self):
        return self.m_birthday
    
    def get_rank(self):
        return self.m_rank
    

    # setters
    def set_name(self, name):
        self.m_name = name

    def set_id(self, id):
        self.m_id = id

    def set_birthday(self, birthday):
        self.m_birthday = birthday

    def set_rank(self, rank):
        self.m_rank = rank

    def seniority(self, other_soldier):
        if(self.m_rank.keys() < other_soldier.m_rank.keys()):
            print(self.m_name + " is a higher rank than " + other_soldier.m_name)

        else:
            print(self.m_name + " is a higher rank than " + other_soldier.m_name)
