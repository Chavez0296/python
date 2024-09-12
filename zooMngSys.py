class Animal: #creating Animal class
    def __init__(self, name, species, legs, habitat) -> None: #constructor to construct an instance of an Animal with specific data
        self.name = name
        self.species = species
        self.legs = legs
        self.habitat = habitat
        self.animDict = {    #initialize dictionary to hold all data pertaining to intance of Animal
            "name": "",
            "species": "",
            "legs": "",
            "habitat": "",
        }
        self.animDict["name"] = self.name#putting all the data associated with intance of Animal into a dictionary
        self.animDict["species"] = self.species
        self.animDict["legs"] = self.legs
        self.animDict["habitat"] = self.habitat

    def print_animal_details(self, animDict): #print animal details function that passes in dictionary of animal instance
        print(f"Name: {animDict['name']}, Species: {animDict['species']}, Legs: {animDict['legs']}, Habitat: {animDict['habitat']}") #prints data according to assignment requirements

    def classify(self, legs): #classify function declaration
        newLegs = int(legs)   #convert legs into an int and store it in place holder
        if newLegs == 0:      # if legs is 0 
            return "Snake or Fish" #this will return 
        elif newLegs == 2:    #if legs is 2 then 
            return "Bird or Human" #this returns
        elif newLegs == 4:    #if legs is 4 then
            return "Mammal or Reptile" #this returns 
        else:
            return "Insect or Spider" #legs is greater than 4 then this returns.


animalList = []  #initialize list to store Animal instances
animalList.append(Animal("Lion", "Mammal", 4, "Savannah")) #add all the animals to the list
animalList.append(Animal("Cow", "Mammal", 4, "Grassland"))
animalList.append(Animal("Shark","Fish", 0, "Ocean"))
animalList.append(Animal("Spider", "Insect", 6, "Backyard"))
animalList.append(Animal("Human", "Mammal", 2, "Everywhere"))
animalList.append(Animal("Dog", "Mammal", 4, "Land"))

for i in range(len(animalList)): #iterate through the list and call the print_animal_details
    animalList[i].print_animal_details(animalList[i].animDict)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

for i in range(len(animalList)): #iterate through the list and print what the classification of each animal in the list is based on legs
    print(f"{animalList[i].animDict['name']}: {animalList[i].classify(animalList[i].animDict['legs'])}") #used f string to print based on assignment requirement to print animal name along side classification

