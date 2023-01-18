
# fibonacci sequence recursive
def fibonacci(x, y, n, a=0):
    if n <= 1:
        return n
    elif n >= 2:
        a += 1
        if a == n:
            print(y)
            return ""
        return fibonacci(y, x+y, n, a)


first = 0
second = 1
num = int(input("Enter the number: "))
print(fibonacci(first, second, num))
