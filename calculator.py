def add(x, y, z):
    return x + y + z

def subtract(x, y, z):
    return z - y - x

def multiply(x, y):
     return x * y

def divide(x, y):
    if y == 0:
        print(f"{x}/{y}: Having a denominator of 0 will reult in a ZeroDivisionError!")
        return
    return x / y

expression = divide(multiply(add(1,1,1),1),multiply(subtract(1,4,6),1))
print(expression)

undefined = divide(4,0)
print(undefined)
