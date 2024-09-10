from functools import reduce
numbers = [1,2,3]

result = filter(lambda n : n % 2 == 0, numbers)
result = map(lambda a : a * 2, numbers)

print(list(result)) #filter and map global functions

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]
sum = reduce(lambda a, b: a[1] + b[1], expenses) #reduce

print(sum)

def factorial(n): #recursion
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))

def increment(n: int) -> int: #annotations
    return n + 1

print(increment(2))