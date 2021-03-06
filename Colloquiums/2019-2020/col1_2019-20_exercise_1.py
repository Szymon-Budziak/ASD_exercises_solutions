# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T), która sortuje elementy tablicy T od najładniejszych do najmniej ładnych.
# Użyty algorytm powinien być możliwie jak najszybszy.Proszę w rozwiązaniu umieścić 1-2 zdaniowy
# opis algorytmu oraz proszę oszacować jego złożoność czasową.


def convert_number(number):
    B = [0]*10
    single = 0
    multiple = 9
    copy = number
    while number > 0:
        digit = number % 10
        B[digit] += 1
        number //= 10
    for i in range(10):
        if B[i] > 1:
            multiple -= 1
        elif B[i] == 1:
            single += 1
    value = 10*single+multiple
    return (value, copy)


def counting_sort(T, k):
    C = [0]*len(T)
    B = [0]*10
    for i in range(len(T)):
        index = T[i][0]/k
        B[int(index % 10)] += 1
    for i in range(1, 10):
        B[i] += B[i-1]
    j = len(T)-1
    while j >= 0:
        index = T[j][0]/k
        C[B[int(index % 10)]-1] = T[j]
        B[int(index % 10)] -= 1
        j -= 1
    for i in range(len(T)):
        T[i] = C[i]


def radix_sort(T):
    maximum = 0
    for i in range(len(T)):
        maximum = max(maximum, T[i][0])
    i = 1
    while maximum/i > 0:
        counting_sort(T, i)
        i *= 10


def pretty_sort(T):
    A = []
    for i in range(len(T)):
        A.append(convert_number(T[i]))
    # We go through the array nd convert number. If length of number is k
    # the complexity of this operation is O(k*n)
    radix_sort(A)
    # Radix sort has the complexity of O(k*n) where k is the number of
    # digits of a number
    for i in range(len(T)):
        T[i] = A[-1-i][1]
    # We go through the array and replace element of original array with
    # the element from additional A list
    # Total complexity of algorithm should be O(n*k) + O(n)
    return T


T = [123, 455, 1266, 114577, 2344, 6733]
print(pretty_sort(T))
