def digit_root(num):
    while num >= 10:
        digits_sum = 0

        for digit in str(num):
            digits_sum += int(digit)

        num = digits_sum

    return num


# Примеры
print(digit_root(4851))    # 9
print(digit_root(97569))   # 9
print(digit_root(889987))  # 4