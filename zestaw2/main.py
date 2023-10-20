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

if __name__ == "__main__":
    # Zadanie 2.10
    line = """Napis wielowierszowy,
    ciekawe z ilu wyrazow sie sklada,
    pewnie z pietnastu. Sprawdzmy to
    funkcja ex2_10()"""
    print(f"Zadanie 2.10, ilosc wyrazow w napisie wielowierszowym: {ex2_10(line)}")

    # Zadanie 2.11
    word = "slowo"
    print(f"Zadanie 2.11, slowo z podkresleniami: {ex2_11(word)}")

    # Zadanie 2.12


    # Zadanie 2.13


    # Zadanie 2.14


    # Zadanie 2.15


    # Zadanie 2.16


    # Zadanie 2.17


    # Zadanie 2.18


    # Zadanie 2.19

