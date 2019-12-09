from .. import binary_search_tree


def test_bst_insert():
    bst = binary_search_tree.BinarySearchTree([5, 3, 8, 0, 2, 6])


def test_bst_find():
    bst = binary_search_tree.BinarySearchTree([5, 3, 8, 0])
    assert bst.find(0).value == 0


def test_bst_delete_no_child():
    bst = binary_search_tree.BinarySearchTree([8, 3, 0, 5, 7, 11, 10, 12, 14])
    bst.delete(7)

    assert bst.find(5).right == None


def test_bst_delete_one_child():
    bst = binary_search_tree.BinarySearchTree([8, 3, 0, 5, 7, 11, 10, 12, 14])
    bst.delete(12)

    bst.find(11).right.value == 14


def test_bst_delete_two_childs():
    bst = binary_search_tree.BinarySearchTree([8, 3, 0, 5, 7, 11, 10, 12, 14])
    bst.delete(8)

    node = bst.find(10)
    assert node.left.value == 3
    assert node.right.value == 11


def test_bst_get_min():
    bst = binary_search_tree.BinarySearchTree([8, 3, 0, 5, 7, 11, 10, 12, 14])
    assert bst.min().value == 0
