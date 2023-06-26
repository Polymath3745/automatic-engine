from soldier import Soldier

class AirforcePilot(Soldier):
    def __init__(self, name, id, birthday, rank, rank_value, aircraft):
        super().__init__(name, id, birthday, rank, rank_value)
        self.m_aircraft = aircraft

    def war_cry(self):
        print("Aim High ... Fly-Fight-Win!")

    def get_aircraft(self):
        return self.m_aircraft
    
    def set_aircraft(self, aircraft):
        self.m_aircraft = aircraft