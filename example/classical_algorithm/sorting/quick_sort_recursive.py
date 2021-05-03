import random

def partition(data: list, low: int, high: int) -> int:
    i = low - 1
    pivot = data[high]

    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]

    return (i + 1)

def quick_sort(data: list, low: int, high: int):
    if low < high:
        pIdx = partition(data, low, high)
        
        quick_sort(data, low, pIdx - 1)
        quick_sort(data, pIdx + 1, high)


if __name__ == '__main__':
    data = random.sample(range(0, 100), 10)
    print(data)
    quick_sort(data, 0, 9)
    print(data)