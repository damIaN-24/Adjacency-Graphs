graph = {
    "A": ["B", "C"],
    "B": ["K"],
    "C": ["A", "D", "F"],
    "D": ["C", "E", "G", "H"],
    "E": ["D"],
    "F": ["C", "D", "G", "J"],
    "G": ["F", "D"],
    "H": ["D", "J"],
    "J": ["F", "H"],
    "K": ["B"],
}

def print_neighbour(given_node):
    print(graph[given_node])

#print_neighbour("A")

def node_connection(user_grpah, given_node1, given_node2):
    if given_node1 in graph[given_node2]:
        print(True)
    else:
        print(False)

node_connection(graph,"A", "B")






