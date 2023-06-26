from soldier import Soldier

def main():
    soldier1 = Soldier("Gabriel J.", 1234, 1301998, "captain", 5)
    soldier2 = Soldier("Omid", 23455, 23003, "private", 1)

    soldier1.seniority(soldier2)

if __name__ == "__main__":
    main()