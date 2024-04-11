### Para que serve o método append
O método append() é utilizado p0ara adicionar um elemento ao final de uma lista.

### vetor_grande = [i for i in range(1, 1_000_001)]
Isso é uma compreensão de lista, o primeiro i é o valor que será adicionado À lista para cada interação do loop, é como se fosse um 'vetor_grande[i]'

### tamanho_parte = len(vetor_grande) // num_threadspartes = [(i * tamanho_parte, (i + 1) * tamanho_parte) for i in range(num_threads)]
Dividir o vetor em partes iguais para cada thread. Lembra da iteração e índices? O primeiro indície é início e o segundo índice é fim.