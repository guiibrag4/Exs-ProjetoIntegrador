# monte uma estratégia para calcular a soma dos valores contidas no arquivo de texto em anexo.

import threading
import queue

def worker(q, numeros):
    soma = sum(numeros)
    q.put(soma)

def soma_bilhao():
    num_threads = 1
    q = queue.Queue()
    threads = []
    
    with open('numerosBilhao.txt', 'r') as f:
        numeros = [int(line) for line in f]
    
    nums_por_thread = len(numeros) // num_threads

    for i in range(num_threads):
        start = i * nums_por_thread
        print(f"Thread {i} iniciando de {start}")
        if i == num_threads - 1:
            end = len(numeros)
        else:
            end = start + nums_por_thread
        t = threading.Thread(target=worker, args=(q, numeros[start:end]))
        t.start()
        print(f"Thread {i} iniciada")
        threads.append(t)

    for t in threads:
        t.join()

    total = 0
    while not q.empty():
        total += q.get()

    return total

if __name__ == "__main__":
    resultado = soma_bilhao()
    print(f"A soma total é: {resultado}")