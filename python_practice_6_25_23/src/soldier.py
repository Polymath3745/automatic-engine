class Soldier:
    def __init__(self, name, id, birthday, rank, rank_value):
        self.m_name = name
        self.m_id = id
        self.m_birthday = birthday
        self.m_rank = rank
        self.m_rank_value = rank_value

    def get_name(self):
        return self.m_name
    
    def get_id(self):
        return self.m_id
    
    def get_birthday(self):
        return self.m_birthday
    
    def get_rank(self):
        return self.m_rank
    
    def set_name(self, name):
        self.m_name = name

    def set_id(self, id):
        self.m_id = id

    def set_birthday(self, birthday):
        self.m_birthday = birthday

    def set_rank(self, rank):
        self.m_rank = rank

    def seniority(self, other_soldier):
        if self.m_rank_value > other_soldier.m_rank_value:
            print(self.m_name + " is a higher rank than " + other_soldier.m_name)
            print(self.m_name + " is a " + self.m_rank)
            print(other_soldier.m_name + " is a " + other_soldier.m_rank)
        else:
            print(other_soldier.m_name + " is a higher rank than " + self.m_name)
