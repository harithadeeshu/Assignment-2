def move_negative_elements(arr):
    n = len(arr)
    neg_idx = 0

    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[neg_idx] = arr[neg_idx], arr[i]
            neg_idx += 1

    return arr

arr = [4, -3, 2, -5, -1, 0, -2, 6, -7]
result = move_negative_elements(arr)
print("Array with negative elements moved to one side:", result)
