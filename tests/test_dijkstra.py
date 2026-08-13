from main import dijkstra


def test_finds_shortest_path() -> None:
    graph = {
        1: [(2, 3), (3, 1)],
        2: [(4, 2)],
        3: [(4, 1)],
        4: [],
    }

    distance, path = dijkstra(graph, 1, 4)

    assert distance == 2
    assert path == [1, 3, 4]


def test_returns_none_when_unreachable() -> None:
    graph = {
        1: [(2, 1)],
        2: [],
        3: [],
    }

    distance, path = dijkstra(graph, 1, 3)

    assert distance is None
    assert path == []
