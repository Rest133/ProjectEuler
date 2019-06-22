# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

find_num = 285341394
max_prime_divider = 1
running = True
i = 1

while running:
    print("Делим число {0} на {1} ".format(find_num, max_prime_divider))

    if find_num % i == 0:
        max_prime_divider = i
        find_num //= i

    i += 1
    if find_num == 1:
        running = False

print("Максимальный делитель равен", max_prime_divider)  # Почему это работает?
