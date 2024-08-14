import math
import time


def problem2(upper):
    result = 0
    x = 1
    y = 1
    while y <= upper:
        y, x = x+y, y
        if math.remainder(y, 2) == 0:
            result = result + y

    print(f"x {x} y {y}")
    return result


def main():
    print("Project Euler, Problem 2")

    start = time.time()
    result = problem2(4000000)
    end = time.time()
    elapsed = end - start
    print(f"Answer {result}")
    print(f"{elapsed} s :: {start} {end}")


if __name__ == '__main__':
    main()
