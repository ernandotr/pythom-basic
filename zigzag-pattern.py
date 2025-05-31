n = 13
for i in range(1, 4):
    for j in range(1, n + 1):
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()