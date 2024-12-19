def max_chunks(arr):
    max_so_far = 0
    chunk = 0

    for i in range(len(arr)):
        max_so_far = max(max_so_far, arr[i])

        if i == max_so_far:
            chunk += 1
    return chunk


arr = [4, 3, 2, 1, 0]
print(max_chunks(arr))
