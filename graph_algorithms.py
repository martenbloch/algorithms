from enum import Enum
from collections import deque
import priority_queue as pq
import copy
import time


class UnweightedGraph:

    def __init__(self, a_edges, is_directed=False):
        # convert tuple of tuples to adjacency lists
        self.adj_list = {}
        for edge in a_edges:
            start = edge[0]
            end = edge[1]

            if start not in self.adj_list:
                self.adj_list[start] = []
            self.adj_list[start].append(end)

            if end not in self.adj_list:
                self.adj_list[end] = []

            if not is_directed:
                start = edge[1]
                end = edge[0]

                if start not in self.adj_list:
                    self.adj_list[start] = []
                self.adj_list[start].append(end)

                if end not in self.adj_list:
                    self.adj_list[end] = []

    def __str__(self):
        return str(self.adj_list)

    def get_vertexes(self):
        return self.adj_list.keys()

    def get_reachable_vertexes(self, a_vertex):
        return self.adj_list[a_vertex]

    def remove_vertex(self, a_vertex):
        self.adj_list.pop(a_vertex)


def get_all_connections(graph, vertex, c):
    neigh = graph.get_reachable_vertexes(vertex)
    for n in neigh:
        if n in c:
            continue
        c.add(n)
        c = c.union(get_all_connections(graph, n, c))
    return c



class WeightedGraph:
    def __init__(self, a_edges, is_directed=False):
        # convert tuple of tuples to adjacency lists
        self.adj_list = {}
        self.edges = list(a_edges)
        self.is_dir = is_directed
        for edge in a_edges:
            start = edge[0]
            end = edge[1]
            w = edge[2]

            if start not in self.adj_list:
                self.adj_list[start] = {}
            self.adj_list[start][end] = w

            if end not in self.adj_list:
                self.adj_list[end] = {}

            if is_directed:
                start = edge[1]
                end = edge[0]
                w = edge[2]

                if start not in self.adj_list:
                    self.adj_list[start] = {}
                self.adj_list[start][end] = w

                self.edges.append((start, end, w))

    def __str__(self):
        return str(self.adj_list)

    def get_vertexes(self):
        return self.adj_list.keys()

    def get_reachable_vertexes(self, a_vertex):
        return self.adj_list[a_vertex].keys()

    def get_weight(self, a_begin, a_end):
        return self.adj_list[a_begin][a_end]

    def get_edges(self):
        return self.edges

    def is_directed(self):
        return self.is_dir

    def remove_vertex(self, a_vertex):
        for v in self.adj_list.values():
            v.pop(a_vertex, None)


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class BfsInfo:

    def __init__(self):
        self.color = Color.WHITE
        self.d = -1
        self.parent = -1

    def __str__(self):
        return "d:" + str(self.d) + " parent: " + str(self.parent)


def breadth_first_search(a_graph, a_source_vertex):

    # fill each vertex with default data
    info = {key: BfsInfo() for key in a_graph.get_vertexes()}

    # fill data for source vertex
    info[a_source_vertex].color = Color.GRAY
    info[a_source_vertex].d = 0

    # enqueue source vertex
    queue = deque()
    queue.append(a_source_vertex)

    while len(queue) != 0:
        vertex = queue.popleft()
        reachable_vertexes = a_graph.get_reachable_vertexes(vertex)
        for v in reachable_vertexes:
            if info[v].color == Color.WHITE:
                info[v].color = Color.GRAY
                info[v].d = info[vertex].d + 1
                info[v].parent = vertex
                queue.append(v)
        info[vertex].color = Color.BLACK
    return info


