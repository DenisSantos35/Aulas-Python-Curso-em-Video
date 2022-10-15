m = float(input('Uma distancia de metros: '))
print('A medida de {}m corresponde a'.format(m))
print('{}Km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m/1000, m/100, m/10, m*10, m*100, m*1000))
