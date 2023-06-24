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

    # This function takes in the rank of the calling soldier and the comparison one
    # it then uses the values dict function to grab the rank value
    # passes this to the list function which then grabs it as a integer and compares
    # to the rank value of the other soldier

    def seniority(self, other_soldier):
        if(list(self.m_rank.values())[0] > list(other_soldier.m_rank.values())[0]):
            print(self.m_name + " is a higher rank than " + other_soldier.m_name)
            print(self.m_name + " is a " + list(self.m_rank.keys())[0])
            print(other_soldier.m_name + " is a " + list(other_soldier.m_rank.keys())[0])

        else:
            print(other_soldier.m_name + " is a higher rank than " + self.m_name)
