import sys
from pathlib import Path
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

sys.path.insert(0, str(Path(__file__).parent.parent))

from task4 import create_tree, convert_to_max_heap
from task4.origin_tree import add_edges


def draw_tree(ax, tree_root, current_id=None):
    ax.clear()
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = []
    labels = {}
    edge_colors = []
    
    for node in tree.nodes(data=True):
        colors.append(node[1]['color'])
        labels[node[0]] = node[1]['label']
        if node[0] == current_id:
            edge_colors.append('black')
        else:
            edge_colors.append('none')
    
    nx.draw(tree, pos=pos, labels=labels, arrows=False, 
            node_size=2500, node_color=colors, ax=ax,
            edgecolors=edge_colors, linewidths=3)


def count_nodes(root):
    if root is None:
        return 0
    count = 1
    count = count + count_nodes(root.left)
    count = count + count_nodes(root.right)
    return count


def reset_colors(root):
    if root is None:
        return
    root.color = "#CCCCCC"
    reset_colors(root.left)
    reset_colors(root.right)


def get_color(step, total, base_r, base_g, base_b):
    factor = step / max(total - 1, 1)
    r = int(base_r + (255 - base_r) * factor * 0.4)
    g = int(base_g + (255 - base_g) * factor * 0.4)
    b = int(base_b + (255 - base_b) * factor * 0.4)
    color = "#" + format(r, '02x') + format(g, '02x') + format(b, '02x')
    return color


# Створюємо дерево
root = create_tree()
convert_to_max_heap(root)

total_nodes = count_nodes(root)

# ============ BFS обхід (в ширину) ============
print("BFS обхід (в ширину)")

plt.ion()
fig, ax = plt.subplots(figsize=(8, 5))
draw_tree(ax, root)
plt.pause(1)

# Використовуємо чергу для BFS
queue = deque()
queue.append(root)
step = 0

while len(queue) > 0:
    node = queue.popleft()
    
    # Змінюємо колір вузла (синій)
    node.color = get_color(step, total_nodes, 65, 185, 255)
    step = step + 1
    
    # Малюємо дерево
    draw_tree(ax, root, node.id)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.8)
    
    # Додаємо дітей в чергу
    if node.left is not None:
        queue.append(node.left)
    if node.right is not None:
        queue.append(node.right)

plt.ioff()
plt.show()

# Скидаємо кольори
reset_colors(root)

# ============ DFS обхід (в глибину) ============
print("DFS обхід (в глибину)")

plt.ion()
fig, ax = plt.subplots(figsize=(8, 5))
draw_tree(ax, root)
plt.pause(1)

# Використовуємо стек для DFS
stack = []
stack.append(root)
step = 0

while len(stack) > 0:
    node = stack.pop()
    
    # Змінюємо колір вузла (рожевий)
    node.color = get_color(step, total_nodes, 255, 30, 90)
    step = step + 1
    
    # Малюємо дерево
    draw_tree(ax, root, node.id)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.8)
    
    # Додаємо дітей в стек (правий перший, щоб лівий був зверху)
    if node.right is not None:
        stack.append(node.right)
    if node.left is not None:
        stack.append(node.left)

plt.ioff()
plt.show()
