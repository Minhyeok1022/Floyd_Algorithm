'''
import sys module for representing NO_PATHinite number
which indicates no direct path

import unittest module for testing the code

import main module which is the imperative version of floyd algorithm
to compare the expected distances
'''
import sys
import unittest
import main

NO_PATH = sys.maxsize
# create a graph with 5 nodes and random edge weights
graph = [
    [0, 4, 2, 1, 6, 2, 7, 3],
    [NO_PATH, 0, 5, 7, 2, 9, 1, 8],
    [NO_PATH, NO_PATH, 0, 2, 8, 3, 5, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0, 7, 6, 8, 3],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 5, 3, 6],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 2, 5],
    [-1, NO_PATH, -1, -1, NO_PATH, NO_PATH, 0, 8],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0],
]

MAX_LENGTH = len(graph[0])

def floyd_recursive(start_node, intermediate, end_node, distance, check):
    """
    :param start_node: starting node
    :param intermediate: node
    :param end_node: ending node
    :param distance: distance from start until intermediate
    :param check: 1D lists that checking intermediate node is visited or not
    :return: return minimum distance between start to end
    """

    # Assume that if start_node and end_node are the same
    # then the distance would be zero
    if start_node == end_node:
        graph[start_node][end_node] = 0

    # If there is no path connected, return and update nothing
    if intermediate == NO_PATH:
        return

    # If there is any path to reach the end node,
    # check total distance and update to smaller value
    if intermediate == end_node:
        graph[start_node][end_node] = min(graph[start_node][end_node], distance)
        return

    distance = graph[start_node][intermediate] + graph[intermediate][end_node]

    for inter in range(MAX_LENGTH):
        # If already visited, passing
        if check[inter]:
            continue
        check[inter] = 1
        if not check[start_node]:
            return

        # recursively call itself with next intermediate node and renewed distance
        floyd_recursive(start_node, inter, end_node, distance, check)
        check[inter] = 0

def solve(dist):
    """
    :param dist: initial distance
    :return: returning updated 2D lists that having minimum distances between start to end
    """

    for start in range(MAX_LENGTH):
        for end in range(MAX_LENGTH):
            # make a check variable to check whether nodes are visited or not
            check = [0] * MAX_LENGTH
            check[start] = 1
            floyd_recursive(start, 0, end, NO_PATH, check)
    print(dist)
    return dist

class TestFloyd(unittest.TestCase):
    """
    Making unittest class
    """
    def test_floyd_recursion(self):
        """
        Making test function to test sample graph
        """

        # expected values are from the imperative version
        # expected should be the same as result variable below to calculate exact time
        expected = main.floyd(graph)
        result = solve(graph)

        # assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
