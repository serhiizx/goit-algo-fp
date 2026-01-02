import heapq

# Створення графа
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Початкова вершина
start = 'A'

# Ініціалізація відстаней
distances = {}
for vertex in graph:
    distances[vertex] = float('infinity')
distances[start] = 0

# Словник для збереження попередніх вершин
previous = {}
for vertex in graph:
    previous[vertex] = None

# Бінарна купа (відстань, вершина)
heap = []
heapq.heappush(heap, (0, start))

# Множина відвіданих вершин
visited = set()

# Основний цикл алгоритму Дейкстри
while len(heap) > 0:
    # Витягуємо вершину з мінімальною відстанню
    current_distance, current_vertex = heapq.heappop(heap)
    
    # Пропускаємо якщо вже відвідали
    if current_vertex in visited:
        continue
    
    visited.add(current_vertex)
    
    # Перебираємо всіх сусідів
    neighbors = graph[current_vertex]
    for neighbor in neighbors:
        weight = neighbors[neighbor]
        new_distance = current_distance + weight
        
        # Якщо знайшли коротший шлях
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            previous[neighbor] = current_vertex
            heapq.heappush(heap, (new_distance, neighbor))

# Виведення результатів
print("Граф:")
for vertex in graph:
    print(f"  {vertex}: {graph[vertex]}")

print(f"\nНайкоротші шляхи від вершини '{start}':")
print("-" * 50)

for vertex in sorted(distances.keys()):
    if vertex == start:
        continue
    
    # Відновлення шляху
    path = []
    current = vertex
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    # Виведення
    distance = distances[vertex]
    path_str = " -> ".join(path)
    print(f"{start} -> {vertex}: відстань = {distance}, шлях: {path_str}")
