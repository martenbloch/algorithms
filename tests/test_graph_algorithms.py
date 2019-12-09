from .. import graph_algorithms


def test_equality():
    o1 = graph_algorithms.BfInfo(1)
    o2 = graph_algorithms.BfInfo(1)
    o3 = graph_algorithms.BfInfo(2)
    o2.d = 8
    assert o1 == o2
    assert o1 != o3


def test_less_than():

    # v1.d == v2.d, v1.vertex < v2.v.vertex
    o1 = graph_algorithms.BfInfo(1)
    o2 = graph_algorithms.BfInfo(2)
    assert o1 < o2

    # v1.d != v2.d
    o3 = graph_algorithms.BfInfo(3)
    o3.d = 100
    o4 = graph_algorithms.BfInfo(4)
    o4.d = 15
    assert o4 < o3

    # v1.d != v2.d, v1.d == -1
    o5 = graph_algorithms.BfInfo(5)
    o6 = graph_algorithms.BfInfo(6)
    o6.d = 4
    assert o6 < o5

    # v1.d != v2.d, v2.d == -1
    o7 = graph_algorithms.BfInfo(5)
    o7.d = 3
    o8 = graph_algorithms.BfInfo(6)
    assert o7 < o8


def test_dijkstra():
    pass

