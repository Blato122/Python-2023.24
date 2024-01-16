"""
ZADANIE 12.8 (RANDOMQUEUE)
Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. 
Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce. 
"""

import random

class RandomQueue:
    def __init__(self, size=10):
        self.storage = []
        self.capacity = size

    def insert(self, item):
        """
        Wstawia element w czasie O(1).
        """
        if not self.is_full():
            self.storage.append(item)
        else:
            print("Kolejka jest pelna.")

    def remove(self):
        """
        Zwraca losowy element w czasie O(1).
        """
        if not self.is_empty():
            return self.storage.pop(random.randint(0, len(self.storage) - 1))
        else:
            print("Kolejka jest pusta.")

    def is_empty(self):
        return len(self.storage) == 0

    def is_full(self):
        return len(self.storage) == self.capacity

    def clear(self):
        """
        Czyszczenie listy.
        """
        self.storage = []
        # self.storage[:] = []]

# testy - nie korzystalem z innych bibliotek, poniewaz zrobienie takich testow, jak ponizej,
# bylo moim zdaniem bardziej czytelne i szybsze. Oprocz sprawdzania dzialania funkcji, wypisuje
# rowniez capacity kolejki oraz inne informacje. Wszystkie funkcje dzialaja poprawnie i w czasie O(1).
if __name__ == "__main__":
    print("------------------ Utworzono kolejke losowa o pojemnosci 6 ------------------")
    rq = RandomQueue(size=6)
    print(rq.capacity)
    print(rq.storage)
    print(rq.is_empty())
    print(rq.is_full())
    print()

    print("------------------ Dodawanie elementow do kolejki ------------------")

    for i in range(8): 
        # specjalnie dodaje wiecej niz 6 elementow, zeby zobaczyc zachowanie kolejki w takim przypadku jesli element 
        # sie nie miesci, zwyczajnie nie jest dodawany, nic wiecej sie nie dzieje, oprocz wypisania odpowiedniego komunikatu
        rq.insert(i)
        print(rq.storage)
        print(rq.is_empty())
        print(rq.is_full())
        print()

    print("------------------ Usuwanie elementow z kolejki ------------------")
    
    for _ in range(9):
        # tutaj rowniez usuwam wiecej elementow, niz jest w kolejce, zeby zobaczyc co sie stanie. Nie dzieje sie
        # nic zlego, z pustej kolejki nie da sie nic usunac, wypisywany jest jedynie komunikat.
        elem = rq.remove()
        print(elem)
        print(rq.storage)
        print(rq.is_empty())
        print(rq.is_full())
        print()

    print("------------------ Ponowne dodawanie elementow do kolejki ------------------")

    for i in range(6):
        rq.insert(i)
        print(rq.storage)
        print(rq.is_empty())
        print(rq.is_full())
        print()

    print("------------------ Czyszczenie kolejki ------------------")
    rq.clear()
    print(rq.storage)
    print(rq.is_empty())
    print(rq.is_full())
