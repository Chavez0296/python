def add(x, y, z):    #declare add function that accepts 3 arguments
    return x + y + z # returns the addition of 3 arguments passed in 

def subtract(x, y, z):# declare subtract function that accepts 3 arguments
    return z - y - x  # returns the subtraction of the 3 arguments in reverse order

def multiply(x, y): # declare multiply function that takes two arguments
     return x * y   # returns the multiplication of the two arguments

def divide(x, y):   # delcare divide function that takes two arguments
    if y == 0:      # if y == 0 condition to notify user that dividing by 0 is not possible
        print(f"{x}/{y}: Having a denominator of 0 will reult in a ZeroDivisionError!") #print error notice
        return          # returns None if this happens
    return x / y        # else it returns the division of x / y

expression = divide(multiply(add(1,1,1),1),multiply(subtract(1,4,6),1)) # initialize expression to hold math expression  ((x+y+z)*x)/(z-y-x)*y
print(expression)   #prints the result of the calculation

undefined = divide(4,0)  #example to show the division by 0 error 
print(undefined)  # prints the example
