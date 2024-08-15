import math

def factor(target):
    # For target, return a list of it's factors
    factors = []
    for i in range(1, int(math.sqrt(target))+1):
        if (target % i) == 0:
            factors.append(i)
            if (target / i) != i  & i != 1:
                factors.append(int(target / i))
    return factors


def abundant(target):
    # returns true if the target number is abundant
    factors = factor(target)
    total_factors = 0
    # sum all the factors
    for j in factors:
        total_factors = j + total_factors
    if total_factors > target:
        return True
    return False