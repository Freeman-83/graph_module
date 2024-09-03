def get_graph_data(links):
    """Функция постороения графа маршрута."""
    graph = {}
    for link in links:
        graph.setdefault(link.node_1, {}).update({link.node_2: link.cost})
    
    return graph


def find_lowest_cost_node(costs, processed):
    """Функция поиска узла с нимаеньшим весом."""

    lowest_cost = float('inf')
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def find_path(links, start_node, end_node):
    """Функция построения кратчайшего маршрута."""

    processed = []
    result_nodes_list = []
    total_distance = 0
    start_node.cost = 0

    graph = get_graph_data(links)
    parents = {}
    
    neighbors = graph[start_node]
    next_node = find_lowest_cost_node(neighbors, processed)
    next_node.cost = start_node.cost + neighbors[next_node]
    parents[next_node] = start_node

    while next_node:
        neighbors = graph.get(next_node, {})

        for neighbors_node in neighbors:
            new_cost = next_node.cost + neighbors[neighbors_node]
            
            if neighbors_node.cost > new_cost:
                neighbors_node.cost = new_cost
                parents[neighbors_node] = next_node

        processed.append(next_node)

        next_node = find_lowest_cost_node(neighbors, processed)

    result_nodes_list.append(end_node)
    next_node = parents.get(end_node)

    while next_node:
        result_nodes_list.append(next_node)
        end_node = next_node
        next_node = parents.get(end_node)
    
    result_nodes_list.reverse()
    total_distance = result_nodes_list[-1].cost

    return result_nodes_list, total_distance
