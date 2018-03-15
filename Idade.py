idade = int(input())

ano = idade / 365  
mes = (idade % 365) / 30
dia = (idade % 365) % 30

print('%.0f' % ano)
print('%.0f' % mes)
print('%.0f'  % dia)

