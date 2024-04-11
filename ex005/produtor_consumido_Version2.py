import threading
import queue

def worker(q, nome):
    count = 0
    print(f'{nome} iniciada')
    while True:
        item = q.get()
        if item is None:
            break
        print(f'{nome} processando o item: {item}')
        q.task_done()
        count += 1
    print(f'Morreu {nome} e executou {count} itens')
    
q = queue.Queue()

print('Digite o número de threads:')
threads = int(input())

for i in range(int(threads)):
    t = threading.Thread(target=worker, args=(q, 'Thread-' + str(i)))
    t.start()

# Adicionar itens à fila
for i in range (11):
    q.put(i)

# Esperar até que todos os itens sejam processados
q.join()

for i in range(threads):  # Adicionar um item None para cada thread
    q.put(None)
    
# Adicionar um item especial para sinalizar o término
for t in threading.enumerate():
    if t is not threading.main_thread() and t.is_alive():
        t.join()


# q: O que faz o método get
# a: Retorna e remove um item da fila

# q: O que faz o método task_done
# a: Indica que um item foi processado

# q: O que faz o método Queue
# a: Cria uma fila

# q: O que faz o método put
# a: Adiciona um item à fila

