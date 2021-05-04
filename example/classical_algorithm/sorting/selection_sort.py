import random

def selection_sort(data: list):
    maxIndex = len(data) - 1
    minIdx = 0

    for cmpIdx in range(0, maxIndex):
        minIndex = cmpIdx + 1
        loopIdx = minIndex + 1

        while loopIdx < maxIndex:
            if data[loopIdx] < data[minIndex]:
                minIndex = loopIdx
            loopIdx += 1

        if data[cmpIdx] > data[minIndex]:
            data[cmpIdx], data[minIndex] = data[minIndex], data[cmpIdx]

    return

if __name__ == '__main__':
    data = random.sample(range(0, 100), 10)
    print(data)
    selection_sort(data)
    print(data)
