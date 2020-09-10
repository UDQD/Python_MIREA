from pip._vendor import pkg_resources


def srs(t):
    out = ''
    try:
        _package = pkg_resources.working_set.by_key[t.replace('-','_')]

        for el in _package.requires():
            eln = str(el)
            try:
                eln = eln[:eln.index('=') - 1]
            except ValueError:
                pass
            if '-' in eln:
                eln = eln.replace('-','_')
            print(str(t) + '->' + "\"" + eln + "\"")
            srs(eln)

        return out
    except KeyError:
        pass

pack = input(':')
print('digraph G {')
srs(pack)
print('}')
