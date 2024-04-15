import threading
import queue

def worker(q, nome):
    soma = 0
    count = 0
    print(f'{nome} iniciada')
    while True:
        item = q.get()
        if item is None:
            break
        print(f'{nome} processando o item: {item}')
        soma += item
        q.task_done()
        count += 1
    print (f'{nome} finalizada. Soma: {soma}')
    print(f'Morreu {nome} e executou {count} itens')
    
q = queue.Queue()

print('Digite o número de threads:')
threads = int(input())

for i in range(int(threads)):
    t = threading.Thread(target=worker, args=(q, 'Thread-' + str(i)))
    t.start()

# Adicionar itens à fila
with open ('numerosBilhao.txt', 'r') as f:
    for line in f:
        q.put(int(line))
    
# Esperar até que todos os itens sejam processados
q.join()

for i in range(threads):  # Adicionar um item None para cada thread
    q.put(None)
    
# Adicionar um item especial para sinalizar o término
for t in threading.enumerate():
    if t is not threading.main_thread() and t.is_alive():
        t.join()

# measure-command { python produtor_consumidor_version2.py | Out-Default }
