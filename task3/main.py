"""
Завдання 3. Алгоритм Дейкстри з бінарною купою

Знаходження найкоротших шляхів у зваженому графі.
"""

import heapq


def dijkstra(graph: dict, start: str) -> tuple[dict, dict]:
    """
    Алгоритм Дейкстри з використанням бінарної купи (min-heap).
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    previous = {vertex: None for vertex in graph}
    
    # Бінарна купа: (відстань, вершина)
    heap = [(0, start)]
    
    # Множина відвіданих вершин
    visited = set()
    
    while heap:
        # Витягуємо вершину з мінімальною відстанню - O(log V)
        current_distance, current_vertex = heapq.heappop(heap)
        
        # Пропускаємо, якщо вже відвідали
        if current_vertex in visited:
            continue
            
        visited.add(current_vertex)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо знайшли коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                # Додаємо в купу - O(log V)
                heapq.heappush(heap, (distance, neighbor))
    
    return distances, previous


def reconstruct_path(previous: dict, start: str, end: str) -> list:
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    
    if path[0] != start:
        return []
    
    return path


def print_results(start: str, distances: dict, previous: dict):
    """Виводить результати алгоритму."""
    print(f"\nНайкоротші шляхи від вершини '{start}':")
    print("-" * 50)
    
    for vertex in sorted(distances.keys()):
        if vertex == start:
            continue
            
        distance = distances[vertex]
        if distance == float('infinity'):
            print(f"{start} -> {vertex}: шлях не існує")
        else:
            path = reconstruct_path(previous, start, vertex)
            path_str = " -> ".join(path)
            print(f"{start} -> {vertex}: відстань = {distance}, шлях: {path_str}")


# Створення зваженого графа використовуючи списки суміжності
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

if __name__ == "__main__":
    print("Граф:")
    for vertex, edges in graph.items():
        print(f"  {vertex}: {edges}")
    
    start_vertex = 'A'
    distances, previous = dijkstra(graph, start_vertex)
    
    print_results(start_vertex, distances, previous)
