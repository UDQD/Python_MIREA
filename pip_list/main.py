import requests as rq

L = []


def normalize(s):
    if ' ' in s:
        s = s[:s.index(' ')]
    if '[' in s:
        s = s[:s.index('[')]
    if ';' in s:
        s = s[:s.index(';')]

    return s


def chek(pac):
    try:
        url = 'https://pypi.org/pypi/' + pac + '/json'
        json = rq.get(url).json()
        m = json['info']['requires_dist']

        if m != None:
            for el in m:
                el = normalize(el)
                print("\"" + pac + "\"" + '<-' + "\"" + el + "\"")
                if el not in L:
                    L.append(el)
                    chek(el)

    except Exception as ex:
        print(' ! чет пошло не так ! ', ex, "pac = ", pac)


zn = input(': ')
print('digraph G {')
chek(zn)
print('}')
