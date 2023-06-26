from soldier import Soldier
from navySeal import NavySeal
from airforcePilot import AirforcePilot

def main():
    soldier1 = Soldier("Gabriel J.", 1234, 1301998, "captain", 5)
    soldier2 = Soldier("Omid", 23455, 23003, "private", 1)

    navy_seal = NavySeal("Gabriel", 1234, "01301998", "Captain", 6, "Gunner")
    navy_seal.war_cry()

    airforce_pilot = AirforcePilot("Omid", 123345, "023003", "Private", 1, "B-2")
    airforce_pilot.war_cry()

    soldier1.seniority(soldier2)

if __name__ == "__main__":
    main()