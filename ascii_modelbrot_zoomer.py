for y in range(-20, 20):
    line = ""
    for x in range(-40, 40):
        z = complex(x/20, y/20)
        c = 0
        for i in range(100):
            c = c**2 + z
            if abs(c) > 2:
                line += "*"
                break
        else:
            line += " "
    print(line)