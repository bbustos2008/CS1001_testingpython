import collections
import random

class customer:
    def __init__(self, name):
        self.name = name

line = collections.deque()

names = ["Bill", "John","Carol","Joan", "Enrique"]
for c in range(1,10):
    name = random.choice(names)
    customer = customer(name)
    line.append(name)  

while len(line) > 0:
    lane = random.randrange(0,2)
    if lane == 0:
        c = line.pop()
        print(f"{customer} is in lane {lane}")
    else:
        c = line.popleft()
        print(f"{customer} is in lane {lane}")    