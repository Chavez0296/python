class Animal:
    def __init__(self, name, species, legs, habitat) -> None:
        self.name = name
        self.species = species
        self.legs = legs
        self.habitat = habitat
        self.animDict = {
            "Name": "",
            "Species": "",
            "Legs": "",
            "Habitat": "",
        }
        self.animDict["Name"] = self.name
        self.animDict["Species"] = self.species
        self.animDict["Legs"] = self.legs
        self.animDict["Habitat"] = self.habitat
    def __str__(self):
        return f"{self.animDict}"

a1 = Animal("Lion", "Mammal", 4, "Savannah")
print(a1)