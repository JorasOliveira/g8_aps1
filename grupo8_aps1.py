import math

#somos o grupo 8
#comprimento: 175 mm
#secao transversal: circulcar
# Coeficiente de Conveccao: 20 [W/mK]
#constantes 
l = 0.3 #metros
p = 0.12 #metros
a = 0.0009 #metros^2
h = 15 #W/m^2 K
k = 240 #W/mK - Aluminio
t_inf =  298.15 #k - temperatura do ambiente
t_b = 373.15 #K - temperatura da superficie
m = math.sqrt(10) #m^-1
cosh = 1.49
senh = 1.1

upper = 1 + ((h/(m*k)) * 0) #cosh(0) == 1; senh(0) == 0 
lower = cosh + ((h/(m*k)) * senh)
f = (t_b - t_inf)
up_low = upper/lower

t_x = (f * up_low) + 300
# print(t_x)
