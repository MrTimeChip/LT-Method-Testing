import random
import math
import copy


class AnomalyContext:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def using(self, x, y):
        return AnomalyContext(copy.copy(x), copy.copy(y))

    def with_outlier(self, avg_impact=0.99, extreme_multiplier=1):
        new_x = copy.copy(self.x)
        new_y = copy.copy(self.y)
        min_y = math.trunc(min(new_y))
        max_y = math.trunc(max(new_y))

        sgn = math.copysign(1, extreme_multiplier)
        extreme_multiplier = abs(extreme_multiplier)

        avg = (min_y + max_y) // 2

        min_seed = math.trunc((avg * 1.7 - avg / 2) * extreme_multiplier)
        max_seed = math.trunc((avg + avg / 4) * extreme_multiplier)

        amount = len(new_y)
        for i in range(amount):
            if random.random() > avg_impact:
                new_y[i] = new_y[i] + sgn * random.randint(min_seed, max_seed)
        return AnomalyContext(new_x, new_y)

    def with_step(self, after=500, over=300, diff=5):
        new_x = copy.copy(self.x)
        new_y = copy.copy(self.y)
        amount = len(new_x)
        piece = diff / over
        coeff = piece
        for i in range(after, amount):
            new_y[i] += coeff
            if abs(coeff) < abs(diff):
                coeff += piece
        return AnomalyContext(new_x, new_y)

    def with_random(self):
        new_x = copy.copy(self.x)
        new_y = copy.copy(self.y)
        amount = len(new_x)
        for i in range(amount):
            new_y[i] *= random.randint(900, 1100)/1000
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


def generate_periodic_values(min_value=25, max_value=75, amount=1500,
                             period_multiplier=1):
    x = []
    y = []
    half_range = (max_value - min_value) / 2
    for i in range(amount):
        value = min_value + half_range + math.sin(period_multiplier * i) * half_range
        x.append(i)
        y.append(value)
    return AnomalyContext(x, y)


def empty():
    return AnomalyContext([], [])
