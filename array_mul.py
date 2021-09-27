def mul(a, b):
    c = []

    for i in range(len(a)):
        new_row = []
        for j in range(len(a[i])):
            new_row.append(a[i][j] + b[i][j])
        c.append(new_row)

    return c

