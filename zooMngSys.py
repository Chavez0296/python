class Animal:
    def __init__(self, name, species, legs, habitat) -> None:
        self.name = name
        self.species = species
        self.legs = legs
        self.habitat = habitat
        self.animDict = {
            "name": "",
            "species": "",
            "legs": "",
            "habitat": "",
        }
        self.animDict["name"] = self.name
        self.animDict["species"] = self.species
        self.animDict["legs"] = self.legs
        self.animDict["habitat"] = self.habitat
    def print_animal_details(self, animDict):
        print(f"Name: {animDict['name']}, Species: {animDict['species']}, Legs: {animDict['legs']}, Habitat: {animDict['habitat']}")
    def classify(self, legs):
        newLegs = int(legs)
        if newLegs == 0:
            return "Snake or Fish"
        elif newLegs == 2:
            return "Bird or Human"
        elif newLegs == 4:
            return "Mammal or Reptile"
        else:
            return "Insect or Spider"


animalList = []
animalList.append(Animal("Lion", "Mammal", 4, "Savannah"))
animalList.append(Animal("Cow", "Mammal", 4, "Grassland"))
animalList.append(Animal("Shark","Fish", 0, "Ocean"))
animalList.append(Animal("Spider", "Insect", 6, "Backyard"))
animalList.append(Animal("Human", "Mammal", 2, "Everywhere"))
animalList.append(Animal("Dog", "Mammal", 4, "Land"))

for i in range(len(animalList)):
    animalList[i].print_animal_details(animalList[i].animDict)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

for i in range(len(animalList)):
    print(f"{animalList[i].animDict['name']}: {animalList[i].classify(animalList[i].animDict['legs'])}")

