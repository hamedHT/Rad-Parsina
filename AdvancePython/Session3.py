class FootBall:
    def __init__(self, country, division, no_of_times):
        self.country = country
        self.division = division
        self.no_of_times = no_of_times
    def fifa(self):
        print(f"{self.country} national football team is placed in '{self.division}' FIFA division")
class WorldChampions(FootBall):
    def world_championship(self):
        print(f"{self.country} national football team is {self.no_of_times} times world champions")
def main():
    germany = WorldChampions("Germany", "UEFA", 4)
    germany.fifa()
    germany.world_championship()
if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------------------------

class Country:
    def __init__(self, country_name):
        self.country_name = country_name
    def country_details(self):
        print(f"Happiest Country in the world is {self.country_name}")
class HappiestCountry(Country):
    def __init__(self, country_name, continent):
        super().__init__(country_name)
        self.continent = continent
    def happy_country_details(self):
        print(f"Happiest Country in the world is {self.country_name} and is in {self.continent} ")
def main():
        finland = HappiestCountry("Finland", "Europe")
        finland.happy_country_details()
if __name__ == "__main__":
        main()