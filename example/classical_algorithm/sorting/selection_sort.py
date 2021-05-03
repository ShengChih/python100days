import random

def selection_sort(data: list) -> list:
    maxIndex = len(data) - 1
    minIdx = 0

    for cmpIdx in range(0, maxIndex):
        print("Loop %s:" % cmpIdx)
        minIndex = cmpIdx + 1
        loopIdx = minIndex + 1

        while loopIdx < maxIndex:
            if data[loopIdx] < data[minIndex]:
                minIndex = loopIdx
            loopIdx += 1

        if data[cmpIdx] > data[minIndex]:
            tmp = data[cmpIdx]
            data[cmpIdx] = data[minIndex]
            data[minIndex] = tmp

        print(data)

    return data

if __name__ == '__main__':
    data = random.sample(range(0, 100), 10)
    print(data)
    print(selection_sort(data))
