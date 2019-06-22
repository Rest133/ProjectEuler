# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов
# будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

full_sum = 0
maxNumber = 4000000
running = True
i = 1  # next number
j = 0  # previously number

while running:
    temp = i
    i += j
    j = temp

    s = i + j
    if s % 2 == 0:
        full_sum += s
        print("i + j =", s)
        print("Full sum =", full_sum)

    if i >= maxNumber:
        running = False

print("End of program")
