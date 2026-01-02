try:
    from .origin_tree import create_tree, draw_tree
except ImportError:
    from origin_tree import create_tree, draw_tree
from collections import deque


def convert_tree_to_array(root):
    """Збирає всі значення з дерева у чергу"""
    if not root:
        return []
    
    values = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        values.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return values


def heapify(arr, n, i):
    """
    Робить піддерево з коренем i правильною купою.
    """
    largest = i
    left = 2 * i + 1  # Лівий нащадок
    right = 2 * i + 2  # Правий нащадок
    
    # Якщо лівий нащадок більший за корінь
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Якщо правий нащадок більший за поточний
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Якщо найбільший не корінь - міняємо місцями
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr):
    """
    Перетворює масив на max-heap.
    """
    n = len(arr)
    
    # Проходимо від останнього батька до кореня
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    return arr


def assign_values_to_tree(root, values):
    """Записує значення з масиву назад у дерево (BFS)"""
    if not root or not values:
        return
    
    queue = deque([root])
    idx = 0
    
    while queue and idx < len(values):
        node = queue.popleft()
        node.val = values[idx]
        idx += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def convert_to_max_heap(root):
    """Конвертує бінарне дерево в max-heap"""

    values = convert_tree_to_array(root)
    
    build_max_heap(values)
    assign_values_to_tree(root, values)
    return root

# Карта кольорів по рівнях
LEVEL_COLORS = [
    "#FF6B6B",
    "#FF9D00",
    "#F7EB6B",
    "#96CEB4",
]


def colorize_heap(root):
    """Заповнюэ кольорами вузли дерева по рівнях"""
    if not root:
        return
    
    queue = deque([(root, 0)])  # (вузол, рівень)
    
    while queue:
        node, level = queue.popleft()
        
        # Присвоюємо колір з карти (циклічно якщо рівнів більше)
        node.color = LEVEL_COLORS[level % len(LEVEL_COLORS)]
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))


if __name__ == '__main__':
    root = create_tree()
    print("До конвертації:")
    draw_tree(root)
    
    convert_to_max_heap(root)
    colorize_heap(root)
    
    print("Після конвертації в max-heap:")
    draw_tree(root)