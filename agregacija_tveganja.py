import random
import time
import statistics as st
import numpy as np
import matplotlib.pyplot as plt

start = time.time()

NUMBER_OF_SIMULATIONS = 1000

# Nastavitev vrednosti
TVEGANJA = [["požar", 5, 1000, 10000], 
            ["poplava", 1, 10000, 10000], 
            ["kibernetski", 2, 10000, 40000], 
            ["potres", 3, 100, 50000], 
            ["napad vesoljcev", 1, 1000, 2000], 
            ["strela", 4, 10, 1000], 
            ["vlom", 1, 1000, 10000], 
            ["toča", 2, 5, 50], 
            ["tornado", 1, 4000, 60000], 
            ["meteorit", 1, 10000, 100000],]


# Deluje do števil dolgih 14 mest
def random_f(bottom, upper):
    while True:
        tm = str(time.time()).split(".")

        tm2o = tm[1][::-1]
        last = int(tm2o[-1])
        tm2 = ""
        for i in range(len(tm2o)):
            tm2oint = int(tm2o[i])
            if tm2oint < last:
                tm2oint += 1
            tm2 += str(abs(tm2oint - last))

        x = int(tm[0][-len(tm[1])-1:-1])
        tm1 = str(x + int(tm2))

        if len(tm1) > len(tm2):
            tm1 = tm1[1:]
        t = str(tm1) + tm[1]

        try:
            t = int(t[-len(str(upper))-1:-1])
            if t <= upper and t >= bottom:
                return t
        except ValueError:
            continue


def generate_frequency(freq) -> list[int]:
    frequency: list[int] = [random_f(0, freq) for _ in range(100)]
    return frequency


def generate_damage(frequency, lower, upper) -> list[int]:
    damage = []
    for f in frequency:
        for _ in range(f):
            damage.append(random_f(lower, upper))
    
    return damage

# Klikokrat se bo požar zgodil v enem letu
def simulation(simulations, freq, lower, upper) -> list[int]:
    frequency = generate_frequency(freq)
    damage = generate_damage(frequency, lower, upper)
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


def show(data):
    m = st.mean(data)
    std = st.stdev(data)

    # Histogram
    plt.hist(data, bins=100, color="skyblue", edgecolor="black", density=False)

    # Označimo srednjo vrednost in ±1σ, ±2σ
    for x in [m - 2*std, m - std, m, m + std, m + 2*std]:
        plt.axvline(x, color="red", linestyle="--")

    plt.xlabel("Škoda")
    plt.ylabel("Relativna frekvenca")
    plt.title(f"Porazdelitev škode ({NUMBER_OF_SIMULATIONS} ponovitev)")
    plt.show()


def main():
    škoda = {"požar" : [], 
            "poplava" : [], 
            "kibernetski" : [], 
            "potres" : [], 
            "napad vesoljcev" : [], 
            "strela" : [], 
            "vlom" : [], 
            "toča" : [], 
            "tornado" : [], 
            "meteorit" : [], 
            }

    for tveganje in TVEGANJA:
        škoda[tveganje[0]] = simulation(NUMBER_OF_SIMULATIONS, tveganje[1], tveganje[2], tveganje[3])

    yearly_damage = []
    for index in range(NUMBER_OF_SIMULATIONS):
        sum = 0
        for key in škoda.keys():
            sum += škoda[key][index]
        yearly_damage.append(sum)

    sorted = bubble_sort(yearly_damage)

    print(f"Celoten čas: {time.time() - start}")

    extreme_value = round(np.percentile(sorted, 95), 2)
    print(extreme_value)

    show(sorted)

main()