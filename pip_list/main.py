from pip._vendor import pkg_resources

t = input(': ')
_package_name = t
_package = pkg_resources.working_set.by_key[_package_name]

out1 = 'digraph G {'

out3 = '}'
L = []
print(out1)
for el in range(len(_package.requires())):
    print(t, '->', "\"", _package.requires()[el], "\"")
print(out3)
