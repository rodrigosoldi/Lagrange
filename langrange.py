#Desenvolvido por:
# Rodrigo Soldi - 41344391
# Kaique Pantosi Damato - 41326040
# Emannuel - 41330056

import matplotlib.pyplot as mat

def lagrange(points, x):
    #para cada ponto
    l = []
    for i in range(len(points)):
        num = 1
        den = 1
        for k in range(len(points)):
            if i != k:
                num *= x - points[k][0]
                den *= points[i][0] - points[k][0]

        if den != 0:
            l += [points[i][1] * num / den]

    return sum(l)

points = [(-1, 0), (0, -1), (1, 0)]

x_list = range(-20, 20)
y_list = [lagrange(points, x) for x in range(-20, 20)]

mat.plot(x_list, y_list)
mat.grid(True)
mat.show()
