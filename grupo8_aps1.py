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
d = 0.24 # Diâmetro - metros
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
# delta_temp = temp_b - temp_amb
# theta_b = math.cosh(m*l) + (h/(m*k_al)) * math.sinh(m*l)
# emezao = theta_b*math.sqrt(h*p*k_al*area_t)
# taxa_trans_max = h*area_s*theta_b
# # cosh = math.cosh(m*l)
# # senh = math.sinh(m*l)

# # ----------------------------------
# #Temperatura na extremidade da aleta
# # ----------------------------------

# upper = math.cosh(m*(l-l)) + (h/(m*k_al)) * math.sinh(m*(l-l))

# result = upper/theta_b

# temp_extremidade = result * delta_temp + temp_amb

# print("A temperatura na extremidade da aleta é: %f" %(temp_extremidade))

# # ----------------------------------
# # Construção do gráfico ao longo do comprimento da aleta
# # ----------------------------------

# lista_dist = np.arange(0.001, 0.176, 0.001)
# lista_temp = []

# for i in (lista_dist):
#     upper = math.cosh(m*(l-i)) + (h/(m*k_al)) * math.sinh(m*(l-i))
#     lower = math.cosh(m*l) + (h/(m*k_al)) * math.sinh(m*l)
#     result = upper/lower

#     temp_ponto = result * delta_temp + temp_amb
#     lista_temp.append(temp_ponto)

# plt.plot(lista_dist, lista_temp)
# plt.title('Gráfico de distribuição de temperatura ao longo do comprimento da aleta')
# plt.xlabel('Distância em Metros (m)')
# plt.ylabel('Temperatura em Kelvin (K)')
# plt.grid()
# plt.show()

# # ----------------------------------
# # Taxa de transferência de calor
# # ----------------------------------

# a_1 = math.sinh(m*l) + (h/(m*k_al)) * math.cosh(m*l)
# a_2 = math.cosh(m*l) + (h/(m*k_al)) * math.sinh(m*l)

# taxa_trans = emezao*(a_1/a_2)

# print("A taxa de transferência de calor é: %f" %(taxa_trans))

# # ----------------------------------
# # Eficiência da aleta
# # ----------------------------------

# eficencia = taxa_trans/(taxa_trans_max)
# print("A eficiência é de: %f" %(eficencia))

# # ----------------------------------
# # Efetividade da aleta
# # ----------------------------------

# efetividade = taxa_trans/(h*area_t*theta_b)
# print("A efetividade é de: %f" %(efetividade))

# # ----------------------------------
# # Taxa de transferência de calor em aleta infinita
# # ----------------------------------

# print("A taxa de transferência de calor em aleta infinita é: %f" %(emezao))

# # ----------------------------------
# # Comparação da taxa de transferência de calor em aleta finita com a de aleta infinita
# # ----------------------------------

# # R:

# # ----------------------------------
# # Qual deveria ser o comprimento da aleta para que a hipótese da aleta infinita forneça uma medida precisa?
# # ----------------------------------

# M = 13.25

# emezao = theta_b*math.sqrt(h*p*k_al*area_t)

resultado_analise1 = math.sqrt(h*p*k_al*area_t) # Resultado = 12.79
theta_b_esperado = 13.25/12.79 # Resultado = 1.03

# theta_b = math.cosh(m*l) + (h/(m*k_al)) * math.sinh(m*l)
# 1.03/math.sinh(m*l) = math.cosh(m*l) + (h/(m*k_al))

var_analise = (h/(m*k_al)) # Resultado = 0.07
print(var_analise)

# (1.03/math.sinh(m*l)) - 0.07 = math.cosh(m*l)
# 1.03 - (0.07 * math.sinh(m*l)) /math.sinh(m*l) = math.cosh(m*l)
# 1.03 - (0.07 * math.sinh(m*l)) = math.cosh(m*l) * math.sinh(m*l)

#Continuação (Dúvida de como faz essa conta)


