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
