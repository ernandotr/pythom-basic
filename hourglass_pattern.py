def hourglass_pattern(n):
    for i in range(n):
        print(' ' * i + '*' * (2 * (n - i) - 1))
    for i in range(n - 2, -1, -1):
        print(' ' * i + '*' * (2 * (n - i) - 1))
hourglass_pattern(5)