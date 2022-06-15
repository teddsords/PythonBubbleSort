# Disciplina: Arquitetura de Computadores
# Atividade: Avaliação 01 – Programação em Linguagem de Montagem e de Alto Nível
# Programa 01
# Aluno: Teddy Ordoñez

def bubble_sort(array):
  size = len(array)

  for i in range(size):
    for j in range(0, size-i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]


array = [8, 2, 0 ,1]

print(f"Original array: {array}")
bubble_sort(array)
print(f"Sorted array: {array}")