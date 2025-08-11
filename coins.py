import matplotlib.pyplot as plt
import random
from statistics import mean

PONOVITVE = 100000

tosses = [random.randint(0, 1) for _ in range(PONOVITVE)]

mean_value = mean(tosses)
heads = 0

for x in range(int(len(tosses)/5)):
    print(tosses[x*5:x*5+5])
    if tosses[x*5:x*5+5].count(0) == 3:
        heads += 1
    
print(f"Verjetnost, da pade glava je: {round(heads/(PONOVITVE/5)*100, 2)} %")
print(f"Binosmka verjetnost: {round(10/(2**5)*100, 2)} %")