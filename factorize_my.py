from time import time
from concurrent.futures import ProcessPoolExecutor
import sys


def counter(number):
    result = []
    for n in range(1, number + 1):
        if number % n == 0:
            result.append(n)
    return result


def factorize(*number):
    with ProcessPoolExecutor(4) as executor:
        result = list(executor.map(counter, number))
    return result


if __name__ == "__main__":
    timer = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f"{a}\n{b}\n{c}\n{d}")
    print(f'Time: {round(time() - timer, 4)}', file=sys.stderr)