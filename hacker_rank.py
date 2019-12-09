import graph_algorithms
import time
import connected_components


def roads_and_libraries(n, c_lib, c_road, cities):
    g = graph_algorithms.UnweightedGraph(cities)
    vertex_set = {v for v in g.get_vertexes()}

    alone_cities = n - len(vertex_set)

    num_of_city_groups = 0
    cost = 0
    while len(vertex_set) != 0:
        el = vertex_set.pop()
        vertex_set.add(el)
        info = graph_algorithms.breadth_first_search(g, el)

        vertexes_to_remove = {k for k, v in info.items() if v.d != -1}

        num_of_vertexes = len(vertexes_to_remove)
        if num_of_vertexes * c_lib < ((num_of_vertexes - 1)*c_road + c_lib):
            cost = cost + (num_of_vertexes * c_lib)
        else:
            cost = cost + (num_of_vertexes - 1)*c_road + c_lib

        vertex_set = vertex_set.difference(vertexes_to_remove)
        num_of_city_groups = num_of_city_groups + 1

    print("groups:{0}".format(num_of_city_groups))
    cost = cost + (alone_cities*c_lib)
    return cost


def roads_and_libraries2(n, c_lib, c_road, cities):

    connected_cities = set()
    groups = []

    for start, end in cities:
        connected_cities.add(start)
        connected_cities.add(end)

        f_start = False
        f_end = False
        i_start = -1
        i_end = -1
        i = 0
        for g in groups:

            if not f_start:
                f_start = start in g
                if f_start and i_start == -1:
                    i_start = i

            if not f_end:
                f_end = end in g
                if f_end and i_end == -1:
                    i_end = i
            i = i + 1

        if not f_start and not f_end:
            s = set()
            s.add(start)
            s.add(end)
            groups.append(s)

        if f_start and not f_end:
            groups[i_start].add(end)

        if not f_start and f_end:
            groups[i_end].add(start)

        if f_start and f_end:
            groups[i_start] = groups[i_start].union(groups[i_end])
            if i_start != i_end:
                groups.pop(i_end)

    alone_cities = n - len(connected_cities)
    cost = alone_cities*c_lib
    for g in groups:
        num_cities = len(g)
        if num_cities * c_lib < ((num_cities - 1)*c_road + c_lib):
            cost = cost + (num_cities * c_lib)
        else:
            cost = cost + (num_cities - 1)*c_road + c_lib
    return cost


def roads_and_libraries3(n, c_lib, c_road, cities):

    connected_cities = set()
    groups = []

    city_to_group = dict()
    cities.sort()

    for start, end in cities:
        connected_cities.add(start)
        connected_cities.add(end)

        s = city_to_group.get(start)
        e = city_to_group.get(end)

        if s is None and e is None:
            si = set()
            si.add(start)
            si.add(end)
            groups.append(si)

            city_to_group[start] = len(groups)-1
            city_to_group[end] = len(groups) - 1

        if s is not None and e is None:
            groups[s].add(end)
            city_to_group[end] = s

        if s is None and e is not None:
            groups[e].add(start)
            city_to_group[start] = e

        if s is not None and e is not None:
            groups[s] = groups[s].union(groups[e])

            for v in groups[e]:
                city_to_group[v] = s

            if s != e:
                for k, v in city_to_group.items():
                    if v > e:
                        city_to_group[k] = v - 1

                groups.pop(e)

    alone_cities = n - len(connected_cities)
    cost = alone_cities*c_lib
    nc = 0
    for g in groups:
        num_cities = len(g)
        nc = nc + num_cities
        if num_cities * c_lib < ((num_cities - 1)*c_road + c_lib):
            cost = cost + (num_cities * c_lib)
        else:
            cost = cost + (num_cities - 1)*c_road + c_lib
    return cost


def roads_and_libraries4(n, c_lib, c_road, cities):
    g = graph_algorithms.UnweightedGraph(cities)

    groups = []
    c = set()
    visited = set()
    vertexes = g.get_vertexes()
    for v in vertexes:
        if v not in visited:
            c = graph_algorithms.get_all_connections(g, v, c)
            visited = visited.union(c)
            groups.append(c)
            c = set()
    print(len(groups))
    return 0


def roads_and_libraries5(n, c_lib, c_road, cities):
    alone_cities, sets = connected_components.get_connected_components([i+1 for i in range(n)], cities)
    print(alone_cities)
    print(len(sets))
    cost = alone_cities*c_lib
    nc = 0
    for g in sets:
        num_cities = g.get_size()
        nc = nc + num_cities
        if num_cities * c_lib < ((num_cities - 1)*c_road + c_lib):
            cost = cost + (num_cities * c_lib)
        else:
            cost = cost + (num_cities - 1)*c_road + c_lib
    return cost

def roads_and_libraries6(n, c_lib, c_road, cities):

    alone_cities, sets = connected_components.get_connected_components_tree([i + 1 for i in range(n)], cities)
    cost = alone_cities*c_lib
    nc = 0
    for g in sets:
        num_cities = g
        nc = nc + num_cities
        if num_cities * c_lib < ((num_cities - 1)*c_road + c_lib):
            cost = cost + (num_cities * c_lib)
        else:
            cost = cost + (num_cities - 1)*c_road + c_lib
    return cost



def merge_sets(a_sets):
    for i in range(len(a_sets)):
        for j in range(i+1, len(a_sets)):
            if j >= len(a_sets):
                continue

            tmp = a_sets[i].intersection(a_sets[j])
            if tmp:
                a_sets[i] = a_sets[i].union(a_sets[j])
                a_sets.pop(j)

    return a_sets


class TestData:

    def __init__(self, n, roads, clib, croad, connections):
        self.n = n
        self.roads = roads
        self.clib = clib
        self.croad = croad
        self.connections = connections


def load_road_and_libraries_data(a_file_name):
    data = []
    item = TestData(0, 0, 0, 0, [])
    for line in open(a_file_name, encoding="utf8"):
        values = line.split()
        if len(values) == 4:
            if item.n != 0:
                data.append(item)
            item = TestData(int(values[0]), int(values[1]), int(values[2]), int(values[3]), [])
        else:
            values = line.split()
            item.connections.append((int(values[0]), int(values[1])))
    data.append(item)
    return data


if __name__ == "__main__":
    print("HK")



    #'''
    test_cases = load_road_and_libraries_data("roads_and_libraries_case3.txt")
    print("loaded data")
    tt = 0
    for data in test_cases:
        start = time.time_ns()
        res = roads_and_libraries6(data.n, data.clib, data.croad, data.connections)
        end = time.time_ns()
        total = ((end - start)/1000000)
        tt = tt + total
        print("result:{0}, cities:{1} time:{2}".format(res, data.n, total))

    print("end: {0}".format(tt))

    '''
    print(roads_and_libraries2(3, 2, 1, ((1, 2), (3, 1), (2, 3))))  # expected 4
    print(roads_and_libraries2(6, 2, 5, ((1, 3), (3, 4), (2, 4), (1, 2), (2, 3), (5, 6))))  # expected 12
    roads_and_libraries2(9, 91, 84, ((8, 2), (2, 9)))        # 805
    roads_and_libraries2(5, 92, 23, ((2,1),(5,3),(5,1), (3,4), (3,1),(5,4),(4,1),(5,2),(4,2))) #184
    roads_and_libraries2(8, 10, 55, ((6,4),(3,2),(7,1)))#80
    roads_and_libraries2(1, 5, 3, ())#5
    roads_and_libraries2(2, 102, 1, ())#204
    '''