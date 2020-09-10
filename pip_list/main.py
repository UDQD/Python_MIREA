from pip._vendor import pkg_resources


def srs(t):
    out = ''
    try:
        _package = pkg_resources.working_set.by_key[t]

        for el in _package.requires():
            eln = str(el)
            try:
                eln = eln[:eln.index('=') - 1]
            except ValueError:
                pass
            print(str(t) + '->' + "\"" + eln + "\"")
            srs(eln)

        return out
    except KeyError:
        pass


print('digraph G {')
srs("sphinx")
print('}')
