def howSum(target, nums, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    
    for num in nums:
        remainder = target - num
        remainderResult = howSum(remainder,nums,memo)
        if remainderResult != None:
            memo[target] = [*remainderResult,num]
            return memo[target]
    
    memo[target] = None
    return None

# m = target sum
# n = numbers.length
##
# Brute Force = time O(n^m * m)
# space: O(m)
#
# Memoized
# time: O(n*m^2)
# space: O(m^2)
#

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))