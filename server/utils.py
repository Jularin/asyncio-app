def rearrange(arr, stop):
    for i in range(0, stop, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return "".join(arr)
