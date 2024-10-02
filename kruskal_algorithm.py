from merge_sort import merge_sort  # Importing the merge_sort function from the merge_sort module
from union_find import union_find  # Importing the union_find class from the union_find module


def kruskal(vertices_list, edges_list):
    """
    Computes the Minimum Spanning Tree (MST) of a connected, undirected graph using Kruskal's algorithm.

    Parameters:
    vertices_list: A list of vertices in the graph. Each vertex should be a hashable type (e.g., string, int).
    edges_list: A list of edges in the graph, where each edge is represented as a tuple (u, v, weight).
                       'u' and 'v' are the vertices connected by the edge, and 'weight' is the weight of the edge.

    Returns:
    list: A list of edges in the minimum spanning tree, where each edge is represented as a tuple (u, v, weight).

    Description:
    The function initializes an empty list to hold the edges of the minimum spanning tree (MST). It first sorts the 
    edges based on their weights using the `merge_sort` function. Then, it utilizes a union-find data structure 
    (represented by the `union_find` class) to efficiently keep track of connected components in the graph.

    The algorithm iterates through the sorted list of edges, adding an edge to the MST if it connects two vertices 
    that are in different sets (to avoid cycles). The union operation merges the sets of the two vertices.

    The function returns the list of edges that make up the minimum spanning tree.

    Example:
   
    Given the following graph G(V,E)
    
    Vertices: ['A', 'B', 'C', 'D', 'E']
    Edges: [
        ('A', 'B', 2),
        ('A', 'D', 3),
        ('A', 'C', 1),
        ('A', 'E', 2),
        ('B', 'C', 3),
        ('C', 'D', 8),
        ('D', 'E', 5),
        ('C', 'E', 1)
    ]
    
    The function can be called as follows:
    
    min_spann_tree = kruskal(['A', 'B', 'C', 'D', 'E'], [
        ('A', 'B', 2),
        ('A', 'D', 3),
        ('A', 'C', 1),
        ('A', 'E', 2),
        ('B', 'C', 3),
        ('C', 'D', 8),
        ('D', 'E', 5),
        ('C', 'E', 1)
    ])
    
    Output:
    The minimum spanning tree will be:
    [('A', 'C', 1), ('C', 'E', 1), ('A', 'B', 2), ('A', 'D', 3)]
    
    This output represents the edges included in the minimum spanning tree, along with their weights.
    """
    minimal_span_tree = []  # Initialize an empty list to store the edges of the minimum spanning tree
    merge_sort(edges_list)  # Sort the edges based on their weights using the merge_sort function
    u_f = union_find(vertices_list)  # Create an instance of the union_find class for disjoint set operations

    # Iterate through each edge in the sorted list
    for u, v, weight in edges_list:
        # Check if the vertices u and v are in different sets
        if u_f.find(u) != u_f.find(v):
            # If they are in different sets, add the edge (u, v) with its weight to the minimal spanning tree
            minimal_span_tree.append((u, v, weight))
            # Union the sets of u and v
            u_f.union(u, v)

    return minimal_span_tree  # Return the list containing the edges of the minimum spanning tree



    

    
