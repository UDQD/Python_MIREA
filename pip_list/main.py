import pkg_resources


def srs(t):
    try:
        _package = pkg_resources.working_set.by_key[t.replace('-', '_')]

        for el in _package.requires():
            eln = str(el)
            try:
                eln = eln[:eln.index('=') - 1]
            except ValueError:
                pass

            eln = eln.replace('-', '_')
            print(str(t) + '->' + "\"" + eln + "\"")
            srs(eln)

    except KeyError:
        pass


pack = input(':')
print('digraph G {')
srs(pack)
print('}')
