# fibonacci sequence iterative
first = 0
second = 1
num = int(input("Enter the number: "))


def fibonacci(x, y, n):
    for i in range(n):
        x, y = y, x+y
    return x


print(fibonacci(first, second, num))
