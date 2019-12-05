import os
arquivos = os.listdir('C:/Users/Sheilla.CONTAGIL2/Documents/Arquivos ReceitanetBX - Copia')
matriz = []
count = 0
array =  arquivos[0].split('-')
el = array[0]

for i in range(len(arquivos)):
    array = arquivos[i].split('-')
    
    if(i+1) == len(arquivos):
        count+=1
        matriz.append([el, count])
        
    if el == array[0]:
        count+=1
        
    else:
        count+= 1
        matriz.append([el, count])
        el = array[0]
        count = 0

print('Cnpjs baixados: ', len(matriz))
for el in matriz:
    print(el)

print('Quantidade de arquivos: ', len(arquivos))

count=0
for el in matriz:
    print(el[0])
    count+=el[1]
    
print('Soma de notas: ', count)

#print(matriz)
