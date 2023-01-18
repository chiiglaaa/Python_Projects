def linear_search(array, k):
    for i in range(0, len(array)):
        if array[i] == k:
            return i
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
k = 13
result = linear_search(array, k)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at: {result}")
