from collections import Counter

def most_endangered(species_lsit):
    if not species_list:
        return None
    
    most = species_list[0]['name']
    low = species_list[0]['population']

    for species in species_list[1:]:
        
        val = species['population']
        
        if val < low:
            lowest = val
            most = species['name']
    
    return most
    

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))


def count_endangered_species(endangered_species, observed_species):
    
    check = set(endangered_species)
    count = 0
    for l in observed_species:
        if l in check:
            count += 1

    return count
    pass


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  



def find_balanced_subsequence(art_pieces):

    count = Counter(art_pieces)
    
    maxLen = 0

    for i, cnt in count.items():
        if (cnt2 := count.get(i+1, 0)) > 0:
            maxLen = max(maxLen, cnt + cnt2)

    pass

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

def is_authentic_collection(art_pieces):

    table = {}
    for i in art_pieces:
        if i not in table:
            table[i] = 0
        table[i] += 1

    if table.get(len(art_pieces)-1,0) != 2:
        return False

    for item in range(1,len(art_pieces)-1):
        if table.get(item,0) != 1:
            return False
    
    return True
    pass

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))

def organize_exhibition(collection):
    freq = {}

    for item in collection:
        if item not in freq:
            freq[item] = 0
        freq[item] += 1
    #print(freq.items())
    newList = [[] for i in range(max(freq.values()))]
    
    for artist,count in freq.items():
       
        for i in range(count):
            #print(f"{artist}")
            newList[i].append(artist)
            

    return newList


    pass

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))

def subdomain_visits(cpdomains):
    domSet = set()
    cpTable = {}

    for domain in cpdomains:
        arr = domain.split()
        cpTable[arr[1]] = arr[0]
        
    pass

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))