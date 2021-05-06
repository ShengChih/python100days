from typing import Type

class Tower(object):

    def __init__(self, index: int):
        self._index = index
        self._disks = []


    @property
    def index(self) -> int:
        return self._index


    @property
    def disks(self) -> list:
        return self._disks


    def add(self, n: int) -> bool:
        if not self._disks or n < self._disks[-1]:
            self._disks.append(n)
            print("加入 %d 至 tower %d" % (n, self._index))
            return True

        return False


    def moveTopTo(self, dest: 'Tower') -> bool:
        n = self._disks.pop()
        print("從 tower %d 拿起 %d" % (self._index, n))

        return dest.add(n)


    def moveDisks(self, n: int, dest: 'Tower', buffer: 'Tower'):
        if n <= 0:
            return

        self.moveDisks(n - 1, buffer, dest)
        self.moveTopTo(dest)
        buffer.moveDisks(n - 1, dest, self)


def main():
    n = 10
    towers = []

    for i in range(0, 3):
        towers.append(Tower(i))

    for j in range(n, 0, -1):
        towers[0].add(j)

    towers[0].moveDisks(n, towers[2], towers[1])
    print(towers[2].disks)


if __name__ == '__main__':
    main()