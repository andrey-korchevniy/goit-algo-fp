import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def create_heap(arr):
    nodes = {}
    root = None

    for i, val in enumerate(arr):
        nodes[i] = Node(val)
        if i == 0:
            root = nodes[i]
        else:
            parent_index = (i - 1) // 2
            if i % 2 == 1:
                nodes[parent_index].left = nodes[i]
            else:
                nodes[parent_index].right = nodes[i]

    return root

def get_color_gradient(n):
    colors = []
    for i in range(n):
        intensity = 255 - int(255 * (i / n))
        colors.append(f"#9999{intensity:02X}")
    return colors

def dfs(tree_root, colors, visited=None):
    if visited is None:
        visited = []
    visited.append(tree_root)
    tree_root.color = colors[len(visited) - 1]

    if tree_root.left:
        dfs(tree_root.left, colors, visited)
    if tree_root.right:
        dfs(tree_root.right, colors, visited)
    return visited

def bfs(tree_root, colors):
    queue = [tree_root]
    visited = []
    while queue:
        node = queue.pop(0)
        visited.append(node)
        node.color = colors[len(visited) - 1]

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited

heap_values = [38, 34, 17, 15, 10, 9, 8, 5, 7, 6]
heap_root = create_heap(heap_values)
colors = get_color_gradient(len(heap_values))

visited_dfs = dfs(heap_root, colors)
draw_tree(heap_root)  # Малюємо стан дерева після DFS

heap_root = create_heap(heap_values)  # Оновлюємо дерево для BFS
visited_bfs = bfs(heap_root, colors)
draw_tree(heap_root)  # Малюємо стан дерева після BFS