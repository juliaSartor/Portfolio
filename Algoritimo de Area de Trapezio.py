#Escreva um algoritimo que calcule a área de um trapézio

Alt = int(input('Qual a altura do trapézio?:'))
BaseM = int(input('Qual a medida da base maior do trapézio?:'))
BaseN = int(input('Qual a medida da base menor do trapézio?:'))
Area = ((BaseM+BaseN)*Alt)/2
print(f'A área total do trapézio é: {Area}')
