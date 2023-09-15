#Faça um algoritmo que peça o ano de nascimento da pessoa, peça o ano atual e calcule a idade do usuário. 

AnoN = int(input('Que ano você nasceu?:'))
AnoA = int(input('Qual é o ano atual?:'))
Idade = AnoA-AnoN
if Idade >= 18:
 print('Você pode tirar carteira de motorista')
else:
 print('você não pode dirigir ainda')
       