def merge_sort(arr):
    print(arr, " Array")
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return list(sorted(left + right))

example = [54,26,93,17,77]
print(merge_sort(example))
