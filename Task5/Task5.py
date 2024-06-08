import uuid
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.parent = None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root, traversal_type, visited_nodes):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = []
    labels = {}
    for node_id, data in heap.nodes(data=True):
        if node_id in visited_nodes:
            brightness = visited_nodes.index(node_id) / len(visited_nodes)
            color = "#{:02x}{:02x}{:02x}".format(
                int(brightness * int(data['color'][1:3], 16)),
                int(brightness * int(data['color'][3:5], 16)),
                int(brightness * int(data['color'][5:], 16))
            )
            colors.append(color)
            labels[node_id] = data['label']
        else:
            colors.append(data['color'])
            labels[node_id] = data['label']

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color="white")
    if traversal_type == "depth_first":
        traversal_label = "Обхід у глибину"
    elif traversal_type == "breadth_first":
        traversal_label = "Обхід у ширину"
    plt.text(0.02, 0.95, traversal_label, fontsize=12, fontweight='bold', transform=plt.gca().transAxes) 
    plt.show()


def depth_first_traversal(root):
    if root is None:
        return []
    stack = [(root, [root.id])]
    visited = []
    while stack:
        node, path = stack.pop()
        if node.id not in visited:
            visited.append(node.id)
            node.color = "#1296F0"  
            if node.right:
                stack.append((node.right, path + [node.right.id]))
            if node.left:
                stack.append((node.left, path + [node.left.id]))
            yield visited, path

def breadth_first_traversal(root):
    if root is None:
        return []
    queue = Queue()
    queue.put((root, [root.id]))
    visited = []
    while not queue.empty():
        node, path = queue.get()
        if node.id not in visited:
            visited.append(node.id)
            node.color = "#FF5733"  
            if node.left:
                queue.put((node.left, path + [node.left.id]))
            if node.right:
                queue.put((node.right, path + [node.right.id]))
            yield visited, path

# Функція для вставки елемента в купу
def heap_insert(root, key):
    new_node = Node(key)
    if root is None:
        return new_node
    else:
        queue = [root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                new_node.parent = current
                break
            elif not current.right:
                current.right = new_node
                new_node.parent = current
                break
            else:
                queue.append(current.left)
                queue.append(current.right)
        heapify_up(root, new_node)
    return root

# Функція для перебудови купи 
def heapify_up(root, node):
    while node.parent is not None and node.val > node.parent.val:
        node.val, node.parent.val = node.parent.val, node.val
        node = node.parent

# Відображення бінарної купи
def visualize_traversal(traversal_type):
    # Відповідно до вибраного обходу будуємо бінарне дерево
    heap_root = None
    heap_root = heap_insert(heap_root, 5)
    heap_root = heap_insert(heap_root, 3)
    heap_root = heap_insert(heap_root, 8)
    heap_root = heap_insert(heap_root, 2)
    heap_root = heap_insert(heap_root, 6)
    heap_root = heap_insert(heap_root, 10)

    # Візуалізація обходу
    visited_nodes = []
    if traversal_type == "depth_first":
        for visited, path in depth_first_traversal(heap_root):
            visited_nodes.append(visited)
        draw_heap(heap_root, "depth_first", visited_nodes[-1])
    elif traversal_type == "breadth_first":
        for visited, path in breadth_first_traversal(heap_root):
            visited_nodes.append(visited)
        draw_heap(heap_root, "breadth_first", visited_nodes[-1])

# Візуалізація обходу у глибину
visualize_traversal("depth_first")

# Візуалізація обходу у ширину
visualize_traversal("breadth_first")
