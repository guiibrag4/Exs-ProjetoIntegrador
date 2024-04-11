import threading
import time

# Função para calcular a soma de uma parte do vetor
def calcular_soma_parte(vetor, inicio, fim, resultado):
    soma = sum(vetor[inicio:fim])
    resultado.append(soma)

# Função principal
def main():

    inicio_execucao = time.time()

    vetor_grande = [i for i in range(1, 1_000_001)]

    num_threads = 4

    tamanho_parte = len(vetor_grande) // num_threads
    partes = [(i * tamanho_parte, (i + 1) * tamanho_parte) for i in range(num_threads)]

    resultados = []

    threads = []
    for inicio, fim in partes:
        thread = threading.Thread(target=calcular_soma_parte, args=(vetor_grande, inicio, fim, resultados))
        thread.start()
        threads.append(thread)

    # Aguardar todas as threads terminarem
    for thread in threads:
        thread.join()

    fim_execucao = time.time()

    # Calcular a soma total a partir dos resultados parciais
    soma_total = sum(resultados)
    print("Soma total:", soma_total)

    tempo_execucao = fim_execucao - inicio_execucao
    minutos = int (tempo_execucao // 60)
    segundos = format(tempo_execucao % 60, ".2f")

    print(f'Tempo de execução \n {minutos} minutos e {segundos} segundos')

if __name__ == "__main__":
    main()