import random
import time
import statistics as st
import numpy as np

NUMBER_OF_SIMULATIONS = 1000
FIRE_F = 5
FIRE_LOWER = 1000
FIRE_UPPER = 10000

# Deluje do števil dolgih 16 mest
def random_f(bottom, upper):
    while True:
        try:
            t = int(str(time.time())[-len(str(upper))-1:-1][::-1])
            if t <= upper and t >= bottom:
                return t
        except ValueError:
            continue


def generate_frequency() -> list[int]:
    frequency: list[int] = [random_f(0, 5) for _ in range(100)]
    return frequency


def generate_damage(frequency) -> list[int]:
    damage = []
    for f in frequency:
        for _ in range(f):
            damage.append(random_f(1000, 10000))
    
    return damage

# Klikokrat se bo požar zgodil v enem letu
def simulation(simulations) -> list[int]:
    frequency = generate_frequency()
    damage = generate_damage(frequency)
    one_year: list[int] = []

    for _ in range(simulations):
        d = 0
        for _ in range(random.choice(frequency)):
            d += random.choice(damage)
        one_year.append(d)
    
    return one_year


def bubble_sort(sim):
    for _ in range(len(sim)):
        switch = False
        for index in range(len(sim)-1):
            if sim[index] > sim[index + 1]:
                switch = True
                temp = sim[index]
                sim[index] = sim[index + 1]
                sim[index + 1] = temp
        
        if not switch:
            break
    
    return sim


sim = simulation(NUMBER_OF_SIMULATIONS)
sorted = bubble_sort(sim)
extreme_value = round(np.percentile(sorted, 95), 2)
print(extreme_value)
