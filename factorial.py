import time


def factorial(num):
    if num < 0:
        raise TypeError
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def non_r_factorial(num):
    if num < 0:
        raise TypeError
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product


if __name__ == "__main__":
    start_time = time.time()
    print(factorial(45))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Recursive time: {elapsed_time} seconds")
    start_time = time.time()
    print(non_r_factorial(45))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Non Recursive time: {elapsed_time} seconds")
