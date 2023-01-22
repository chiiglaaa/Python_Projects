def insertion_sorting(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                if array[j] < array[j-1]:
                    while array[j-1] < array[j]:
                        array[j], array[j + 1] = array[j + 1], array[j]
    return array

arr = [12, 11, 7, 10, 3, 1, 20, 9, 13, 5, 6]
print(insertion_sorting(arr))