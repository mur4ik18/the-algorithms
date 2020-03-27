# Задача: найти НОД(наибольший общий делитель) натуральных чисел a и b.
# Ввод: a, b ∈ N.


def Euclidean_algorithm(a:int,b:int):
    while (a != 0) and (b != 0):
        if a < b:
            a,b = b,a
        a %= b
    print(a + b)
    return a + b

x = int(input('the first num : '))
y = int(input('the second num : '))
Euclidean_algorithm(x,y)