import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        dist, current = heapq.heappop(priority_queue)

        if dist > distances[current]:
            continue

        for neighbor, weight in graph[current].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return distances

if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 5, 'E': 2},
        'C': {'A': 4, 'F': 6},
        'D': {'B': 5, 'E': 1, 'G': 4},
        'E': {'B': 2, 'D': 1, 'F': 3, 'H': 2},
        'F': {'C': 6, 'E': 3, 'H': 1},
        'G': {'D': 4, 'H': 3},
        'H': {'E': 2, 'F': 1, 'G': 3}
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)
    print(f"Shortest distances from {start_node}: {shortest_distances}")