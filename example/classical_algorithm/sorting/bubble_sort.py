import random

def bubble_sort(data: list) -> list:
    maxIdx = len(data) - 1

    for counter in range(maxIdx):
        print("counter %d" % counter)
        idx = 0
        while idx < maxIdx:
            if data[idx] > data[idx + 1]:
                tmp = data[idx]
                data[idx] = data[idx + 1]
                data[idx + 1] = tmp

            idx += 1
            print(data)


    return data

if __name__ == '__main__':
    data = randomlist = random.sample(range(0, 20), 5)
    print(data)
    print(bubble_sort(data))