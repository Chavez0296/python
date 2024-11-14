import random


def add_numbers(a,b):
    result = a + b
    return result

original_list = [1,2,3,4,5]
mod_list = original_list[:2] + [10] + original_list[3:]


#Iterative Loop
def factorial_nonrecur(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#recursive loop

def factorial_Rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_Rec(n - 1)
    
def filter_words(word_list, condition_func):
    filter_words = [word for word in word_list if condition_func(word)]
    return filter_words

def is_long_word(word):
    return len(word)> 5

word_list = ['apple', 'banana', 'grape', 'apricot', 'kiwi', 'strawberry']

result2 = filter_words(word_list, is_long_word)

#Using imperative Programming

numbers = [1,2,3,4,5]
squared_nums = []

for num in numbers:
    squared_nums.append(num**2)

print(f"Squared: {squared_nums}")


#Using Functional Programming

def square(num):
    return num ** 2

squared_numms = list(map(square,numbers))
print("Squared numbers (Functional): ", squared_numms)

#Pure Function

def add(a,b):
    total = a + b
    return total
print(add(5,10))

#Impure Function

def adding(a,b):
    total = a + b
    print(total)
    #printing to the console from the function is a side-effect

def randAdd(a,b):
    total = a + b + random.randint(1,10)
    return total
#impure function because it gives different outputs




#An example of a side-effect in Python:
# Global variable
counter = 0
# Function with a side effect
def increment_counter():
    global counter
    counter += 1
# Calling the function results in a side effect
increment_counter()
print("Counter:", counter) # Output: Counter: 1















print(f"Original List: {original_list}")
print(f"Modified List: {mod_list}")
print(f"{original_list[3:]}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(factorial_nonrecur(5))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(factorial_Rec(5))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Long words: ", result2)