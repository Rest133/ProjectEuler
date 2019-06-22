# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.


def find_palindrome(num):
    reversed_number = 0
    while num != 0:
        reversed_number += num % 10
        num //= 10
        reversed_number *= 10

    return reversed_number // 10


max_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        reversed_num = find_palindrome(number)
        if reversed_num == number and reversed_num > max_palindrome:
            max_palindrome = reversed_num

print("Max palindrome =", max_palindrome)
print("Program end.")
