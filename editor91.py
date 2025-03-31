import random

n = []
a = {}
while True:
    n = input()

    if '52' in n and ' = ' in n:
        if n.index('=') == 2:
            i = n.split(' = ')
            a[i[0]] = int(n[7:-1])
          
        continue
    if '42' in n and ' = ' in n:
        if n.index('=') == 2:
            i = n.split(' = ')
            a[i[0]] = n[7:-1]

        continue
    if 'bull' in n and ' = ' in n:
        if n.index('=') == 2:
            i = n.split(' = ')
            a[i[0]] = bool(n[9:-1])

        continue
    if 'ludoman' in n and ' = ' in n:
        if n.index('=') == 2:
            i = n.split(' = ')
            a[i[0]] = random.randint(0, int(n[12:-1]))

        continue
    if 'Minecraft' in n and ' = ' in n:
        if n.index('=') == 2:
            i = n.split(' = ')
            a[i[0]] = float(n[14:-1])

        continue
    if 'Dota2' in n:

        for i in a.keys():
            if i in n:
                n = n.replace(n[6:-1], str(a[i]))
                break
        n = n.replace('Dota2', 'print')
        exec(n)
    if ' += ' in n:
        if n[0] in a:
            a[n[0]] = a[n[0]] + int(n[5:])

    if ' -= ' in n:
        if n[0] in a:
            a[n[0]] = a[n[0]] - int(n[5:])

    if ' *= ' in n:
        if n[0] in a:
            a[n[0]] = a[n[0]] * int(n[5:])

    if ' %= ' in n:
        if n[0] in a:
            a[n[0]] = a[n[0]] % int(n[5:])

    if ' /= ' in n:
        if n[0] in a:
            a[n[0]] = a[n[0]] / int(n[5:])

    if ' //= ' in n:
        if n[0] in a:
            a[n[0]] = a[n[0]] // int(n[5:])








