def factorial(n):
    assert n >= 0 

    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def fibonacci(n):
    assert n > 0

    a = 0
    b = 1

    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(3, n + 1):
            res = a + b
            a = b
            b = res
    return res

def reverse_iter(L, left=0, right=None):
    right = right or len(L)-1

    while left < right:
        print(L)
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

# L[::-1]

def reverse_recursive(L, left=0, right=None):
    right = right or len(L)-1
    
    if left >= right:
        return
    
    print(L)
    L[left], L[right] = L[right], L[left]
    reverse_recursive(L, left + 1, right - 1)

# def rev(L):
#     if len(L) == 0: 
#         return []
#     return [L[-1]] + rev(L[:-1])

def reverse(L, left=0, right=None):
    right = right or len(L)-1

    if left >= right:
        return
    
    return L[:left] + list(reversed(L[left:right+1])) + L[right+1:]

def sum_seq(sequence):
    return sum(sum_seq(item) if (isinstance(item, (list, tuple))) else item 
               for item in sequence)

def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def make_grid(height, width):
    vertical = "   |"
    horizontal = "---+"
    full_h = "+" + horizontal * width + "\n"
    full_v = "|" + vertical * width + "\n"
    return height * (full_h + full_v) + full_h

def make_ruler(length):
    section = "....|"
    section_len = len(section)
    full = "|" + length * section
    numbers = "0" + "".join((" " * (section_len - len(str_x := str(x)))) + str_x
                      for x in range(1, length + 1))
    return full + "\n" + numbers

if __name__ == "__main__":
    # Zadanie 4.2
    print(f"Zadanie 4.2 - linijka i siatka") # zrobione w zestawie 3
    height, width = 10, 20
    print(f"siatka: \n{make_grid(height, width)}")    
    length = 16
    print(f"miarka: \n{make_ruler(length)}")

    # Zadanie 4.3
    n = 6
    print(f"Zadanie 4.3 - silnia iteracyjna: {factorial(n)}")

    # Zadanie 4.4
    print(f"Zadanie 4.4 - fibonacci: ", end="")
    print(", ".join(str(fibonacci(m)) for m in range(1, 11)))

    # Zadanie 4.5
    L1 = [1, 2, 3, 4, 5, 6, 7]
    L2 = L1[:] # L1 = L2 = [1, 2, 3, ...] nie dziala!
    L3 = L1.copy()
    # L4 = list(L1)
    reverse_iter(L1, 1, 4)
    print(f"Zadanie 4.5 - odwracanie listy iteracyjnie: {L1}")
    reverse_recursive(L2, 1, 4)
    print(f"Zadanie 4.5 - odwracanie listy rekurencyjnie: {L2}")
    # print(f"Zadanie 4.5 - odwracanie listy sposob dodatkowy: {reverse(L3, 1, 4)}")

    # Zadanie 4.6
    seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
    print(f"Zadanie 4.6 - suma liczb w zagniezdzonych sekwencjach: {sum_seq(seq)}")

    # Zadanie 4.7
    print(f"Zadanie 4.7 - splaszczona lista elementow zagniezdzonych sekwencji: {flatten(seq)}")
