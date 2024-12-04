import random
pole = [48, 95, 21, 3, 35, 66, 69, 41, 33, 99]

def bubble_sort():
    n = len(pole)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if pole[j] > pole[j+1] :
                pole[j], pole[j+1] = pole[j+1],pole[j]
            print(pole)
    return pole

print(bubble_sort())

arrayy = [-15, 54, 23, -69, 13, -89, 74, 7, 8, 15]

def is_sorted(arrayy):
    for i in range(1, len(arrayy)):
        if arrayy[i] < arrayy[i-1]:
            return False
    return True

def bogosort(arrayy):
    count = 0
    while not is_sorted(arrayy):
        random.shuffle(arrayy)
        count += 1
        print(f"Pokus {count}: {arrayy}")
    print(f"Seznam seřazen po {count} pokusech.")
    return arrayy

print("Bogo sort:", bogosort(arrayy))