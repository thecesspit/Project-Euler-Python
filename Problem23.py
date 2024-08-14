import math
import time


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


def problem23(upper):
    # first find abundant numbers below the upper range
    abundant_numbers = []
    result = 0

    for i in range(1, int(upper)):
        if abundant(i):
            abundant_numbers.append(i)

    # create a list upper long with 0's in each place
    n_list = [0 for i in range(0,upper+1)]

    # for each pair of number in the abundant list, add them together and add 1 to that position in the list.
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i+j <= upper:
                n_list[i+j] += 1

    # go back through the list and add up every index where the value is still 0
    for key, z in enumerate(n_list):
        if z == 0:
            result = result + key
    return result


def main():
    # https://projecteuler.net/problem=23
    print("Project Euler, Problem 23 - Non-abundant Sums")

    start = time.time()
    result = problem23(28123)
    end = time.time()
    elapsed = end - start
    print(f"Answer {result}")
    print(f"{elapsed} s :: {start} {end}")


if __name__ == '__main__':
    main()
