import threading
import time

# Função para calcular a soma de uma parte do vetor
def calcular_soma_parte(vetor, inicio, fim, resultado):
    soma = sum(vetor[inicio:fim])
    resultado.append(soma)

# Função principal
def main():
    # Vetor de números muito grande
    inicio_execucao = time.time()
    vetor_grande = range(1, 500_000_001)  # Exemplo de vetor com números de 1 a 1 milhão

    # Número de threads a serem utilizadas
    num_threads = 2

    # Dividir o vetor em partes iguais para cada thread
    tamanho_parte = len(vetor_grande) // num_threads
    partes = [(i * tamanho_parte, (i + 1) * tamanho_parte) for i in range(num_threads)]

    # Lista para armazenar os resultados parciais
    resultados = []

    # Criar e iniciar as threads
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