


def graph_maker(puzzle):

    """
    Given an array, turns into BST nodes.
    """

    graph = {}

    base = "Node"

    for i in range(len(puzzle)):
        for j in range(len(puzzle)):

            zero = 0
            zero = {}
            graph.update(zero)



puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(graph_maker(puzzle))