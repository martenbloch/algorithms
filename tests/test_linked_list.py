from .. import connected_components


def test_add():
    ll = connected_components.LinkedList()
    ll.add(5)
    ll.add(1)
    ll.add(7)
    assert 3 == ll.get_size()
    assert 5 == ll.get(0)
    assert 1 == ll.get(1)
    assert 7 == ll.get(2)
