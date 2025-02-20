def omelete():
    ovos = 12 # variável local de omelete
    print('Ovos = ', ovos)
def bacon ():
    ovos = 6 # variável local de bacon
    print('Ovos = ', ovos)
    omelete()
    print('Ovos = ', ovos)
ovos = 2
bacon()
print('Ovos = ', ovos)