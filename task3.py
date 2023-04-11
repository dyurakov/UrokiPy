
ax = float(input("Введите x точки A: \n"))
ay = float(input("Введите y точки A: \n"))

bx = float(input("Введите x точки B: \n"))
by = float(input("Введите y точки B: \n"))

cx = float(input("Введите x точки C: \n"))
cy = float(input("Введите y точки C: \n"))



def rasstoyanie(v1x,v1y,v2x,v2y):
    return ((v2x-v1x)**2+(v2y-v1y)**2)**0.5

AC = rasstoyanie(ax,ay,cx,cy)
BC = rasstoyanie(bx,by,cx,cy)

print(f'Длина отрезка AB {AC}')
print(f'Длина отрезка BC {BC}')

print(f'Сумма длин отрезков AC и BC: {AC+BC}')