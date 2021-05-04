import random

def insertion_sort(data: list):
    for undoIdx in range(1, len(data)):
        sortedIdx = undoIdx - 1
        key = data[undoIdx]

        while sortedIdx >= 0 and key < data[sortedIdx]:
            data[sortedIdx + 1] = data[sortedIdx]
            sortedIdx -= 1

        data[sortedIdx + 1] = key

    return

if __name__ == '__main__':
    data = random.sample(range(1, 100), 10)
    print(data)
    insertion_sort(data)
    print(data)