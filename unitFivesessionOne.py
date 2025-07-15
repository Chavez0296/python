class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    def add_item(self, item_name):
        check = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu","cacao tree"]
        for elem in check:
            if item_name == elem:
                self.furniture.append(item_name) 
def of_personality_type(townies, personality_type):
    group = []
    for townie in townies:
        if townie.personality == personality_type:
            group.append(townie.name)
    return group
def message_received(start_villager, target_villager):
    
    while start_villager.neighbor != None:
        start_villager = start_villager.neighbor

        if start_villager == target_villager:
            return True
    
    return False

apollo = Villager("Apollo", "Eagle", "lazy", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)


alice = Villager("Alice", "Koala", "lazy", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle
print_linked_list(kk_slider)

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head == None:
        print("Aw! Better luck next time!")
        return None

    print(f"I caught {head.fish_name}!")
    head = head.next
  
    return head
    pass

def fish_chances(head, fish_name):
    tot = float(0)
    found = float(0)

    while head != None:
        tot += 1
        if head.fish_name == fish_name:
            found += 1

        head = head.next
        
    return round(found/tot,2)
    pass

def restock(head, new_fish):
    curr = head
    while curr:
        if curr.next == None:
            curr.next = Node(new_fish)
            return head
        curr = curr.next
    return      
    pass

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))

#Carp -> Dace -> Cherry Salmon -> Rainbow Trout