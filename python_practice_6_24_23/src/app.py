from soldier import Soldier

def main():
    soldier1 = Soldier("Gabriel J.", 1234, 1301998, {"captain" : 5})
    soldier2 = Soldier("Omid", 23455, 23003, {"private" : 1})

    soldier1.seniority(soldier2)
    #soldier1_rank_value = list(soldier1.m_rank.values())[0]
    #print(type(soldier1_rank_value))

if __name__ == "__main__":
    main()