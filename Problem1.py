import math
import time


def problem1(x):
    result = 0

    for i in range(1,x):
        if (math.remainder(i, 3) == 0) | (math.remainder(i, 5) == 0):
            result += i
    return result


def main():
    print("Project Euler, Problem 1")

    start = time.time()
    print(start)
    result = problem1(1000)
    elapsed_time = time.time() - start
    print(f"Answer {result}")
    print(f"{elapsed_time} s")


if __name__ == '__main__':
    main()
