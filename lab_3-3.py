num = int(input('Введите число: '))

Words = {
    1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
    5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
    9: 'девять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
    14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',
    18: 'восемнадцать', 19: 'девятнадцать', 10: 'десять', 20: 'двадцать',
    30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
    70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто', 100: 'сто',
    200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот',
    600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот',
    1000: 'тысяча'
}

ones = num % 10
if 100 <= num < 1000:
    tens = num % 100
    flag = False
    if tens > 19:
        tens -= ones
        flag = True

    if tens in Words and ones in Words:
        if flag:
            print(' '.join((Words[num - tens - ones], Words[tens], Words[ones])))
        else:
            print(' '.join((Words[num - tens], Words[tens])))
    elif tens in Words:
        print(' '.join((Words[num - tens - ones], Words[tens])))
    elif ones in Words:
        print(' '.join((Words[num - tens - ones], Words[ones])))
    else:
        print(Words[num - tens - ones])
elif 19 < num < 100 and ones > 0:
    print(' '.join((Words[num - ones], Words[ones])))
else:
    print(Words.get(num, 'Error'))
