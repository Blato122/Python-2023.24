import itertools
import random

if __name__ == "__main__":
    # Zadanie 7.6
    iter1 = itertools.cycle([0, 1])
    for i, x in enumerate(iter1):
        print(x)
        i += 1
        if (i > 100): break
    
    iter2 = (random.choice(["N", "E", "S", "W"]) for i in iter(int, 1))
    for i, x in enumerate(iter2):
        print(x)
        i += 1
        if (i > 100): break

    iter3 = itertools.cycle(range(7))
    for i, x in enumerate(iter3):
        print(x)
        i += 1
        if (i > 100): break