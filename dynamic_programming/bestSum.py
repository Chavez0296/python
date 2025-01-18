def bestSum(targetSum, nums, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestComb = None
    for num in nums:
        remainder = targetSum - num
        remainderComb = bestSum(remainder,nums, memo)
        if remainderComb != None:
            comb = [*remainderComb,num]
            if shortestComb is None or len(comb) < len(shortestComb):
                shortestComb = comb
    memo[targetSum] = shortestComb
    return shortestComb

print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(100,[1,2,5,25]))