class Student:
    # this is like a constructor
    def __init__(self, name, major, gpa, is_on_probation):
        self.m_name = name
        self.m_major = major
        self.m_gpa = gpa
        self.m_is_on_probation = is_on_probation

    def disp_name(self):
        print(self.m_name)

    def on_honor_roll(self):
        if (self.m_gpa >= 3.5):
            return True
        else:
            return False
