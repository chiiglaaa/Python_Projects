def bubble_sorting(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

arr = [5, 1, 4, 2, 8] # you can change the array but dont make it too big
print(f"Unsorted array: {arr}")
print(f"Sorted array: {bubble_sorting(arr)}")