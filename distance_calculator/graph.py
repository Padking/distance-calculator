import numpy as np
import pandas as pd

from queue import PriorityQueue


FILEPATH = '../data/matrix_distance'  # FIXME


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for _ in range(self.v)] for _ in range(self.v)]

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def _dijkstra(self, start_vertex):
        D = {v: float('inf') for v in range(self.v)}
        self.visited = []
        D[start_vertex] = 0
        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

    def get_dist_path_mat(self) -> pd.DataFrame:
        num_of_vertices = self.v
        # Задание названий столбцов датафрейма
        cols = ['city_id'] + [f'dist_with_city_{i}' for i in range(num_of_vertices)]
        dist_df = pd.DataFrame(columns=cols)

        for i in range(num_of_vertices):
            distances = self._dijkstra(i)
            row = [i] + list(distances.values())
            dist_df.loc[len(dist_df), dist_df.columns] = row

        return dist_df.astype('int')


def create_graph_model(mat: np.array, graph: Graph, vertices=50):
    for i in range(vertices):
        for j in range(vertices):
            dist = mat[i][j]
            if dist != 0:
                graph.add_edge(i, j, dist)


def get_shortest_distance(distance_table: pd.DataFrame, from_city=1, to_city=2):
    distance = distance_table.iloc[from_city][f'dist_with_city_{to_city}']

    return float(distance)


def get_shortest_distance_table(distance_filepath=FILEPATH) -> pd.DataFrame:
    file_with_graph = open(distance_filepath, 'rb')
    mat = np.load(file_with_graph)

    vertices = len(mat)
    g = Graph(vertices)

    create_graph_model(mat, g)
    shortest_distance_table = g.get_dist_path_mat()

    return shortest_distance_table


if __name__ == '__main__':
    shortest_distance_table = get_shortest_distance_table()
    shortest_distance = get_shortest_distance(shortest_distance_table)
    print(f'Кратчайший путь между городами "1" и "2": {shortest_distance}')
