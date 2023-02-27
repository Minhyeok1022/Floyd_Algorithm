"""
1. sys module for representing NO_PATHinite number
which indicates no direct path
2. itertools module for
"""

import sys
import itertools
import unittest
import floyd_recursive

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    MAX_LENGTH = len(distance[0])

    for intermediate, start_node, end_node\
    in itertools.product\
    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):

        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node] )
    #Any value that have sys.maxsize has no path
    #print (distance)
    return distance
#floyd(graph)


class TestFloyd(unittest.TestCase):

    def test_floyd(self):
        # create a graph with 5 nodes and random edge weights

        NO_PATH = sys.maxsize

        graph = [
            [0, 4, 2, 1, 6, 2, 7, 3, 5, 8],
            [NO_PATH, 0, 5, 7, 2, 9, 1, 8, 6, 3],
            [NO_PATH, NO_PATH, 0, 2, 8, 3, 5, 2, 9, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0, 7, 6, 8, 3, 2, 9],
            [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 5, 3, 6, 1, 8],
            [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 2, 5, 8, 3],
            [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 8, 4, 2],
            [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 4],
            [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0]
        ]


        # expected output distances
        # expected should be the same as result variable below to calculate exact time
        expected = floyd_recursive.solve(graph)

        # run the algorithm on the graph
        result = floyd(graph)
        # assert that the result matches the expected output
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
