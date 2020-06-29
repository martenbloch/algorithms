import graph_algorithms
import time
import connected_components
import math
from enum import Enum
import math

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


def rangoli(a_size):
    a_latter = ord('a')
    result = [[] for i in range(a_size*2-1)]
    line = [chr(i) for i in range(a_latter, a_latter + a_size, 1)]
    line = line[::-1] + line[1:]
    result[a_size-1] = line[:]
    offset = 1
    middle = a_size - 1
    cm = a_size -1
    width = (a_size*2-1) + (a_size*2-2)
    while len(line) > 1:
        line.pop(middle)
        line.pop(middle-1)
        result[cm-offset] = line[:]
        result[cm + offset] = line[:]
        middle = middle - 1
        offset = offset + 1

    # format
    output = []
    for l in result:
        output.append(format(l, width))
    return output


def format(a_list, a_size):
    text = ""
    for l in a_list:
        text = text + l + '-'

    if len(text) < a_size:
        padding = round((a_size - len(text))/2)
        text = '-'*padding + text + '-'*padding

    return text[:-1]


def hourglassSum(arr):
    rows = len(arr)
    cols = len(arr[0])
    max_v = -100
    for i in range(rows):
        for j in range(cols):
            s = sum_h(i,j,rows,cols,arr)
            if s > max_v:
                max_v = s
    return max_v


def sum_h(x,y,w,h,arr):
    if x+2 >= w:
        return -100
    if y+2 >= h:
        return -100
    s = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]

    return s


def rotate_left(a_list, r):
    l = len(a_list)
    r = r % l
    k = a_list[r:] + a_list[:r]
    return k


class SinglyLinkedListNode:

    def __init__(self, a_data):
        self.data = a_data
        self.next = None

    def __repr__(self):
        return "data:{0}".format(self.data)


def mergeLists(head1, head2):
    head = None
    tail = None

    if head1.data < head2.data:
        head = SinglyLinkedListNode(head1.data)
        head1 = head1.next
    else:
        head = SinglyLinkedListNode(head2.data)
        head2 = head2.next

    tail = head

    while True:
        if not head1 and not head2:
            break

        if head1 and not head2:
            n = SinglyLinkedListNode(head1.data)
            tail.next = n
            tail = n
            head1 = head1.next
            continue

        if head2 and not head1:
            n = SinglyLinkedListNode(head2.data)
            tail.next = n
            tail = n
            head2 = head2.next
            continue

        if head1.data < head2.data:
            n = SinglyLinkedListNode(head1.data)
            tail.next = n
            tail = n
            head1 = head1.next
        else:
            n = SinglyLinkedListNode(head2.data)
            tail.next = n
            tail = n
            head2 = head2.next

    return head


def remove_duplicates(head):
    if not head:
        return

    s = set()
    s.add(head.data)
    ptr = head.next
    prev = head

    while ptr:
        if ptr.data in s:
            x = prev
            x.next = ptr.next
        else:
            s.add(ptr.data)

        ptr = ptr.next
        prev = prev.next
    return head


class Triplet:

    def __init__(self, a_start_val, a_ratio):
        self.ratio = a_ratio
        self.start_val = a_start_val
        self.mid_val = self.start_val * self.ratio
        self.end_val = self.start_val * self.ratio * self.ratio
        self.num_s = 1
        self.acc = 0
        self.nn = 0

    def append(self, a_val):

        if a_val == self.mid_val:
            self.acc += self.num_s
        elif a_val == self.end_val:
            self.nn += self.acc
        elif a_val == self.start_val:
            self.num_s += 1


def get_a0s(val, r):
    ret = []
    if val % r == 0:
        ret.append(int(val/r))
    else:
        return ret
    if ret[0] % r == 0:
        ret.append(int(ret[0]/r))
    return ret


