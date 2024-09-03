class Node:
    """Класс узла Графа."""
 
    def __init__(self, name: str, cost=float('inf')):
        self.name = name
        self.cost = cost
        self.links = []

    def __repr__(self) -> str:
        return self.name


class Link:
    """Класс связи Графа."""

    def __init__(self, node_1: Node, node_2: Node, cost=0) -> None:
        self.node_1 = node_1
        self.node_2 = node_2
        self.cost = cost

    def __eq__(self, obj) -> bool:
        return (self.node_1 == obj.node_1 and self.node_2 == obj.node_2
                or self.node_1 == obj.node_2 and self.node_2 == obj.node_1)
    
    def __repr__(self) -> str:
        return f'{self.node_1} - {self.node_2}: {self.cost}'


class Graph:
    """Класс Графа."""
 
    def __init__(self):
        self._links: list[Link] = []
        self._nodes: list[Node] = []

    @property
    def links(self):
        return self._links
    
    def add_node(self, node: Node):
        if node not in self._nodes:
            self.self._nodes.append(node)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
        if link.node_1 not in self._nodes:
            self._nodes.append(link.node_1)
        if link.node_2 not in self._nodes:
            self._nodes.append(link.node_2)

    def get_graph_data(self):
        graph = {}
        for link in self._links:
            graph.setdefault(link.node_1, {}).update({link.node_2: link.cost})
        
        return graph


    def find_lowest_cost_node(self, costs, processed):
        """Функция поиска узла с нимаеньшим весом."""

        lowest_cost = float('inf')
        lowest_cost_node = None
        for node, cost in costs.items():
            # cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node

        return lowest_cost_node


    def find_path(self, start_node: Node, end_node: Node):
        """Функция построения кратчайшего маршрута."""

        processed = []
        result_nodes_list = []
        total_distance = 0
        start_node.cost = 0

        graph = self.get_graph_data()
        parents = {}
        
        neighbors = graph[start_node]
        next_node = self.find_lowest_cost_node(neighbors, processed)
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

            next_node = self.find_lowest_cost_node(neighbors, processed)

        result_nodes_list.append(end_node)
        next_node = parents.get(end_node)

        while next_node:
            result_nodes_list.append(next_node)
            end_node = next_node
            next_node = parents.get(end_node)
        
        result_nodes_list.reverse()
        total_distance = result_nodes_list[-1].cost

        return result_nodes_list, total_distance

# {1: {2: 1}, 2: {3: 2, 4: 7}, 3: {4: 3}, 4: {5: 1}}


# map_metro = Graph()
# v1 = Node("Сретенский бульвар")
# v2 = Node("Тургеневская")
# v3 = Node("Чистые пруды")
# v4 = Node("Лубянка")
# v5 = Node("Кузнецкий мост")
# v6 = Node("Китай-город 1")
# v7 = Node("Китай-город 2")

# map_metro.add_link(Link(v1, v2, 1))
# map_metro.add_link(Link(v2, v3, 1))
# map_metro.add_link(Link(v1, v3, 1))

# map_metro.add_link(Link(v4, v5, 1))
# map_metro.add_link(Link(v6, v7, 1))

# map_metro.add_link(Link(v2, v7, 5))
# map_metro.add_link(Link(v3, v4, 3))
# map_metro.add_link(Link(v5, v6, 3))

# print(len(map_metro._links))
# print(len(map_metro._nodes))
# path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
# print(path[0], path[1])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# # print(sum([x.dist for x in path[1]]))  # 7


# map2 = Graph()
# v1 = Station("1")
# v2 = Station("2")
# v3 = Station("3")
# v4 = Station("4")
# v5 = Station("5")

# map2.add_link(Link(v1, v2, 1))
# map2.add_link(Link(v2, v3, 2))
# map2.add_link(Link(v2, v4, 7))
# map2.add_link(Link(v3, v4, 3))
# map2.add_link(Link(v4, v5, 1))

# assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
# assert len(map2._nodes) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

# path = map2.find_path(v1, v5)
# print(path)

