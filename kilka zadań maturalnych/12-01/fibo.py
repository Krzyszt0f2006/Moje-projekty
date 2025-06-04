def fibonacci_sumy(n):
    if n <= 0:
        return 0

    a, b = 0, 1
    suma = 0
    for i in range(n):
        suma += b
        a, b = b, a + b
    return suma

def perimeter(n):
    wynik=(fibonacci_sumy(n+1)*4)
    return wynik
