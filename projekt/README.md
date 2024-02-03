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

### Opis poszczególnych plików, klas i metod:
* disjoint_sets.py - **DisjointSets** - klasa reprezentująca strukturę zbiorów rozłącznych. Przechowuje ona
podział danego zbioru na mniejsze, rozłączne zbiory. Zawiera dwie funkcje: join() łączy dwa zbiory w jeden,
a find() zwraca zbiór, do którego należy wybrany element.
* disjoint_sets.py - **Node** - klasa pomocnicza dla klasy DisjointSets.
* graph.py - **Graph** - klasa reprezentująca graf. Zawiera wymiary grafu (liczbę kolumn i wierszy - cols i rows), jego rozmiar (liczbę wierzchołków - size) oraz listę krawędzi - G. Funkcja generate_edges() dodaje do grafu pionowe i poziome połączenia między wierzchołkami (za pomocą pomocniczej funkcji add_edge()), tak, aby powstała prostokątna siatka. Funkcja kruskal() zwraca drzewo (również obiekt klasy Graph), z którego następnie, w klasie Maze, może zostać utworzony labirynt.
* maze.py - **Maze** - klasa reprezentująca labirynt. Konstruktor przyjmuje jedynie drzewo utworzone przez funkcję kruskal(). Funkcja draw() tworzy graficzną reprezentację labiryntu. Na czarnym tle rysowane są białe komórki oraz przerwy w ścianach. W wyniku powstaje labirynt, w którym są czarne ściany i biała powierzchnia do chodzenia. WALL_W określa szerokość ściany, a CELL_W szerokość komórki. Dodatkowo, losowo jest wybierane wejście i wyjście z labiryntu, tak, aby dało się go przejść od początku do końca. Labirynt można wyświetlić na ekranie za pomocą funkcji show() - grafika pojawi się w nowym okienku, jednak można ją zapisać również do pliku, podając w konsoli nazwę pliku (wraz z rozszerzeniem) pod jaką chcemy go zapisać. Dodatkowo, binarna postać drzewa jest zapisywana do pliku "save.p" za pomocą biblioteki pickle. Umożliwia ona ponowne utworzenie tego samego labiryntu, po wybraniu odpowiedniej opcji w pliku main.py.
* main.py - polecenie "python3 main.py" tworzy i rysuje labirynt o zadanej wielkości (ROWS, COLS). W przypadku wybrania opcji load = True, ładowany jest poprzedni labirynt z pliku "save.p". W przeciwnym wypadku, generowany jest nowy, losowy labirynt.
