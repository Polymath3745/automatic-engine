# Parent class
class Soldier:
    def __init__(self, name, id, birthday, rank):
        self.m_name = name
        self.m_id = id
        self.m_birthday = birthday
        self.m_rank = rank

    def get_name(self):
        return self.m_name
    
    def get_id(self):
        return self.m_id
    
    def get_birthday(self):
        return self.m_birthday
    
    def get_rank(self):
        return self.m_rank
    
