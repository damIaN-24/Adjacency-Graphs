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

# def print_neighbour(given_node):
#     print(graph[given_node])
#
# #print_neighbour("A")
#
# def node_connection(user_graph, given_node1, given_node2):
#     if given_node1 in graph[given_node2]:
#         print(True)
#     else:
#         print(False)
#
# node_connection(graph,"A", "B")
#
# from stack import Stack

# stack_obj = Stack()
#
from queue import ListQueue
#
#
# current_node = "J"
# visited_list = [current_node]
# queue_list = ListQueue()
#
# queue_list.enqueue(current_node)
#
# while queue_list.get_size() > 0:
#     temp_current = current_node
#
#     for neighbour in sorted(graph[current_node]):
#
#         if neighbour not in visited_list:
#             current_node = neighbour
#             queue_list.enqueue(current_node)
#             visited_list.append(current_node)
#             break
#
#     if temp_current == current_node:
#         current_node = queue_list.dequeue()
#
# print(visited_list)


#Depth first traversal
current_node = "J"
visited_list = [current_node]
queue_list = ListQueue()

#Take in first node into the queue
queue_list.enqueue(current_node)

#loop through node neighbours
while queue_list.get_size() > 0:
    current_node = queue_list.dequeue()
    for neighbour in sorted(graph[current_node]):
        if neighbour not in visited_list:
            visited_list.append(neighbour)
            queue_list.enqueue(neighbour)

print(visited_list)





