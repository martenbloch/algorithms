

class Heap:

    def __init__(self):
        self.list = []

    def enqueue(self, a_value):
        self.list.append(a_value)
        self.swim(len(self.list)-1)

    def dequeue(self):
        tmp = self.list[0]

        if len(self.list) > 1:
            self.list[0] = self.list[len(self.list)-1]
            self.sink(0)

        self.list.pop()
        return tmp

    def find(self, a_value):

        parent = 0
        if self.list[parent] == a_value:
            return 0

        while True:
            left = (2 * parent) + 1
            right = (2 * parent) + 2







    def swim(self, a_index):
        if a_index == 0:
            return

        parent = self.get_parent(a_index)

        if not self.list[parent] < self.list[a_index]:
            self.swap(a_index, parent)
            self.swim(parent)

    def sink(self, a_index):
        child_idx = self.get_larger_child(a_index)

        if child_idx == -1:
            return

        if not self.list[a_index] < self.list[child_idx]:
            self.swap(child_idx, a_index)
            self.sink(child_idx)

    def get_larger_child(self, a_index):
        left_idx = (2 * a_index) + 1
        right_idx = (2 * a_index) + 2

        if left_idx >= len(self.list):
            return -1

        if right_idx >= len(self.list):
            return left_idx

        if not self.list[left_idx] < self.list[right_idx]:
            return right_idx
        else:
            return left_idx

    def get_parent(self, a_index):
        parent = int((a_index - 1)/2)
        return parent

    def swap(self, idx1, idx2):
        tmp = self.list[idx1]
        self.list[idx1] = self.list[idx2]
        self.list[idx2] = tmp

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    h = Heap()
    h.enqueue(8)
    h.enqueue(3)
    h.enqueue(9)
    h.enqueue(0)
    h.enqueue(4)
    h.enqueue(1)
    h.enqueue(2)
    h.enqueue(6)
    h.enqueue(5)

    while not h.is_empty():
        print(h.dequeue())