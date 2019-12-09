from .. import heap


def test_get_parent():
    h = heap.Heap()
    assert h.get_parent(0) == 0


def test_enqueue():
    h = heap.Heap()
    h.enqueue(8)
    h.enqueue(3)
    h.enqueue(9)
    h.enqueue(0)
    h.enqueue(4)
    h.enqueue(1)
    h.enqueue(2)
    h.enqueue(6)
    h.enqueue(5)

    assert h.dequeue() == 0
    assert h.dequeue() == 1
    assert h.dequeue() == 2
