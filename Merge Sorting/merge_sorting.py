def merge_sort(arr):
    print(arr, " Array")
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    print(left, " Left")
    right = merge_sort(arr[mid:])
    print(right," Right")
    print(list(sorted(left + right)), " Returner")
    return list(sorted(left + right))

example = [54,26,93,17,77]
print(merge_sort(example))
