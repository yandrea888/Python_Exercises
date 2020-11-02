ini = True

while ini:
    res = input('Escribe algo y se contarán las vocales ')
    a = res.count('a')
    e = res.count('e')
    i = res.count('i')
    o = res.count('o')
    u = res.count('u')
    print('Tu enunciado tiene:\n', str(a),
          'a\n', str(e), 'e\n', str(i), 'i\n',
          str(o), 'o\n', str(u), 'u\n')
    a = input('Otra ves? ')
    a = ''.join(a.split())
    if a.lower().startswith('s'):
        ini = True
    else:
        ini = False