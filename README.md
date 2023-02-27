# Floyd_Warshall Algorithm
Floyd_Algorithm python code for finding the shortest paths between all-paired vertices in a weighted directed 2D graph.

## Usage
To use the Floyd-Warshall algorithm, there are two py files
1) main.py : imperative way
2) floyd_recursive.py : recursive way

They import each other to compare each other's answer in unittest module.
If want the exact code execution time, change expected variable in unnittest class as its own answer. 

```python
graph = [[0, 2, 3, 999],
    [999, 0, 7, 1],
    [4, 999, 0, 6],
    [999, 999, 999, 0]
]

# returns 'graph'
floyd_warshall(graph)

print(graph)

The graph matrix contains the shortest path distances between all pairs of vertices, 

## Contributing

## Requirements
The Floyd-Warshall algorithm implementation requires python 3.

## License
This implementation of the Floyd-Warshall algorithm is released under the MIT License. See the LICENSE file for more details.

## Credits
This implementation was developed by Minhyeok Kim
-Imperative way code is provided by University of Liverpool

## Issues
If you encounter any issues with this implementation, please file an issue on the GitHub repository.
