import hacker_rank
import os
import matplotlib.pyplot as plt


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


def test_queens_attack_01():
    assert hacker_rank.queensAttack(4, 0, 4, 4, []) == 9


def test_queens_attack_02():
    hacker_rank.queensAttack(4, 1, 4, 4, [(2, 4)])


def test_queens_attack_03():
    assert hacker_rank.queensAttack(8, 1, 4, 4, [(5, 3)]) == 24


def test_queens_attack_04():
    assert hacker_rank.queensAttack(5, 3, 3, 4, [(2, 4), (3, 2), (5, 5)]) == 10


def test_queens_attack_05():

    obstacles = [
        (54, 87),
        (64, 97),
        (42, 75),
        (32, 65),
        (42, 87),
        (32, 97),
        (54, 75),
        (64, 65),
        (48, 87),
        (48, 75),
        (54, 81),
        (42, 81),
        (45, 17),
        (14, 24),
        (35, 15),
        (95, 64),
        (63, 87),
        (25, 72),
        (71, 38),
        (96, 97),
        (16, 30),
        (60, 34),
        (31, 67),
        (26, 82),
        (20, 93),
        (81, 38),
        (51, 94),
        (75, 41),
        (79, 84),
        (79, 65),
        (76, 80),
        (52, 87),
        (81, 54),
        (89, 52),
        (20, 31),
        (10, 41),
        (32, 73),
        (83, 98),
        (87, 61),
        (82, 52),
        (80, 64),
        (82, 46),
        (49, 21),
        (73, 86),
        (37, 70),
        (43, 12),
        (94, 28),
        (10, 93),
        (52, 25),
        (50, 61),
        (52, 68),
        (52, 23),
        (60, 91),
        (79, 17),
        (93, 82),
        (12, 18),
        (75, 64),
        (69, 69),
        (94, 74),
        (61, 61),
        (46, 57),
        (67, 45),
        (96, 64),
        (83, 89),
        (58, 87),
        (76, 53),
        (79, 21),
        (94, 70),
        (16, 10),
        (50, 82),
        (92, 20),
        (40, 51),
        (49, 28),
        (51, 82),
        (35, 16),
        (15, 86),
        (78, 89),
        (41, 98),
        (70, 46),
        (79, 79),
        (24, 40),
        (91, 13),
        (59, 73),
        (35, 32),
        (40, 31),
        (14, 31),
        (71, 35),
        (96, 18),
        (27, 39),
        (28, 38),
        (41, 36),
        (31, 63),
        (52, 48),
        (81, 25),
        (49, 90),
        (32, 65),
        (25, 45),
        (63, 94),
        (89, 50),
        (43, 41)
    ]

    x = [e[1] for e in obstacles]
    y = [e[0] for e in obstacles]

    plt.plot(x, y, 'ro')

    x = [81]*100
    y = [i for i in range(1, 101)]
    plt.plot(x, y, 'k')

    s = 34, 1
    x = [i + 34 for i in range(66)]
    y = [i + 1 for i in range(66)]
    plt.plot(x, y, 'k')

    plt.plot(81, 48, "bo")
    plt.grid(True, alpha=1)
    #plt.show()

    assert hacker_rank.queensAttack(100, 100, 48, 81, obstacles) == 40


def test_make_candies_01():

    assert hacker_rank.minimumPasses(1, 2, 1, 60) == 4


def test_make_candies_02():

    assert hacker_rank.minimumPasses(3, 1, 2, 12) == 3


def test_make_candies_03():

    assert hacker_rank.minimumPasses(1, 1, 6, 45) == 16


def test_make_candies_04():

    assert hacker_rank.minimumPasses(1, 1, 1000000000000, 1000000000000) == 1000000000000


def test_make_candies_05():

    assert hacker_rank.minimumPasses(5361, 3918, 8447708, 989936375520) == 3577


def test_make_candies_06():

    assert hacker_rank.minimumPasses(5184889632, 5184889632, 20, 10000) == 1


def test_make_candies_07():
        assert hacker_rank.minimumPasses(1, 100, 10000000000, 1000000000000) == 617737754


def test_make_candies_08():
    assert hacker_rank.minimumPasses(1, 1, 499999999999, 1000000000000) == 999999999999


def test_make_candies_09():
    assert hacker_rank.minimumPasses(3, 13, 13, 1000000000000) == 10


def test_make_candies_10():
    assert hacker_rank.minimumPasses(1, 1, 400000000000, 1000000000000) == 850000000000


def test_make_candies_11():
    assert hacker_rank.minimumPasses(1, 3, 92, 373) == 88
