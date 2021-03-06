# Даны числа "2, 4, 6, 8, 10". В этом списке нужно выписать все числа кратные "4" и умножить их на 2. Вывести на экран.
def modify_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 4:
            lst.remove(lst[i])
        else:
            lst[i] *= 2
    print(lst)


s = [2, 4, 6, 8, 10]
modify_list(s)  # [8, 16]

s = [2, 4, 6, 8, 12]
modify_list(s)  # [8, 16, 24]

# [4, 8, 12, 16, 20, 24, 28, 32, 36, 40] -> lst[i] *= 1
# [8, 16, 24, 32, 40, 48, 56, 64, 72, 80] -> lst[i] *= 2