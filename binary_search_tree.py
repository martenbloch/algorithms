

class Node:
    def __init__(self):
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node, val:{0}".format(self.value)


class BinarySearchTree:

    def __init__(self, a_values):
        self.root = None
        if a_values:
            for v in a_values:
                self.insert(v)

    def insert(self, a_value):
        if not self.root:
            self.root = Node()
            self.root.value = a_value
        else:
            self.helper_insert(self.root, a_value)

    def helper_insert(self, a_parent_node, a_value):
        if a_value < a_parent_node.value:
            if a_parent_node.left == None:
                new_node = Node()
                new_node.value = a_value
                new_node.parent = a_parent_node
                a_parent_node.left = new_node
                return
            else:
                self.helper_insert(a_parent_node.left, a_value)
        else:
            if a_parent_node.right == None:
                new_node = Node()
                new_node.value = a_value
                new_node.parent = a_parent_node
                a_parent_node.right = new_node
                return
            else:
                self.helper_insert(a_parent_node.right, a_value)

    def find(self, a_value):
        if not self.root:
            return None
        else:
            return self.helper_find(self.root, a_value)

    def helper_find(self, a_parent_node, a_value):
        if a_parent_node.value == a_value:
            return a_parent_node

        if a_value < a_parent_node.value:
            if not a_parent_node.left:
                return None
            else:
                return self.helper_find(a_parent_node.left, a_value)
        else:
            if not a_parent_node.right:
                return None
            else:
                return self.helper_find(a_parent_node.right, a_value)

    def delete_node(self, node):
        is_root = False
        if node == self.root:
            is_root = True

        # case1 - no childs
        if not node.left and not node.right:
            if not is_root:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            if is_root:
                self.root = None
            return

        # case2 - one child
        if node.left and not node.right:
            parent = node.parent
            node.left.parent = parent
            if not is_root:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                self.root = node.left
            return

        if not node.left and node.right:
            parent = node.parent
            node.right.parent = parent
            if not is_root:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            else:
                self.root = node.right
            return


        #case3 - node has 2 childs
        successor = self.successor(node)
        node.value = successor.value
        self.delete_node(successor)

    def delete(self, a_value):
        node = self.find(a_value)
        self.delete_node(node)

    def successor(self, a_node):
        if a_node.right:
            return self.get_min(a_node.right)
        else:
            n = a_node.parent
            while self.is_left_child(n):
                n = n.parent
            return n.parent

    def get_min(self, a_node):
        if not a_node.left:
            return a_node
        else:
            return self.get_min(a_node.left)

    def min(self):
        return self.get_min(self.root)

    def is_left_child(self, a_node):
        if a_node.parent.left == a_node:
            return True
        else:
            return False

    def is_empty(self):
        if self.root:
            return False
        return True


if __name__ == "__main__":
    bst = BinarySearchTree([8, 3, 0, 5, 7, 11, 10, 12, 14])
    bst.delete(8)

    node = bst.find(10)