class BfInfo:

    def __init__(self, a_vertex):
        self.d = -1
        self.parent = -1
        self.vertex = a_vertex

    def __repr__(self):
        #return "BfInfo({0.d!r}, {0.parent!r})".format(self)
        return "BfInfo({0},{1},{2})".format(self.vertex, self.d, self.parent)

    def __eq__(self, a_other):
        #if self.d == a_other.d:
        if self.vertex == a_other.vertex:
            return True
        else:
            return False

    def __lt__(self, a_other):

        if self.d == a_other.d:
            if self.vertex < a_other.vertex:
                return True
            else:
                return False
        else:
            if self.d != -1 and a_other.d != -1 and self.d < a_other.d:
                return True
            elif self.d != -1 and a_other.d == -1:
                return True
            elif self.d == -1 and a_other.d != -1:
                return False


def relax(u, v, w):
    if v.d > u.d + w or v.d == -1:
        v.d = u.d + w
        v.parent = u.vertex


def rapture_relax(u, v, w):
    cost = 0
    if (w - u.d) < 0:
        cost = 0
    else:
        cost = w - u.d

    if ((v.d > u.d + cost) or v.d == -1) and u.d != -1:
        v.d = u.d + cost
        v.parent = u.vertex


def bellman_ford(a_graph, a_source_vertex, a_relax_fun):
    info = {key: BfInfo(key) for key in a_graph.get_vertexes()}
    info[a_source_vertex].d = 0

    is_directed = a_graph.is_directed()

    for i in range(len(a_graph.get_vertexes()) - 1):
        for u, v, w in a_graph.get_edges():
            a_relax_fun(info[u], info[v], w)

    for u, v, w in a_graph.get_edges():
        if info[v].d > info[u].d + w or info[v].d == -1:
            return {}
    return info


def dijkstra(a_graph, a_source_vertex, a_relax_fun):
    info = {key: BfInfo(key) for key in a_graph.get_vertexes()}

    sorted_list = copy.deepcopy(list(info.values()))
    sorted_list.sort()
    q = pq.SortedPriorityQueue(sorted_list)
    q.remove(info[a_source_vertex])

    info[a_source_vertex].d = 0
    q.enqueue(info[a_source_vertex])

    while not q.is_empty():
        obj = q.dequeue()
        u = obj.vertex

        #a_graph.remove_vertex(u)

        if u == 50000:
            return info

        vs = a_graph.get_reachable_vertexes(u)

        for v in vs:
            w = a_graph.get_weight(u, v)
            old_v = copy.deepcopy(info[v])

            a_relax_fun(info[u], info[v], w)

            # update queue
            if old_v.d != info[v].d and not q.is_empty():
                q.remove(old_v)
                q.enqueue(info[v])

    return info


def dijkstra_bst(a_graph, a_source_vertex, a_relax_fun):
    info = {key: BfInfo(key) for key in a_graph.get_vertexes()}

    sorted_list = copy.deepcopy(list(info.values()))
    #sorted_list.sort()
    q = pq.BstPriorityQueue(sorted_list)
    q.remove(info[a_source_vertex])

    info[a_source_vertex].d = 0
    q.enqueue(info[a_source_vertex])

    while not q.is_empty():
        obj = q.dequeue()
        u = obj.vertex

        #a_graph.remove_vertex(u)

        if u == 50000:
            return info

        vs = a_graph.get_reachable_vertexes(u)

        for v in vs:
            w = a_graph.get_weight(u, v)
            old_v = copy.deepcopy(info[v])

            a_relax_fun(info[u], info[v], w)

            # update queue
            if old_v.d != info[v].d and not q.is_empty():
                q.remove(old_v)
                q.enqueue(info[v])

    return info


def load_data(a_file_name):
    data = []
    for line in open(a_file_name, encoding="utf8"):
        start, end, w = line.split()
        data.append((int(start), int(end), int(w)))
    return data


