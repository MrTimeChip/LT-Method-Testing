import random
import math
import copy


class AnomalyContext:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def with_outlier(self, avg_impact=0.99):
        new_x = copy.copy(self.x)
        new_y = copy.copy(self.y)
        min_y = min(new_y)
        max_y = max(new_y)

        avg = (min_y + max_y) // 2
        amount = len(new_y)
        for i in range(amount):
            if random.random() > avg_impact:
                min_seed = math.trunc(avg * 1.7 - avg / 2)
                max_seed = math.trunc(avg + avg / 4)
                print(min_seed, max_seed)
                new_y[i] = random.randint(min_seed, max_seed)
            else:
                new_y[i] = random.randint(min_y, max_y)
            print(min_y, max_y)
        return AnomalyContext(new_x, new_y)

    def with_step(self, after=500, over=300, diff=5):
        new_x = copy.copy(self.x)
        new_y = copy.copy(self.y)
        amount = len(new_x)
        piece = diff / over
        coeff = piece
        for i in range(after, amount):
            new_y[i] += coeff
            if coeff < diff:
                coeff += piece
        return AnomalyContext(new_x, new_y)

    def with_random(self):
        new_x = copy.copy(self.x)
        new_y = copy.copy(self.y)
        amount = len(new_x)
        for i in range(amount):
            new_y[i] *= random.randint(800, 1000) / 1000
        return AnomalyContext(new_x, new_y)

    def extract(self):
        return self.x, self.y


def generate_values(min_value=60, max_value=65, amount=1500):
    x = []
    y = []
    for i in range(amount):
        value = random.randint(min_value, max_value)
        x.append(i)
        y.append(value)
    return AnomalyContext(x, y)