'''import datetime

class Trib:
    def __init__(self):
        self.lst = [0,0,1]
    def __iter__(self):

        for i in range(0,36):
            if i < 3:
                yield self.lst[i]
            else:
                self.lst.append(self.lst[i-1]+self.lst[i-2]+self.lst[i-3])
                yield self.lst[i]

a = Trib()
for i in a:
    print(i)'''

import math
class Leibn:
    def __init__(self):
        self.sum = 0
        self.pi = round(math.pi / 4, 2)
        self.step = 1
        self.n = 0

    def __iter__(self):
        while self.sum != self.pi:
            self.element = round((self.step / ((2 * self.n) + 1)), 2)
            self.sum += self.element
            self.sum = round(self.sum,2)
            self.n += 1
            self.step = -1 if self.step == 1 else  1
            yield self.element

a = Leibn()

for i in a:
    print(i)
