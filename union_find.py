class union_find:
    """
    This Union_find class implements the Union-Find data structure,
    also known as Disjoint Set Union (DSU). This structure is used to keep track
    of a partition of a set into disjoint subsets and supports efficient
    union and find operations.

    Operations:
    - Find: Determines the root of the set a particular element belongs to.
    - Union: Merges two sets into one by connecting their roots.

    Attributes:
    - parent: A dictionary that stores the parent of each element.
              If an element is its own parent, it is a root.
    """

    def __init__(self, V):
        """
        Initialize the Union-Find structure.
        Each element starts in its own set, so the parent of each element is itself.
        """
        self.parent = {}
        for v in V:#Each node starts off as its own parent
            self.parent[v]=v
            

    def find(self, v):
        """
        Finds the root of the set containing element v.
        """
        if self.parent[v] != v:
            # Path compression: update the parent of v to its root to flatten the tree
            self.parent[v] = self.find(self.parent[v])  # Recursive call to find the root
        return self.parent[v]

    def union(self, v, u):
        """
        Merges the sets containing elements v and u.
        """
        # Find the roots of both sets
        v_Root = self.find(v)
        u_Root = self.find(u)

        # If they have different roots, merge them
        if v_Root != u_Root:
            # Make one root the parent of the other (arbitrarily)
            self.parent[u_Root] = v_Root
