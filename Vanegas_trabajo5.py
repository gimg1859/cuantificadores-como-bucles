def proposicion():
    x=-100
    y=-100
    z=-100
    sum1=0
    sum2=0
    for x in range (100):
        for y in range (100):
            for z in range (100):
                sum1=(x+y)+z
                sum2=x+(y+z)
                print('sum1 ',sum1,' sum2 ',sum2,' x y z',x,y,z)
    suma=bool(sum1 and sum2)
    return suma



#Main

resultado=proposicion()

print(resultado)
