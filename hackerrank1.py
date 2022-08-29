import math
ab=int(input())
bc=int(input())
ac=math.sqrt((ab)**2+(bc)**2)
h=ac/2.0
m=bc/2.0
d=int(round(math.degrees(math.acos(m/h))))
d=str(d)
print(d+"°")


# import math
# AB=int(input())
# BC=int(input())
# print(round(math.degrees(math.atan(AB/BC))),chr(176),sep='')