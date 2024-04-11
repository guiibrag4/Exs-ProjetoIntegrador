nome_arquivo = input("Entre com o nome do arquivo:")

soma = 0

with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        soma += sum(int(num) for num in linha.split())
    
print("A soma dos números no arquivo é:", soma)

# O with é usado quando existem operações que precisam de algum tipo de finalização após serem concluidas. É uma boa prática me python, pois nesse código ele garante que o arquivo será fechado assim que sair do bloco with. O open serve para abrir o arquivo. 

# Caso o código fosse "arquivo =  open(nome_arquivo, "r")", ele precisaria ser fechado explicitamente depois do bloco, com "arquivo.close()"