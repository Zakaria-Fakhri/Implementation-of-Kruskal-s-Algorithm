class Union_find:
"""
This Union_find class implements the Union-Find data structure,
also known as Disjoint Set Union.
This structure is used to keep track of a partition of a set
into disjoint subsets and supports efficient union and find operations

"""
    def __init__(self, V):
        # Initialize the Union-Find structure.
        self.parent = {}
        for v in V:
            # Each node starts off pointing to itself as its parent.
            self.parent[v] = v

    def find(self, v):
        # This funktion finds the root node of the given node v.
        # If v's parent isn't itself, we keep looking up.
        if self.parent[v] != v:
            return self.find(self.parent[v])  # Keep going up until we find the root.
        else:
            return v  # If it's its own parent, we found the root

        def union(self, v, u):
        # This funktion connects the sets that contain v and u.
        # First, find the root for both nodes.
        v_Root = self.find(v)
        u_Root = self.find(u)

        # If they have different roots, we need to connect them.
        if v_Root != u_Root:
            # connect v_Root with u_Root.
            self.parent[u_Root] = v_Root
