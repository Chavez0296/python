# Problem 1: Hundred Acre Wood
# Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".

def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

# Write a function greeting() that accepts a single parameter, a string name, 
# and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greeting("Luis")

# Problem 3: Catchphrase
# Write a function print_catchphrase() that accepts a string character as a parameter and 
# prints the catchphrase of the given character as outlined in the table below.

def print_catchphrase(character):
    match character:
        case "Pooh":
            return "Oh brother!"
        case "Tigger":
            return "TTFN: Ta=ta for now!"
        case "Eeyore":
            return "Thanks for noticing me."
        case "Christopher Robin":
            return "Silly old bear."
        case default:
            return "Sorry! I don't know Piglet's catchphrase!"
character = "Pooh"
print(print_catchphrase(character))

character = "Piglet"
print(print_catchphrase(character))

# Problem 4: Return Item
# Implement a function get_item() that accepts a 0-indexed list items and a 
# non-negative integer x and returns the element at index x in items. 
# If x is not a valid index of items, return None.


def get_item(items,x):
    if x <= len(items):
        print( items[x])
    else:
        print(None)
    
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

# Problem 5: Total Honey
# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() 
# that accepts a list of integers hunny_jars and returns the sum of all elements 
# in the list. Do not use the built-in function sum().

def sum_honey(hunny_jars):
    sums = 0
    for x in range(len(hunny_jars)):
        sums += hunny_jars[x]

    print(sums)

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

#Problem 6: Double Trouble
#Help Winnie the Pooh double his honey! Write a function doubled() 
# that accepts a list of integers hunny_jars as a parameter and multiplies 
# each element in the list by two. Return the doubled list.

def doubled(hunny_jars):
    print([hunny_jars[x]*2 for x in range(len(hunny_jars))])

hunny_jars = [1, 2, 3]
doubled(hunny_jars)

# Problem 7: Poohsticks
# Winnie the Pooh and his friends are playing a game called Poohsticks 
# where they drop sticks in a stream and race them. They time how long 
# it takes each player's stick to float under Poohsticks Bridge to score each round.

# Write a function count_less_than() to help Pooh and his friends determine 
# how many players should move on to the next round of Poohsticks. 
# count_less_than() should accept a list of integers race_times and an integer 
# threshold and return the number of race times less than threshold.

def count_less_than(race_times, threshold):
    print([race_times[x] for x in range(len(race_times)) if race_times[x] < threshold])

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)

# Problem 8: Pooh's To Do's
# Write a function print_todo_list() that accepts a list of strings named tasks. 
# The function should then number and print each task on a new line using the format:

# Pooh's To Dos:
# 1. Task 1
# 2. Task 2
# ...

def print_todo_list(task):
    print("Pooh's To Dos:")
    count = 1
    for i in range(len(task)):
        print(f"{count}. {task[i]}")
        count += 1

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

# Problem 9: Pairs
# Rabbit is very particular about his belongings and wants to own an 
# even number of each thing he owns. Write a function can_pair() that 
# accepts a list of integers item_quantities. Return True if each number 
# in item_quantities is even. Return False otherwise.

def can_pair(item_quantities):
   
    flag = True
    for x in range(len(item_quantities)):
        if item_quantities[x] % 2 != 0:
            flag = False
    print(flag)
         
item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)

# Problem 10: Split Haycorns
# Piglet's has collected a big pile of his favorite food, haycorns, 
# and wants to split them evenly amongst his friends. 
# Write a function split_haycorns() to help Piglet determine 
# the number of ways he can split his haycorns into even groups. split_haycorns() 
# accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.

def split_haycorns(quantity):
    divs = []
    for x in range(1,quantity+1):
        if quantity % x == 0:
            divs.append(x)
    print(divs)

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)

# Problem 11: T-I-Double Guh-ER
# Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around 
# stealing any letters he needs to spell out his name. Write a function tiggerfy() 
# that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.

def tiggerfy(s):
    
    remove = set("tiger")

    filtered = []
    for ch in s:
        if ch.lower() not in remove:
            filtered.append(ch)
    
    print(f"{"".join(filtered)}")

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)

# Problem 12: Thistle Hunt
# Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
# Write a function locate_thistles() that takes in a list of strings items 
# and returns a list of the indices of any elements with value "thistle". 
# The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
    locations = []
    for i in range(len(items)):
        if items[i] == "thistle":
            locations.append(i)

    print(locations)

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)

#Write a function linear_search() to help Winnie the Pooh locate 
# his lost items. The function accepts a list items and a target value 
# as parameters. The function should return the first index of target 
# in items, and -1 if target is not in the lst. Do not use any built-in 
# functions.

def linear_search(lst, target):
    found = -1
    for i in range(len(lst)):
        if lst[i] == target:
            found = i

    print(found)

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)

# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming 
# language Tiger with only four operations and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# #Initially, the value of tigger is 1 because he's the only tigger around! 
# Given a list of strings operations containing a list of operations, 
# return the final value of tigger after performing all the operations.

def final_value_after_operations(operations):
    tigger = 1
    
    for i in range(len(operations)):
        if (operations[i] == "bouncy" or operations[i] == "flouncy"):
            tigger += 1
        elif (operations[i] == "trouncy" or operations[i] == "pouncy"):
            tigger -= 1
        else:
            continue
    
    print(tigger)
    
operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)

# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger! 
# Write a function tiggerfy() that accepts a string word 
# and returns a new string that removes any substrings t, i, gg, and er 
# from word. The function should be case insensitive.

def tiggerfy(word):
    
    result_chars = []
    i = 0
    word_lower = word.lower()
    n = len(word)
    
    while i < n:
        # 1) Check for the two‐letter substrings "gg" or "er" first:
        if i + 1 < n:
            two = word_lower[i : i + 2]
            if two == "gg" or two == "er":
                # Skip both characters
                i += 2
                continue
        
        # 2) If we didn’t match a two‐letter pattern, check for single "t" or "i":
        one = word_lower[i]
        if one == "t" or one == "i":
            # Skip this one character
            i += 1
            continue
        
        # 3) Otherwise, keep the original character (preserving its case)
        result_chars.append(word[i])
        i += 1
    
    print("".join(result_chars))    
    

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)



def local_maximums(grid):
    n = len(grid)

    if n < 3:
        return []
    
    row_max = [[0]*(n-2) for _ in range(n)]
    for r in range(n):
        for c in range(n-2):
            a,b,d = grid[r][c], grid[r][c+1], grid[r][c+2]
            row_max[r][c] = a if a >= b and a >= d else(b if b >= c else c)

    m = n - 2
    local_maxes = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            x,y,z = row_max[i][j], row_max[i+1][j], row_max[i+2][j]
            local_maxes[i][j] = x if x >= y and x >= z else (y if y >= z else z)

    return local_maxes

grid1 = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]

grid2 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

# Compute and display results:
print(local_maximums(grid1))
print(local_maximums(grid2))

        