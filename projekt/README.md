# Temat projektu - generowanie labiryntów za pomocą algorytmu Kruskala

### Opis ogólny:
Zaczynam od stworzenia grafu o podanej przez użytkownika liczbie wierzchołków
w pionie (kolumny) i w poziomie (wiersze). Dzięki temu, graf przyjmuje "prostokątny"
kształt. Następnie, łączę sąsiadujące wierzchołki krawędziami. Krawędzie, dzięki tej
reprezentacji, są pionowe lub poziome. Otrzymujemy więc graf, który przypomina siatkę
labiryntu.

Mając "szkielet", trzeba jeszcze wygenerować sam labirynt - wykorzystuję do tego algorytm Kruskala.
z wprowadzoną pewną modyfikacją. Polega ona na tym, że kolejnych krawędzi nie wybieram od najmniejszej 
wagi, a po prostu losuję je (a właściwie to mieszam za pomocą random.shuffle()) - jest to równoznaczne 
z przydzieleniem losowych wag krawędziom, a potem wybieraniu ich zaczynając od najmniejszej wagi. To jednak
wymagałoby przechowywania dodatkowej informacji o wadze, w mojej implementacji nie jest to konieczne.

Algorytm kruskala zwraca minimalne drzewo rozpinające wcześniej utworzonego grafu, którego później
używam do stworzenia labiryntu. W jaki sposób jednak jest to drzewo związane z labiryntem? Wyobraźmy
sobie, że każdy wierzchołek grafu reprezentuje jedną komórkę labiryntu. Pomiędzy komórkami są ściany.
Aby wiedzieć, czy daną ścianę narysować, sprawdzamy, czy komórki, które miałaby ona rozdzielać, łączy
krawędź minimalnego drzewa rozpinającego. Jeśli tak - ściany nie ma, jeśli nie - ściana jest. Tak
właśnie powstaje labirynt.

### Opis poszczególnych klas i metod:
* disjoint_sets.py - **DisjointSets** - klasa reprezentująca strukturę zbiorów rozłącznych. Przechowuje ona
  podział danego zbioru na mniejsze, rozłączne zbiory. Zawiera dwie funkcje: join() łączy dwa zbiory w jeden,
  a find() zwraca zbiór, do którego należy wybrany element.
* disjoint_sets.py - **Node** - klasa pomocnicza dla klasy DisjointSets
* graph.py - **Graph** - klasa reprezentująca graf. Zawiera wymiary grafu (liczbę kolumn i wierszy)
