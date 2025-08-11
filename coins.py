import matplotlib.pyplot as plt
import random
from statistics import mean

tosses = [random.randint(0, 1) for _ in range(10000)]

mean_value = mean(tosses)

print(mean_value)
print(f"Odstopanje: {round(abs(0.5-mean_value)*100, 2)} %")
plt.hist(tosses)
plt.show()