def countTriplets(arr, r):

    if r == 1:
        d = dict()
        for i in range(len(arr)):
            v = arr[i]
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]

        num = 0
        for k, v in d.items():
            m = 0
            m = math.factorial(len(v)) / (6 * math.factorial(len(v) - 3))
            num += m
        return int(num)

    d = {e: get_a0s(e, r) for e in set(arr)}
    triplets = {}

    for i in range(len(arr)):
        v = arr[i]

        for e in d[v]:
            if e in triplets.keys():
                triplets[e].append(v)

        if v in triplets:
            triplets[v].append(v)
        else:
            triplets[v] = Triplet(v, r)

    num = 0
    for v in triplets.values():
        num += v.nn

    return num


class Dir(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    LEFT_UP = 4
    LEFT_DOWN = 5
    RIGHT_UP = 6
    RIGHT_DOWN = 7


def queensAttack(n, k, y, x, obstacles):
    num_squares = [0 for i in range(8)]
    num_squares[Dir.LEFT.value] = x - 1
    num_squares[Dir.RIGHT.value] = n - x
    num_squares[Dir.UP.value] = n - y
    num_squares[Dir.DOWN.value] = y - 1
    num_squares[Dir.LEFT_UP.value] = min(x - 1, n - y)
    num_squares[Dir.LEFT_DOWN.value] = min(x - 1, y - 1)
    num_squares[Dir.RIGHT_UP.value] = min(n - x, n - y)
    num_squares[Dir.RIGHT_DOWN.value] = min(n - x, y - 1)

    if k == 0:
        return sum(num_squares)
    else:
        for oy, ox in obstacles:
            if y == oy and ox < x:
                num_squares[Dir.LEFT.value] = min(num_squares[Dir.LEFT.value], x - ox - 1)
            elif y == oy and ox > x:
                num_squares[Dir.RIGHT.value] = min(num_squares[Dir.RIGHT.value], ox - x - 1)
            elif x == ox and oy > y:
                num_squares[Dir.UP.value] = min(num_squares[Dir.UP.value], oy - y - 1)
            elif x == ox and oy < y:
                num_squares[Dir.DOWN.value] = min(num_squares[Dir.DOWN.value], y - oy - 1)
            elif ox > x and oy < y and ox-x == y-oy:
                num_squares[Dir.RIGHT_DOWN.value] = min(num_squares[Dir.RIGHT_DOWN.value], min(ox - x, y - oy) -1)
            elif ox > x and oy > y and ox-x == oy-y:
                num_squares[Dir.RIGHT_UP.value] = min(num_squares[Dir.RIGHT_UP.value], min(ox - x, oy - y) - 1)
            elif ox < x and oy < y and x-ox == y-oy:
                num_squares[Dir.LEFT_DOWN.value] = min(num_squares[Dir.LEFT_DOWN.value], min(x - ox, y - oy) - 1)
            elif ox < x and oy > y and x-ox == oy-y:
                num_squares[Dir.LEFT_UP.value] = min(num_squares[Dir.LEFT_UP.value], min(x - ox, oy - y) - 1)

    return sum(num_squares)


def split(m, w, amount):
    diff = m - w
    if diff < 0:
        if amount <= abs(diff):
            m += amount
        else:
            m += abs(diff)
            r = amount - abs(diff)
            m += r // 2
            w += r - r // 2
    else:
        if amount <= abs(diff):
            w += amount
        else:
            w += abs(diff)
            r = amount - abs(diff)
            w += r // 2
            m += r - r // 2

    return m, w


def minimumPasses(m, w, p, n):
    tc = 0
    passes = 0
    l = 0
    min_pass_acc = []
    print("")
    while tc < n:
        tc = m * w + l
        min_pass_acc.append(((n - l) / (m * w)) + passes)

        amount = tc // p
        if amount != 0:
            m, w = split(m, w, amount)
            l = tc - amount * p
            passes += 1
        else:
            np = math.floor((p - l)/(m*w))
            if (p - l) % (m*w) == 0:
                np -= 1
            l = np * m * w + l
            passes += np
            pass

        if tc >= n:
            m_p = int(math.ceil(min(min_pass_acc)))
            if m_p == 0:
                m_p = 1
            if m_p < passes:
                return m_p
            else:
                return passes
        #l = tc - amount * p
        #print("pass:{}, m:{} w:{}, l:{}".format(passes, m, w, l))
    return passes


if __name__ == "__main__":
    print("HK")


