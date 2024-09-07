class Node:
    """Класс узла Графа."""
 
    def __init__(self, name: str, cost=float('inf')):
        self.name = name
        self.cost = cost
        # self.links = []

    def __repr__(self) -> str:
        return self.name


class Link:
    """Класс связи между вершинами Графа."""

    def __init__(self, node_1: Node, node_2: Node, cost=1) -> None:
        self.node_1 = node_1
        self.node_2 = node_2
        self.cost = cost

    def __eq__(self, obj) -> bool:
        return (self.node_1 == obj.node_1 and self.node_2 == obj.node_2
                or self.node_1 == obj.node_2 and self.node_2 == obj.node_1)
    
    def __repr__(self) -> str:
        return f'link: {self.node_1} -> {self.node_2}, cost: {self.cost}'


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

    @staticmethod
    def get_graph_data(links):
        """Функция постороения графа маршрута."""
        graph = {}
        for link in links:
            graph.setdefault(link.node_1, {}).update({link.node_2: link.cost})
        
        return graph

    @staticmethod
    def find_lowest_cost_node(nodes, processed):
        """Функция поиска узла с наименьшим весом."""

        lowest_cost = float('inf')
        lowest_cost_node = None
        for node, cost in nodes.items():
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node

        return lowest_cost_node


    def find_path(self, start_node, end_node):
        """Функция построения кратчайшего маршрута."""

        processed = []
        result_nodes_list = []
        total_distance = 0
        start_node.cost = 0

        graph = self.get_graph_data(self.links)
        parents = {}

        while start_node:
            neighbors = graph.get(start_node, {})

            for neighbors_node in neighbors:
                new_cost = start_node.cost + neighbors[neighbors_node]
                
                if neighbors_node.cost > new_cost:
                    neighbors_node.cost = new_cost
                    parents[neighbors_node] = start_node

            processed.append(start_node)

            next_node = self.find_lowest_cost_node(neighbors, processed)
            start_node = next_node

        result_nodes_list.append(end_node)
        next_node = parents.get(end_node)

        while next_node:
            result_nodes_list.append(next_node)
            next_node = parents.get(next_node)
        
        result_nodes_list.reverse()
        total_distance = end_node.cost

        return result_nodes_list, total_distance
