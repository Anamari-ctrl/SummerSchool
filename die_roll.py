# Za pomoč je bil uporabljen chat-gpt, za lažji začetek s knjižnico matplotlib
import random
import matplotlib.pyplot as plt

PONOVITVE = 100_000

# Inicializiramo frekvence za 6 strani kocke
frequency = [0] * 6

# Simuliramo mete kocke
for _ in range(PONOVITVE):
    frequency[random.randint(0, 5)] += 1

# Pretvorimo v relativne frekvence (opcijsko)
relative_frequency = [f / PONOVITVE for f in frequency]

# Narišemo stolpčni graf
faces = [1, 2, 3, 4, 5, 6]
plt.bar(faces, relative_frequency, color="skyblue", edgecolor="black")
plt.xlabel("Število na kocki")
plt.ylabel("Relativna frekvenca")
plt.title(f"Porazdelitev metov kocke ({PONOVITVE} ponovitev)")
plt.show()

