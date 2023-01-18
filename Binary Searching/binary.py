# binary search using recursion

minimum_value = int(input("enter min value: "))     # minimum number
maximum_value = int(input("enter max value: "))    # maximum number
find = int(input("choose the number:  "))          # the number we need to find
guess = (minimum_value + maximum_value) // 2
#

def binary(min, max, n, guess):
    if guess == n:
        print(f"The number is {guess}.")
    elif guess > n:
        max = guess - 1
        guess = (min + max) // 2
        print("The number is greater than the actual number.")
        print(guess)
        return binary(min, max, n, guess)
    elif guess < n:
        min = guess + 1
        guess = (min + max) // 2
        print("The number is lower than the actual number.")
        print(guess)
        return binary(min, max, n, guess)


print(binary(minimum_value, maximum_value, find, guess))
