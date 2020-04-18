from . import binary_search_insert
from . import binary_search_tree


class SortedPriorityQueue:

    def __init__(self, a_sorted_list):
        self.list = a_sorted_list

    def enqueue(self, a_value):
        pos = binary_search_insert.binary_insert(self.list, a_value)

    def dequeue(self):
        return self.list.pop(0)

    def remove(self, a_value):
        pos = binary_search_insert.binary_search(self.list, a_value)
        self.list.pop(pos)

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False


class BstPriorityQueue:

    def __init__(self, a_values):
        self.bst = binary_search_tree.BinarySearchTree(a_values)

    def enqueue(self, a_value):
        self.bst.insert(a_value)

    def dequeue(self):
        min_node = self.bst.min()
        self.bst.delete_node(min_node)
        return min_node.value

    def remove(self, a_value):
        self.bst.delete(a_value)

    def is_empty(self):
        return self.bst.is_empty()


if __name__ == "__main__":
    q = BstPriorityQueue([1, 3, 5, 9])
    q.remove(3)
    q.remove(1)
    assert q.dequeue() == 5
    q.enqueue(6)
    q.enqueue(7)
    assert q.dequeue() == 6
