from soldier import Soldier

class NavySeal(Soldier):
    def __init__(self, name, id, birthday, rank, rank_value, specialization):
        super().__init__(name, id, birthday, rank, rank_value)
        self.m_specialization = specialization

    def war_cry():
        print("The Only Easy Day Was Yesterday!")

    def get_specialization(self):
        return self.m_specialization
    
    def set_specialization(self, specialization):
        self.m_specialization = specialization
