import math

def square(side):
    area = side * side
    return math.ceil(area)

print(square(5))      # ожидается 25 (целая сторона)
print(square(5.1))    # ожидается 27 (5.1 * 5.1 = 26.01 → ceil до 27)
print(square(2.3))    # ожидается 6 (2.3 * 2.3 = 5.29 → ceil до 6)
#коммит для Pull Reguest