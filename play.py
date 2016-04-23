def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print("5!={:,}, 3!={:,}, 11!={:,}".format(factorial(5), factorial(3), factorial(11)))


def fibonacci(limit):
    nums = []
    current = 0
    next = 1
    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


print('via list')
for n in fibonacci(100):
    print(n, end=', ')

print()


def fibonacci_co():
    current = 0
    next = 1
    while True:
        current, next = next, next + current
        yield current


print('with yield')
for n in fibonacci_co():
    if n > 1000:
        break
    print(n, end=', ')
