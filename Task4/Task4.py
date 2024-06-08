import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла
        self.parent = None 

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

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
                new_node.parent = current  # Встановити посилання на батьківський вузол
                break
            elif not current.right:
                current.right = new_node
                new_node.parent = current  # Встановити посилання на батьківський вузол
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
heap_root = None
heap_root = heap_insert(heap_root, 5)
heap_root = heap_insert(heap_root, 3)
heap_root = heap_insert(heap_root, 8)
heap_root = heap_insert(heap_root, 2)
heap_root = heap_insert(heap_root, 6)
heap_root = heap_insert(heap_root, 10)
draw_heap(heap_root)
