import math
import matplotlib.pyplot as plt
import numpy as np
# Grupo 8
# ----------------------------------
#  - Diogo Duarte
#  - Jorás Custodio
# ----------------------------------

# Comprimento: 175 mm
# Seção transversal: Circular
# Coeficiente de Convecção: 20 [W/mK]

# ----------------------------------
#Dados
# ----------------------------------

l = 0.175 # Comprimento - metros
d = 0.024 # Diâmetro - metros
p = math.pi*d # Perímetro - metros
raio = d/2
area_t = (math.pi*(d**2))/4 # Área transversal - metros^2
area_s = (2*math.pi*raio*l) + area_t #Área superfície 
k_al = 240 # W/mK - Aluminio
temp_amb =  298.15     # Temperatura do ambiente - Kelvin
temp_b = 373.15    # temperatura da superficie - Kelvin
h = 20 # Coeficiente de convecção - W/m^2 K

# # ----------------------------------
# #Parâmetros calculados
# # ----------------------------------

m = math.sqrt((h*p)/(k_al*area_t)) #m^-1
delta_temp = temp_b - temp_amb
theta_b = math.cosh(m*l) + (h/(m*k_al)) * math.sinh(m*l)
emezao = theta_b*math.sqrt(h*p*k_al*area_t)
taxa_trans_max = h*area_s*theta_b
# cosh = math.cosh(m*l)
# senh = math.sinh(m*l)

# ----------------------------------
#Temperatura na extremidade da aleta
# ----------------------------------

upper = math.cosh(m*(l-l)) + (h/(m*k_al)) * math.sinh(m*(l-l))

result = upper/theta_b

temp_extremidade = result * delta_temp + temp_amb

print("A temperatura na extremidade da aleta é: %f" %(temp_extremidade))

# ----------------------------------
# Construção do gráfico ao longo do comprimento da aleta
# ----------------------------------

lista_dist = np.arange(0.001, 0.176, 0.001)
lista_temp = []

for i in (lista_dist):
    upper = math.cosh(m*(l-i)) + (h/(m*k_al)) * math.sinh(m*(l-i))
    lower = math.cosh(m*l) + (h/(m*k_al)) * math.sinh(m*l)
    result = upper/lower

    temp_ponto = result * delta_temp + temp_amb
    lista_temp.append(temp_ponto)

plt.plot(lista_dist, lista_temp)
plt.title('Gráfico de distribuição de temperatura ao longo do comprimento da aleta')
plt.xlabel('Distância em Metros (m)')
plt.ylabel('Temperatura em Kelvin (K)')
plt.grid()
plt.show()

# ----------------------------------
# Taxa de transferência de calor
# ----------------------------------

a_1 = math.sinh(m*l) + (h/(m*k_al)) * math.cosh(m*l)
a_2 = math.cosh(m*l) + (h/(m*k_al)) * math.sinh(m*l)

taxa_trans = emezao*(a_1/a_2)

print("A taxa de transferência de calor é: %f" %(taxa_trans))

# ----------------------------------
# Eficiência da aleta
# ----------------------------------

eficencia = taxa_trans/(taxa_trans_max)
print("A eficiência é de: %f" %(eficencia))

# ----------------------------------
# Efetividade da aleta
# ----------------------------------

efetividade = taxa_trans/(h*area_t*theta_b)
print("A efetividade é de: %f" %(efetividade))

# ----------------------------------
# Taxa de transferência de calor em aleta infinita
# ----------------------------------

print("A taxa de transferência de calor em aleta infinita é: %f" %(emezao))

# ----------------------------------
# Comparação da taxa de transferência de calor em aleta finita com a de aleta infinita
# ----------------------------------

# R: A taxa de transferência de calor com o método da aleta infinita é 1.7 vezes maior
#    do que a taxa de transferência de calor com o método da aleta finita. 

# # ----------------------------------
# # Qual deveria ser o comprimento da aleta para que a hipótese da aleta infinita forneça uma medida precisa?
# # ----------------------------------
# considerando que com a hipotese da aleta infinta, temp_base = temp_ambiente
# entao, podemos considerar a troca de calor como adiabatica
# para a troca adiabatica, q_a = M * tanh(mc*cl)
# para a hipotese da aleta infinita, q_a = M
# igualando os termos, temos M = M * tanh(m * l)
# 1 = tanh(m * l)
# m = math.sqrt((h*p)/(k_al*area_t)) #m^-1
# m = 3.726
# 1 = tanh(3.726 * l)
# para tanh(x) = 1, x = 3 
# portanto 3.726 * l = 3
# l = 3 / 3.726
l_7 = 3/3.726

print("O comprimento L para que a hipótese da haleta infinta forneça uma medida precisa é: %f" %(l_7))



# ----------------------------------
#Determinando a condutividade termica do material desconhecido
# ----------------------------------
#
# theta/theta_b = e**(-sqrt((h*p) / (k*A))) * x

# log_e(theta/theta_b) = (-sqrt((h*p) / (k*A)) ) * x

# [log_e(theta/theta_b) / x ] = -sqrt((h*p) / (k*A))

# log_e(theta/theta_b) / x ]^2 = (h*p) / (k*A)

# k = - (h * p)/( a * [log_e( theta/theta_b ) / x ]^2 )


# ----------------------------------
#Calculando a condutividade termica do material desconhecido
# ----------------------------------

ex_2_t_a = 75 # Graus Celcius
ex_2_t_base = 100 # Graus Celcius
ex_2_t_ambiente = 25 # Graus Celcius
k_a = 240 #W/m^2 K
l = 0.175 # Comprimento - metros
d = 0.024 # Diâmetro - metros
p = math.pi*d # Perímetro - metros
raio = d/2
area_t = (math.pi*(d**2))/4 # Área transversal - metros^2
area_s = (2*math.pi*raio*l) + area_t #Área superfície 
h = 20 # Coeficiente de convecção - W/m^2 K

ex_2_theta = ex_2_t_a  - ex_2_t_ambiente
ex_2_theta_base = ex_2_t_base - ex_2_t_ambiente

div = ex_2_theta / ex_2_theta_base

hp = h * p
log_e = math.log(div)

#calculando x

sqrt = math.sqrt((h * p) / (k_a * area_t))
x = log_e / (-sqrt)
nominador = - h*p 
denominador  = ((log_e)/ x) ** 2


k = nominador / ( area_t * denominador)

print(k)

