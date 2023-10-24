def is_whitespace(c):
    return ((ord(c) > 8 and ord(c) < 14) or ord(c) == 32)

# def ex2_10(line):
#     word_count = 0
#     word = False

#     for i, c in enumerate(line):
#         if is_whitespace(c) or i == len(line) - 1:
#             if word:
#                 word_count += 1
#                 word = False
#         else:
#             word = True

#     return word_count

def ex2_10(line):
    return len(line.split())

def ex2_11(word):
    return "_".join(word)
    # print(*word, sep="_") - alternatywne rozwiazanie

def ex2_12(line, last_chars=False):
    return "".join(word[len(word)-1 if last_chars else 0] for word in line.split())

def ex2_13(line):
    return sum(len(word) for word in line.split())

def ex2_14(line):
    # max = ""
    # for word in line.split():
    #     if (len(word) > len(max)):
    #         max = word
    # return max
    return max(line.split(), key=len)
    # return sum(1 for char in line if not char.isspace()) - alternatywne rozwiazanie

def ex2_15(ints):
    # return "".join(map(str, ints))
    return "".join(str(x) for x in ints)

def ex2_16(line, old_str, new_str):
    return line.replace(old_str, new_str)

def ex2_17(line, sort_option):
    options = ["alph", "len"]
    if sort_option not in options:
        raise ValueError("Invalid option. Choose one of: %s", options)
    return sorted(line.split(), key=lambda word: word[0]) if sort_option == options[0] \
        else sorted(line.split(), key=lambda word: len(word.strip(",.")))

def ex2_18(x):
    return str(x).count("0")
    # return sum(x == "0" for x in str(number)) - alt. rozw.

def ex2_19(ints):
    return " ".join(str(x).zfill(3) for x in ints)

if __name__ == "__main__":
    # Zadanie 2.10
    line_ = """Napis wielowierszowy,
    ciekawe z ilu wyrazow sie sklada,
    pewnie z pietnastu. Sprawdzmy to
    funkcja ex2_10()"""
    print(f"Zadanie 2.10, ilosc wyrazow w napisie wielowierszowym: {ex2_10(line_)}")

    # Zadanie 2.11
    word = "slowo"
    print(f"Zadanie 2.11, slowo z podkresleniami: {ex2_11(word)}")

    # Zadanie 2.12
    print(f"Zadanie 2.12 - wyraz z pierwszych znakow wiersza line: {ex2_12(line_)}")
    print(f"Zadanie 2.12 - wyraz z ostatnich znakow wiersza line: {ex2_12(line_, True)}")

    # Zadanie 2.13
    line = "to jest napis do zadania 2.13 i 2.14, GvR."
    print(f"Zadanie 2.13 - laczna dlugosc wyrazow wynosi: {ex2_13(line)}")
    
    # Zadanie 2.14
    x = ex2_14(line)
    print(f"Zadanie 2.14 - najdluzszy wyraz: {x}, dlugosc: {len(x)}")
    
    # Zadanie 2.15
    int_list = [1, 2, 6, 7, 3, 4, 9, 0]
    print(f"Zadanie 2.15 - napis z cyfr: {ex2_15(int_list)}")
    
    # Zadanie 2.16
    old_str = "GvR"
    new_str = "Guido van Rossum"
    print(f"Zadanie 2.16 - zamiana ciagu znakow: {ex2_16(line, old_str, new_str)}")
    
    # Zadanie 2.17
    print(f"Zadanie 2.17 - sortowanie wyrazow alfabetycznie: {ex2_17(line, 'alph')}")
    print(f"Zadanie 2.17 - sortowanie wyrazow pod wzgledem dlugosci: {ex2_17(line, 'len')}")
    
    # Zadanie 2.18
    y = 3008301040990
    print(f"Zadanie 2.18 - liczba zer w liczbie {y}: {ex2_18(y)}")
    
    # Zadanie 2.19
    int_list_2 = [1, 34, 555, 31, 89, 345, 212, 12, 10]
    print(f"Zadanie 2.19 - trzycyfrowe bloki: {ex2_19(int_list_2)}")
