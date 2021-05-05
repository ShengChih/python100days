import random

def merge_sort(data: list):
    length = len(data)

    if length == 1:
        return
    elif length == 2:
        if data[0] > data[1]:
            data[0], data[1] = data[1], data[0]

    mid = length // 2
    left = data[:mid]
    right = data[mid:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

    return

if __name__ == '__main__':
    data = random.sample(range(0, 100), 10)
    print(data)
    merge_sort(data)
    print(data)