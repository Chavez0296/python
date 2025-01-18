def dib(n):
    if n <= 1:
        return
    dib(n-1)
    dib(n-1)
    
def fib(n):
    if n <=2:
        return 1
    return fib(n-1) + fib(n-2)
'''
    O(dib) <= O(fib) <= O(lib)
    O(2^n) <= O(2^n) <= O(2^n)
    O(n) space complexity 
'''
def lib(n):
    if n <= 1:
        return
    lib(n-2)
    lib(n-2)
    
def fibtwo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n] 
    if n <=2:
        return 1
    memo[n] = fibtwo(n-1,memo) + fibtwo(n-2,memo) #stores values bot
    return memo[n]
# dynamic programming approach changes the time complexity to  O(n) and O(n) space complexity
print(fibtwo(6))
print(fibtwo(7))
print(fibtwo(8))
print(fibtwo(50))
