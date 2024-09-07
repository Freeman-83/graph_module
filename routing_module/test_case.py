from base_classes import Node, Link, Graph


class Station(Node):
    ...


class LinkMetro(Link):
    ...


class TransferStation(Link):
    ...


class MetroGraph(Graph):
    ...


map1 = Graph()
v1 = Node('1')
v2 = Node('2')
v3 = Node('3')
v4 = Node('4')
v5 = Node('5')

map1.add_link(Link(v1, v2))
map1.add_link(Link(v2, v3))
map1.add_link(Link(v2, v4))
map1.add_link(Link(v3, v4))
map1.add_link(Link(v4, v5))

assert len(map1._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map1._nodes) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

map1.add_link(Link(v2, v1))
assert len(map1._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map1.find_path(v1, v5)
print(path)

s = path[1]
print(s)
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Node), "класс Station должен наследоваться от класса Vertex"


map2 = MetroGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(Link(v1, v2, 1))
map2.add_link(Link(v2, v3, 2))
map2.add_link(Link(v2, v4, 7))
map2.add_link(Link(v3, v4, 3))
map2.add_link(Link(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._nodes) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)
print(path)


map_metro = MetroGraph()

v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(Link(v1, v2, 1))
map_metro.add_link(Link(v2, v3, 1))
map_metro.add_link(Link(v1, v3, 1))

map_metro.add_link(Link(v4, v5, 1))
map_metro.add_link(Link(v6, v7, 1))

map_metro.add_link(Link(v2, v7, 5))
map_metro.add_link(Link(v3, v4, 3))
map_metro.add_link(Link(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._nodes))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0], path[1])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# print(sum([x.dist for x in path[1]]))  # 7


