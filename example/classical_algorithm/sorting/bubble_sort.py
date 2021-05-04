import random

def bubble_sort(data: list):
    maxIdx = len(data) - 1

    for counter in range(maxIdx):
        idx = 0
        while idx < maxIdx:
            if data[idx] > data[idx + 1]:
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
            idx += 1
        maxIdx -= 1

    return

if __name__ == '__main__':
    data = randomlist = random.sample(range(0, 100), 10)
    print(data)
    bubble_sort(data)
    print(data)