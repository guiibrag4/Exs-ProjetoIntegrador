# Soma

nome_arquivo = input("Entre com o nome do arquivo:")

soma = 0
with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        numeros = linha.split()
        for num_str in numeros:
            soma += int(num_str)

print("A soma dos números no arquivo é:", soma)

## Divisão

def dividir_arquivo(nome_arquivo, linhas_por_arquivo):
    with open(nome_arquivo, 'r') as arquivo_origem:
        cabecalho = arquivo_origem.readline()  # Preserva o cabeçalho, se houver

        contador = 0
        numero_arquivo = 1
        arquivo_destino = None

        for linha in arquivo_origem:
            if contador % linhas_por_arquivo == 0:
                if arquivo_destino:
                    arquivo_destino.close()
                nome_arquivo_destino = f"{os.path.splitext(nome_arquivo)[0]}_{numero_arquivo}.txt"
                arquivo_destino = open(nome_arquivo_destino, 'w')
                if cabecalho:
                    arquivo_destino.write(cabecalho)
                numero_arquivo += 1
            arquivo_destino.write(linha)
            contador += 1

        if arquivo_destino:
            arquivo_destino.close()

nome_arquivo = input("Entre com o nome do arquivo de origem: ")
linhas_por_arquivo = int(input("Quantidade de linhas por arquivo: "))

dividir_arquivo(nome_arquivo, linhas_por_arquivo)
print("Arquivo dividido com sucesso!")




