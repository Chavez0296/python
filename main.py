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

def string_leng(inp):
    count = 0
    for i in range(len(inp)):
        count += 1
    return count

print(string_leng("hello"))

setter = set([1,2,2,3,4])
print(setter)

class Example:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value)

obj = Example("Hello")
obj.value = "World"
obj.display()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)

sq = [x**2 for x in range(5)]
print(sq)