import math
import time

def problem40(digits):
    # first find abundant numbers below the upper range
    result = 1
    champernowne = []
    for i in range(1, digits[-1] + 1):
        string_i = str(i)
        for j in range(len(string_i)):
            champernowne.append(int(string_i[j]))
    print(champernowne)
    for d in digits:
        print(f"{d} {champernowne[d-1]}")
        result = result * champernowne[d-1]
    return result


def main():
    # https://projecteuler.net/problem=40
    print("Project Euler, Problem 40 - Champernowne's Constant")

    start = time.time()
    digit_list = [1, 10, 100, 1000, 10000, 100000, 1000000]
    result = problem40(digit_list)
    end = time.time()
    elapsed = end - start
    print(f"Answer {result}")
    print(f"{elapsed} s :: {start} {end}")


if __name__ == '__main__':
    main()
