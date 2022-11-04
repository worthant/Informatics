s = input('Введите число ')
while sum([1 for x in s if int(x) == 0 or int(x) == 1]) != 7:
    print('Введите число корректно')
else:
    s1 = s[0] + s[2] + s[4] + s[6]
    s2 = s[1] + s[2] + s[5] + s[6]
    s3 = s[3] + s[4] + s[5] + s[6]

    s_new = s1.count('1') % 2 * 1 + s2.count('1') % 2 * 2 + s3.count('1') % 2 * 4 - 1
    if s_new + 1 != 0:
        if s[s_new] == str(0):
            k = str(1)
        else:
            k = str(0)
        s = s[:s_new] + k + s[s_new + 1:]
        s = s[2] + s[4] + s[5] + s[6]
        print("Сообщение без ошибки ", s)
        print('Столбец с ошибкой', s_new + 1)
    else:
        print("Сообщение без ошибок")
