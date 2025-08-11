import random
import math

FACTOR = 100000000 # Nastavi natančnost
PONOVITVE = 1000000 # To tudi poveča natančnost

radij = 2*FACTOR

točke = [[random.randrange(-radij, radij+1), random.randrange(-radij, radij+1)] for _ in range(PONOVITVE)]

delež = 0
for točka in točke:
    if radij >= math.sqrt(abs(točka[0])**2 + abs(točka[1])**2):
        delež += 1

print(4*delež/PONOVITVE)