if __name__ == "__main__":
    print("G")
    g = UnweightedGraph(((1, 2),\
                         (1, 5),\
                         (2, 1),\
                         (2, 5),\
                         (2, 3),\
                         (2, 4),\
                         (3, 2),\
                         (3, 4),\
                         (4, 2),\
                         (4, 5),\
                         (4, 3),\
                         (5, 4),\
                         (5, 1),\
                         (5, 2)), True)

    c = set()
    c = get_all_connections(g,1,c)
    x = 3


    '''
    g = UnweightedGraph(((1, 2),\
                         (1, 5),\
                         (2, 1),\
                         (2, 5),\
                         (2, 3),\
                         (2, 4),\
                         (3, 2),\
                         (3, 4),\
                         (4, 2),\
                         (4, 5),\
                         (4, 3),\
                         (5, 4),\
                         (5, 1),\
                         (5, 2)))
    info = breadth_first_search(g, 1)

    g = WeightedGraph(((0, 3, 3), \
                       (0, 5, 5),\
                       (3, 5, 2),\
                       (3, 9, 6),\
                       (5, 3, 1),\
                       (5, 9, 4),\
                       (5, 11, 6),\
                       (9, 11, 2),\
                       (11, 0, 3),\
                      (11, 9, 7)))

    start = time.time_ns()
    res = bellman_ford(g, 0, relax)
    end = time.time_ns()
    print(res)
    print("exec time:" + str((end - start)/1000000))

    start = time.time_ns()
    #res = dijkstra(g, 0, relax)
    end = time.time_ns()
    print("exec time:" + str((end - start) / 1000000))
    print(res)

    hr = WeightedGraph(((1, 2, 6337),\
                        (1, 3, 1594),\
                        (1, 4, 3766),\
                        (1, 5, 3645),\
                        (1, 6, 75),\
                        (1, 7, 5877),\
                        (1, 8, 8561),\
                        (1, 9, 242),\
                        (1, 10, 6386),\
                        (2, 3, 3331),\
                        (2, 4, 4194),\
                        (2, 5, 8069),\
                        (2, 6, 3934),\
                        (2, 7, 101),\
                        (2, 8, 8536),\
                        (2, 9, 6963),\
                        (2, 10, 9303),\
                        (3, 4, 7639),\
                        (3, 5, 8512),\
                        (3, 6, 1330),\
                        (3, 7, 6458),\
                        (3, 8, 1180),\
                        (3, 9, 3913),\
                        (3, 10, 1565),\
                        (4, 5, 9488),\
                        (4, 6, 1369),\
                        (4, 7, 8066),\
                        (4, 8, 9439),\
                        (4, 9, 7510),\
                        (4, 10, 6833),\
                        (5, 6, 4215),\
                        (5, 7, 194),\
                        (5, 8, 4774),\
                        (5, 9, 4328),\
                        (5, 10, 187),\
                        (6, 7, 1196),\
                        (6, 8, 200),\
                        (6, 9, 8743),\
                        (6, 10, 1433),\
                        (7, 8, 2933),\
                        (7, 9, 2069),\
                        (7, 10, 1974),\
                        (8, 9, 7349),\
                        (8, 10, 2351),\
                        (9, 10, 8423)), True)

    start = time.time_ns()
    res = bellman_ford(hr, 1, rapture_relax)
    end = time.time_ns()
    print("exec time:" + str((end - start)/1000000))

    start = time.time_ns()
    #res = dijkstra(hr, 1, rapture_relax)
    end = time.time_ns()
    print("exec time:" + str((end - start) / 1000000))

    edges = load_data("n1000_no_path.txt")
    g = WeightedGraph(edges)
    start = time.time_ns()
    res = bellman_ford(g, 1, rapture_relax)
    end = time.time_ns()
    print("bf n1000_no_path.txt exec time:" + str((end - start)/1000000))

    start = time.time_ns()
    #res = dijkstra(g, 1, rapture_relax)
    end = time.time_ns()
    print("d n1000_no_path.txt exec time:" + str((end - start)/1000000))
    '''
    #-------------------------------------------------------------------------------------------------------------------
    '''
    edges = load_data("n1000_r417.txt")
    g = WeightedGraph(edges, True)
    #start = time.time_ns()
    #res = bellman_ford(g, 1, rapture_relax)
    #end = time.time_ns()
    #print("bf n1000_r417.txt exec time:{0}, result:{1}".format( ((end - start)/1000000), res[1000]))

    start = time.time_ns()
    res = dijkstra(g, 1, rapture_relax)
    end = time.time_ns()
    print("d n1000_r417.txt exec time:{0}, result:{1}".format( (end - start)/1000000 , res[1000] ) )


    edges = load_data("n1000_r417.txt")
    g = WeightedGraph(edges, True)
    #start = time.time_ns()
    #res = bellman_ford(g, 1, rapture_relax)
    #end = time.time_ns()
    #print("bf n1000_r417.txt exec time:{0}, result:{1}".format( ((end - start)/1000000), res[1000]))

    start = time.time_ns()
    res = dijkstra_bst(g, 1, rapture_relax)
    end = time.time_ns()
    print("d BST n1000_r417.txt exec time:{0}, result:{1}".format( (end - start)/1000000 , res[1000] ) )

    #-------------------------------------------------------------------------------------------------------------------

    edges = load_data("n50000_r97306.txt")
    g = WeightedGraph(edges, True)
    #start = time.time_ns()
    #res = bellman_ford(g, 1, rapture_relax)
    #end = time.time_ns()
    #print("bf n1000_r417.txt exec time:{0}, result:{1}".format( ((end - start)/1000000), res[1000]))

    start = time.time_ns()
    res = dijkstra(g, 1, rapture_relax)
    end = time.time_ns()
    print("d n50000_r97306.txt exec time:{0}, result:{1}".format( (end - start)/1000000 , res[50000] ) )

    edges = load_data("n50000_r97306.txt")
    g = WeightedGraph(edges, True)
    #start = time.time_ns()
    #res = bellman_ford(g, 1, rapture_relax)
    #end = time.time_ns()
    #print("bf n1000_r417.txt exec time:{0}, result:{1}".format( ((end - start)/1000000), res[1000]))

    start = time.time_ns()
    res = dijkstra_bst(g, 1, rapture_relax)
    end = time.time_ns()
    print("d BST n50000_r97306.txt exec time:{0}, result:{1}".format( (end - start)/1000000 , res[50000] ) )

    '''
    '''
    edges = load_data("n100_r117.txt")
    g = WeightedGraph(edges, True)
    start = 0#time.time_ns()
    res = bellman_ford(g, 1, rapture_relax)
    end = 0#time.time_ns()
    print("bf n100_r117.txt exec time:{0}, result:{1}".format( ((end - start)/1000000), res[100]))

    
    start = 0#time.time_ns()
    res = dijkstra(g, 1, rapture_relax)
    end = 0#time.time_ns()
    print("d n100_r117.txt exec time:{0}, result:{1}".format( (end - start)/1000000 , res[100] ) )
    #for k,v in res.items():
    #    print("{0}, {1}".format(k,v))
    '''
    #-------------------------------------------------------------------------------------------------------------------

'''

    edges = load_data("n100_r468.txt")
    g = WeightedGraph(edges, True)
    start = time.time_ns()
    res = bellman_ford(g, 1, rapture_relax)
    end = time.time_ns()
    print("bf n100_r468.txt exec time:" + str((end - start)/1000000))
    print(res[100])

    start = time.time_ns()
    res = dijkstra(g, 1, rapture_relax)
    end = time.time_ns()
    print("d n100_r468.txt exec time:" + str((end - start)/1000000))
    print(res[100])


    edges = load_data("n10000_r288616.txt")
    g = WeightedGraph(edges)
    start = time.time_ns()
    res = dijkstra(g, 1, rapture_relax)
    end = time.time_ns()
    print("d n10000_r288616.txt exec time:" + str((end - start)/1000000))
    print(res[10000])
'''

