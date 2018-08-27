import numpy


def fib_recursive(n: int):
    if n < 2:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iter(n: int):
    a, b = 1, 1

    for _ in range(n):
        a, b = a + b, a

    return b


def fib_matpow(n: int):
    m = numpy.matrix('1 1 ; 1 0') ** n
    return m.item(0)


def fib(n):
    return (4 << n * (3 + n)) // ((4 << 2 * n) - (2 << n) - 1) & ((2 << n) - 1)


def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    print(cache)
    return cache[n]


if __name__ == '__main__':
    print(staircase(3, [1, 3, 5]))
