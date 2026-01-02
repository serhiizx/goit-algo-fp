import sys
from pathlib import Path
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

sys.path.insert(0, str(Path(__file__).parent.parent))

from task4 import create_tree, convert_to_max_heap
from task4.origin_tree import add_edges


def draw_tree_on_ax(ax, tree_root, current_id=None):
    """Малює дерево на існуючій канві"""
    ax.clear()
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    # Чорна рамка тільки на поточному вузлі
    edge_colors = ['black' if node[0] == current_id else 'none' 
                   for node in tree.nodes(data=True)]
    
    nx.draw(tree, pos=pos, labels=labels, arrows=False, 
            node_size=2500, node_color=colors, ax=ax,
            edgecolors=edge_colors, linewidths=3)


def bfs_visualize(root, ax, fig, color="#FFAEAE"):
    """BFS обхід з візуалізацією"""
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        node.color = color
        
        draw_tree_on_ax(ax, root, node.id)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.8)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs_visualize(root, ax, fig, color="#D0FFAE"):
    """DFS обхід з візуалізацією """
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        node.color = color
        
        draw_tree_on_ax(ax, root, node.id)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.8)
        
        # Спочатку правий, потім лівий (щоб лівий був зверху стеку)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def run_visual_dfs(root):
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 5))
    
    draw_tree_on_ax(ax, root)
    plt.pause(1)
    
    bfs_visualize(root, ax, fig)
    
    plt.ioff()
    plt.show()

def run_visual_bfs(root):
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 5))
    
    draw_tree_on_ax(ax, root)
    plt.pause(1)
    
    dfs_visualize(root, ax, fig)
    
    plt.ioff()
    plt.show()

if __name__ == '__main__':
    root = create_tree()
    convert_to_max_heap(root)
    
    run_visual_bfs(root)
    run_visual_dfs(root)
