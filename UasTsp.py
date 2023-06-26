import networkx as nx
import matplotlib.pyplot as plt

# Membuat graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
G.add_edges_from([('A', 'B', {'weight': 12}),
                  ('A', 'G', {'weight': 12}),
                  ('B', 'C', {'weight': 30}),
                  ('B', 'D', {'weight': 12}),
                  ('C', 'D', {'weight': 11}),
                  ('C', 'G', {'weight': 9}),
                  ('C', 'E', {'weight': 3}),
                  ('D', 'E', {'weight': 11}),
                  ('D', 'F', {'weight': 10}),
                  ('E', 'F', {'weight': 6}),
                  ('E', 'G', {'weight': 7}),
                  ('F', 'G', {'weight': 9}),
                  ('F', 'H', {'weight': 5}),
                  ('G', 'H', {'weight': 8})])


# Fungsi untuk menghitung shortest path menggunakan algoritma TSP
def tsp_shortest_path(graph):
    shortest_path = nx.approximation.traveling_salesman_problem(graph)
    return shortest_path


# Fungsi untuk menghitung shortest path menggunakan algoritma Dijkstra
def dijkstra_shortest_path(graph, start, end):
    shortest_path = nx.dijkstra_path(graph, start, end)
    return shortest_path


# Main program
def main():
    print("Pilihan penghitungan shortest path:")
    print("1. TSP (Traveling Salesman Problem)")
    print("2. Dijkstra")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        # Menghitung shortest path menggunakan TSP
        print("--- TSP (Traveling Salesman Problem) ---")
        tsp_path = tsp_shortest_path(G)
        print("Shortest path:", tsp_path)

        # Menampilkan graph dengan shortest path
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx_edges(G, pos, edgelist=[(tsp_path[i], tsp_path[i + 1]) for i in range(len(tsp_path) - 1)],
                               edge_color='red', width=2)
        plt.show()

    elif choice == '2':
        # Menghitung shortest path menggunakan Dijkstra
        print("--- Dijkstra ---")
        start = input("Masukkan titik awal: ")
        end = input("Masukkan titik akhir: ")
        dijkstra_path = dijkstra_shortest_path(G, start, end)
        print("Shortest path:", dijkstra_path)

        # Menampilkan graph dengan shortest path
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx_edges(G, pos, edgelist=[(dijkstra_path[i], dijkstra_path[i + 1]) for i in
                                                 range(len(dijkstra_path) - 1)], edge_color='red', width=2)
        plt.show()


if __name__ == "__main__":
    main()
