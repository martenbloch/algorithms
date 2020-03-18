

class SelectionSort:
    def __init__(self):
        self.num_swaps = 0

    def sort(self, a_collection):
        self.num_swaps = 0
        size = len(a_collection)
        final_position = 0
        for i in range(size):
            smallest_idx = final_position
            smallest = a_collection[smallest_idx]

            #find minimum
            for j in range(final_position+1, size):
                if a_collection[j] < smallest:
                    smallest = a_collection[j]
                    smallest_idx = j
            self.swap(a_collection, final_position, smallest_idx)
            final_position +=1

    def swap(self, a_collection, a_final_pos, a_idx):
        if a_final_pos == a_idx:
            return
        tmp = a_collection[a_final_pos]
        a_collection[a_final_pos] = a_collection[a_idx]
        a_collection[a_idx] = tmp
        self.num_swaps += 1

    def num_swaps(self):
        return self.num_swaps


class BubbleSort:
    def __init__(self):
        self.num_swaps = 0

    def sort(self, a_collection):

        size = len(a_collection) - 1
        for i in range(len(a_collection) - 1):
            for i in range(size):
                if a_collection[i] > a_collection[i+1]:
                    tmp = a_collection[i]
                    a_collection[i] = a_collection[i+1]
                    a_collection[i+1] = tmp
                    self.num_swaps += 1
            size -= 1

    def num_swaps(self):
        return self.num_swaps


a = [5, 1, 2, 3, 7, 8, 6, 4]
b = BubbleSort()
b.sort(a)
print(a)
