import random

class ProbabilisticGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, node1, node2, probability):
        """Add an edge with a probability between two nodes."""
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = probability
        self.graph[node2][node1] = probability  # Assuming undirected graph
    
    def get_probability(self, node1, node2):
        """Return the probability of an edge between two nodes."""
        return self.graph.get(node1, {}).get(node2, 0)
    
    def are_connected(self, node1, node2):
        """Simulate if two nodes are connected based on their edge probability."""
        probability = self.get_probability(node1, node2)
        return random.random() < probability

# Example usage
pg = ProbabilisticGraph()
pg.add_edge('UserA', 'UserB', 0.7)
pg.add_edge('UserA', 'UserC', 0.4)
pg.add_edge('UserB', 'UserC', 0.6)

print(f"Probability of connection between UserA and UserB: {pg.get_probability('UserA', 'UserB')}")
print(f"Probability of connection between UserA and UserC: {pg.get_probability('UserA', 'UserC')}")

# Simulate connections
print(f"Are UserA and UserB connected? {'Yes' if pg.are_connected('UserA', 'UserB') else 'No'}")
print(f"Are UserA and UserC connected? {'Yes' if pg.are_connected('UserA', 'UserC') else 'No'}")
