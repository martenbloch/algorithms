import hacker_rank
import os


def test_road_and_libraries():
    print(os.getcwd())
    file = "roads_and_libraries_case0.txt"
    test_cases = hacker_rank.load_road_and_libraries_data(os.getcwd() + "/tests/data/" + file)

    for data in test_cases:
        hacker_rank.roads_and_libraries2(data.n, data.clib, data.croad, data.connections)


def test_count_triplets_case_0():

    nums = [1, 2, 2, 4]
    assert hacker_rank.countTriplets(nums, 2) == 2


def test_count_triplets_case_1():

    nums = [1, 3, 9, 9, 27, 81]
    assert hacker_rank.countTriplets(nums, 3) == 6


def test_count_triplets_case_6():

    f = open(os.getcwd() + "/tests/data/triplets-case-6.txt", 'r')

    nums = f.readlines()
    nums = [int(i) for i in nums[0].split()]
    assert hacker_rank.countTriplets(nums, 3) == 2325652489


def test_count_triplets_case_10():

    f = open(os.getcwd() + "/tests/data/triplets-case-10.txt", 'r')

    nums = f.readlines()
    nums = [int(i) for i in nums[0].split()]
    assert hacker_rank.countTriplets(nums, 10) == 1339347780085


def test_count_triplets_case_12():

    nums = [1, 5, 5, 25, 125]
    assert hacker_rank.countTriplets(nums, 5) == 4


def test_count_triplets_case_13():

    nums = [1, 2, 2, 4, 1, 2, 4]
    assert hacker_rank.countTriplets(nums, 2) == 6


def test_count_triplets_case_14():

    nums = [2, 2, 2, 2, 2, 2, 2]
    assert hacker_rank.countTriplets(nums, 1) == 35
