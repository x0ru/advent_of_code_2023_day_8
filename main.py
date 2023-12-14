import csv
import math

from icecream import ic

directions = []
h = {}

with open('file.csv') as file:
    file = csv.reader(file)
    for elements in file:
        if not directions:
            for letter in elements[0]:
                if letter == 'R':
                    directions.append(int(letter.replace('R', '1')))
                elif letter == 'L':
                    directions.append(int(letter.replace('L', '0')))
        elif elements:
            h[elements[0].split(' ')[0]] = list((elements[0].split(' ')[2].removeprefix('('),
                                                 elements[1].removesuffix(")").removeprefix(' ')))

    n = 0
    res = 0
    biggest = []
    starting = []

    for i in h.keys():
        if i[2] == 'A':
            starting.append(i)

    game = True
    kek = []
    ite = 0
    res = []
    for j in range(len(starting)):
        while ite < 1000000:
            for elements in range(len(starting)):
                starting[elements] = h[starting[elements]][directions[n]]
            if starting[j][2] == 'Z':
                kek.append(ite)
            if len(kek) == 2:
                break
            n += 1
            if n == len(directions):
                n = 0
            ite += 1
        for i in range(len(kek) - 1):
            res.append(kek[i + 1] - kek[i])
        ic(res)
        kek = []

    ic(math.lcm(*res))
