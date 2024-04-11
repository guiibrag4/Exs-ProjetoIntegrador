import os

def arquivo_dividido (nome, linhas):
    with open (nome, 'r') as arquivoOrigem:
        cabecalho = arquivoOrigem.readline()

        cont = 0
        fileNumber = 1
        fileDestiny = None

        for linha in arquivoOrigem:
            if cont % linhas == 0:
                if fileDestiny:
                    fileDestiny.close()
                nameDestinyFile = f"{os.path.splitext(nome)[0]}_{fileNumber}.txt"
                fileDestiny = open (nameDestinyFile, 'w')
                if cabecalho:
                    fileDestiny.write(cabecalho)
                fileNumber += 1
            fileDestiny.write(linha)
            cont += 1
        
        if fileDestiny:
            fileDestiny.close()

nameFile = input ("Enter with the name of origin file: ")
rollsFile = int(input("Quant of rols of file: "))

arquivo_dividido(nameFile, rollsFile)
print ("Arquivo dividido com sucesso!!!!!!!!!!!")
