
import multiprocessing
import time

def calcular_soma_parte(args):
    vetor, inicio, fim = args
    return sum(vetor[inicio:fim])

def main():
    inicio_execucao = time.time()

    vetor_grande = range(1, 1_000_000_001)

    num_processes = 2

    tamanho_parte = len(vetor_grande) // num_processes
    partes = [(vetor_grande, i * tamanho_parte, (i + 1) * tamanho_parte) for i in range(num_processes)]

    with multiprocessing.Pool(num_processes) as pool:
        resultados = pool.map(calcular_soma_parte, partes)

    fim_execucao = time.time()

    soma_total = sum(resultados)
    print("Soma total:", soma_total)

    tempo_execucao = fim_execucao - inicio_execucao
    minutos = int (tempo_execucao // 60)
    segundos = format(tempo_execucao % 60, ".2f")

    print(f'Tempo de execução \n {minutos} minutos e {segundos} segundos')

if __name__ == "__main__":
    main()