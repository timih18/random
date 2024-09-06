def insertion_sort(sp):
    for i in range(1, len(sp)):
        for j in range(i, 0, -1):
            if sp[j] < sp[j - 1]:
                sp[j], sp[j - 1] = sp[j - 1], sp[j]
            else:
                break
    return sp
