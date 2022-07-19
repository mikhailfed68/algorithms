from algorithms.dijkstras_algorithm import find_lowest_cost_node
from algorithms.dijkstras_algorithm import find_lowest_cost_road


graph = {
    'a': {'b': 0, 'c': 1},
    'b': {'d': 2},
    'c': {'f': 3, 'g': 8, 'b': 3},
    'd': {'e': 5},
    'e': {'f': 1, 'c': 4},
    'f': {'h': 6, 'g': 2},
    'g': {'h': 7},
    'h': {}
    }

infinity = float('inf')
costs = {
    'b': 0,
    'c': 1,
    'd': infinity,
    'e': infinity,
    'f': infinity,
    'g': infinity,
    'h': infinity
    }

parents = {
    'b': 'a',
    'c': 'a',
    'd': None,
    'e': None,
    'f': None,
    'g': None,
    'h': None
    }

def test_find_lowest_cost_node():
    costs = {
    'b': 6,
    'c': 1,
    'd': 7,
    'e': float('inf')
    }

    assert find_lowest_cost_node(costs) == 'c'


def test_find_lowest_cost_road():
    assert find_lowest_cost_road(graph, costs, parents) == 10
