from .. import hacker_rank
import os


def test_road_and_libraries():
    print(os.getcwd())
    file = "roads_and_libraries_case0.txt"
    test_cases = hacker_rank.load_road_and_libraries_data(os.getcwd() + "/tests/data/" + file)

    for data in test_cases:
        hacker_rank.roads_and_libraries2(data.n, data.clib, data.croad, data.connections)

