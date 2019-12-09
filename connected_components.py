
class Element:
    def __init__(self, a_value):
        self.value = a_value
        self.previous = None
        self.next = None

    def set_value(self, a_value):
        self.value = a_value

    def get_value(self):
        return self.value

    def set_previous(self, a_prev):
        self.previous = a_prev

    def set_next(self, a_next):
        self.next = a_next

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, a_pos, a_value):
        pass

    def get(self, a_pos):
        if self.is_out_of_range(a_pos):
            return
        el = self.head
        for i in range(a_pos):
            el = el.get_next()
        return el.get_value()

    def add(self, a_value):
        el = Element(a_value)

        if not self.head:
            self.tail = el
            self.head = el
        else:
            self.tail.set_next(el)
            self.tail = el
        self.size = self.size + 1

    def is_out_of_range(self, a_pos):
        if a_pos < 0 or a_pos > self.size:
            return True
        return False

    def get_size(self):
        return self.size

    def __iter__(self):
        return LinkedListIter(self)

    def __repr__(self):
        text = "LinkedList, values:"
        for el in self:
            text = text + str(el) + ","
        return text


def combine_linked_lists(a_ll1, a_ll2):
    a_ll1.tail.set_next(a_ll2.head)
    a_ll1.tail = a_ll2.tail
    a_ll1.size = a_ll1.get_size() + a_ll2.get_size()


class LinkedListIter:
    def __init__(self, a_linked_list):
        self.linked_list = a_linked_list
        self.n = 0

    def __next__(self):
        if self.n < self.linked_list.get_size():
            val = self.linked_list.get(self.n)
            self.n = self.n + 1
            return val
        else:
            raise StopIteration


class CcElement:

    def __init__(self, a_value):
        self.value = a_value
        self.set = LinkedList()
        self.set.add(self)

    def __repr__(self):
        return "(CcElement) val:{0}".format(self.value)


def get_connected_components(a_vertices, a_edges):
    cc = [CcElement(v) for v in a_vertices]
    sets = {v.set for v in cc}

    count = len(cc)

    for start, end in a_edges:
        start_set = cc[start - 1].set
        end_set = cc[end-1].set

        if start_set != end_set:
            count = count - 1
            if start_set.get_size() < end_set.get_size():
                start_set = cc[end-1].set
                end_set = cc[start - 1].set

            sets.remove(end_set)
            for el in end_set:
                el.set = start_set

            combine_linked_lists(start_set, end_set)

    length = len(sets)
    sets = [s for s in sets if s.get_size() > 1]
    not_connected = length - len(sets)
    return not_connected, sets


class ElementT:
    def __init__(self, a_value):
        self.parent = self
        self.value = a_value
        self.rank = 0

    def __repr__(self):
        return "(ElementT) val:{0}".format(self.value)


def get_connected_components_tree(a_vertices, a_edges):
    cc = [ElementT(v) for v in a_vertices]

    for start, end in a_edges:
        x = find_root(cc[start-1])
        y = find_root(cc[end-1])

        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank = y.rank + 1

    not_connected = len([el for el in cc if el.value == el.parent.value and el.rank == 0])

    for v in cc:
        v.parent = find_root(v)

    occ = [0 for v in a_vertices]
    for el in cc:
        val = el.parent.value
        occ[val-1] = occ[val-1] + 1

    return not_connected, [v for v in occ if v>1]


def find_root(a_el):
    if a_el.value != a_el.parent.value:
        a_el.parent = find_root(a_el.parent)
    return a_el.parent


if __name__ == "__main__":

    cc = get_connected_components_tree([1, 2, 3, 4, 5], ((1, 2), (1, 3), (3, 4)))
    x = 3
