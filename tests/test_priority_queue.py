from .. import priority_queue


def test_enqueue_dequeue():
    q = priority_queue.SortedPriorityQueue([1, 5, 9])
    assert q.dequeue() == 1
    q.enqueue(2)
    assert q.dequeue() == 2
    assert q.dequeue() == 5
    assert q.dequeue() == 9


def test_remove():
    q = priority_queue.SortedPriorityQueue([1, 3, 5, 9])
    q.remove(3)
    q.remove(1)
    assert q.dequeue() == 5
    q.enqueue(6)
    q.enqueue(7)
    assert q.dequeue() == 6


def test_bst_enqueue_dequeue():
    q = priority_queue.BstPriorityQueue([1, 5, 9])
    assert q.dequeue() == 1
    q.enqueue(2)
    assert q.dequeue() == 2
    assert q.dequeue() == 5
    assert q.dequeue() == 9


def test_bst_remove():
    q = priority_queue.BstPriorityQueue([1, 3, 5, 9])
    q.remove(3)
    q.remove(1)
    assert q.dequeue() == 5
    q.enqueue(6)
    q.enqueue(7)
    assert q.dequeue() == 6
