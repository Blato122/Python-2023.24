#import time

# def roman2int(roman):
#     keys = ["I", "V", "X", "L", "C", "D", "M"]
#     values = [1, 5, 10, 50, 100, 500, 1000]
#     D = dict(zip(keys, values))
#
#     # wersja 1
#     # curr_val = D[roman[0]]
#     # sum = 0
#     # for next in roman[1:]:
#     #     next_val = D[next]
#     #     if curr_val >= next_val:
#     #         sum += curr_val
#     #     else:
#     #         sum -= curr_val
#     #     curr_val = next_val
#     #
#     # sum += next_val
#     # return sum
#
#     # wersja 2
#     sum = 0
#     for r, next_r in zip(roman, roman[1:]):
#         val = D[r]
#         next_val = D[next_r]
#         if val >= next_val:
#             sum += val
#         else:
#             sum -= val
#
#     sum += next_val
#     return sum
    
def roman2int_v2(roman):
    D = {"I": 1, "V" : 5, "X": 10,
         "L" : 50, "C": 100, "M" : 1000}
    values = [D[char] for char in roman]

    # wersja 3
    # sum = 0
    # for current, next in zip(values, values[1:]):
    #     if current >= next:
    #         sum += current
    #     else:
    #         sum -= current
    #
    # sum += next
    # return sum

    # wersja 4
    return sum(current if current >= next else -current for
               current, next in zip(values, values[1:])) + values[-1]

def ex3_9(seq_list):
    return list(sum(seq) for seq in seq_list)

def ex3_8_1(seq1, seq2):
    return set(seq1).union(seq2)

def ex3_8_2(seq1, seq2):
    return set(seq1).intersection(seq2)

def ex3_6(height, width):
    vertical = "   |"
    horizontal = "---+"
    full_h = "+" + horizontal * width + "\n"
    full_v = "|" + vertical * width + "\n"
    return height * (full_h + full_v) + full_h

def ex3_5(length):
    section = "....|"
    section_len = len(section)
    full = "|" + length * section
    numbers = "0" + "".join((" " * (section_len - len(str_x := str(x)))) + str_x
                      for x in range(1, length + 1))
    return full + "\n" + numbers

def is_float(string):
    try: 
        float(string)
        return True
    except ValueError:
        return False

def ex3_4():
    while True:
        x = input("Podaj liczbe: ")
        if is_float(x):
            print(f"Trzecia potega: {float(x)**3}")
        elif x == "stop":
            break
        else:
            print("Niepoprawne wejscie - podaj liczbe")

def ex3_3():
    list = []
    for x in range(31):
        if x % 3 == 0:
            continue
        else:
            list.append(str(x))
    return ", ".join(list)



if __name__ == "__main__":
    # Zadanie 3.10
    roman = "CMLXVI"   # 966
    print(f"Zadanie 3.10 - zamiana na liczby arabskie: {roman2int_v2(roman)}")
    
    # Zadanie 3.9
    seq_list = [[], [4], (1,2), [3,4], (5,6,7)]
    print(f"Zadanie 3.9 - lista sum liczb z sekwencji: {ex3_9(seq_list)}")
    
    # Zadanie 3.8
    seq1 = "aabbcc"
    seq2 = "aabbccddefgh"
    print(f"Zadanie 3.8 - wszystkie elementy z obu sekwencji (bez powtorzen): {ex3_8_1(seq1, seq2)}")
    print(f"Zadanie 3.8 - powtarzajace sie elementy z obu sekwencji (bez powtorzen): {ex3_8_2(seq1, seq2)}")
    
    # Zadanie 3.6
    height, width = 10, 20
    print(f"Zadanie 3.6 - prostokat: \n{ex3_6(height, width)}")
    
    # Zadanie 3.5
    length = 16
    print(f"Zadanie 3.5 - miarka: \n{ex3_5(length)}")
    
    # Zadanie 3.3
    print(f"Zadanie 3.3 - liczby od 0 do 30 z wyjatkiem podzielnych przez 3: {ex3_3()}")

    # Zadanie 3.4
    print(f"Zadanie 3.4 - petla liczaca trzecie potegi liczb:")
    ex3_4()

# Zadanie 3.1
# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

    # x = 2; y = 3;
    # if (x > y):
    #     result = x;
    # else:
    #     result = y;
    # poprawny, choc zwykle w pythonie nie stawiamy srednikow, a if nie wymaga nawiasow

    # for i in "axby": if ord(i) < 100: print (i)
    # niepoprawny - if ord(i) < 100: print (i) nie jest instrukcja prosta, wiec trzeba
    # te czesc kodu przeniesc do kolejnej linii i zrobic wciecie

    #for i in "axby": print (ord(i) if ord(i) < 100 else i)
    # poprawny - print() to instrukcja prosta, przez co przeniesienie tej czesci kodu
    # do nastepnej linii ze wcieciem nie jest konieczne

# Zadanie 3.2
# Co jest złego w kodzie:

    # L = [3, 5, 4] ; L = L.sort()
    # metoda sort() zwraca None, wiec w ten sposob pozbedziemy sie zawartosci listy L,
    # zmaiast ja posortowac

    # x, y = 1, 2, 3
    # zbyt wiele wartosci (3) do przypisania do 2 zmiennych

    # X = 1, 2, 3 ; X[1] = 4
    # X to krotka (inny zapis: X = (1,2,3)), a krotki sa immutable (nie mozna ich modyfikowac)
    # nie mozemy zatem zmienic w krotce 2 na 4

    #X = [1, 2, 3] ; X[3] = 4
    # co prawda tutaj X jest lista, ktora juz mozna modyfikowac, ale indeks 3 wykracza
    # poza jej rozmiar

    # X = "abc" ; X.append("d")
    # string nie ma metody append, zamiast tego mozemy uzyc np. +

    # L = list(map(pow, range(8)))
    # brakuje kolejnego argumentu funkcji map(), bedacego drugim argumentem dla pow()
    # trzeba tam podac potegi, do ktorych chcemy podniesz liczby z range(8)
