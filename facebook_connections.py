import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class FacebookGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_connection(self, user1, user2):
        self.graph.add_edge(user1, user2)
    
    def get_mutual_friends(self, user1, user2):
        return set(self.graph.neighbors(user1)) & set(self.graph.neighbors(user2))
    
    def find_connection_path(self, start, end, max_depth=3):
        queue = deque([(start, [start])])
        visited = set([start])
        
        while queue:
            (node, path) = queue.popleft()
            
            if len(path) > max_depth:
                return None
            
            for neighbor in self.graph.neighbors(node):
                if neighbor == end:
                    return path + [end]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None

    def get_friend_count(self, user):
        return self.graph.degree(user)

    def get_friends_of_friends(self, user):
        friends = set(self.graph.neighbors(user))
        friends_of_friends = set()
        for friend in friends:
            friends_of_friends.update(self.graph.neighbors(friend))
        friends_of_friends.discard(user)
        return friends_of_friends - friends

    def visualize_graph(self, highlight_path=None):
        pos = nx.spring_layout(self.graph, k=0.5, iterations=50)
        plt.figure(figsize=(12, 8))
        
        # Draw all nodes and edges
        nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(self.graph, pos, edge_color='gray', alpha=0.5)
        nx.draw_networkx_labels(self.graph, pos, font_size=10, font_weight='bold')
        
        if highlight_path:
            path_edges = list(zip(highlight_path, highlight_path[1:]))
            nx.draw_networkx_nodes(self.graph, pos, nodelist=highlight_path, node_color='lightgreen', node_size=600)
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='r', width=2)
        
        plt.title("Facebook-inspired Social Graph")
        plt.axis('off')
        plt.tight_layout()
        plt.show()

# Create a FacebookGraph instance
fb_graph = FacebookGraph()

# Add connections
connections = [
    ("Alice", "Bob"), ("Alice", "Charlie"), ("Alice", "David"),
    ("Bob", "Charlie"), ("Bob", "Eve"), ("Bob", "Frank"),
    ("Charlie", "David"), ("Charlie", "Eve"),
    ("David", "Frank"), ("Eve", "George"),
    ("Frank", "George"), ("George", "Harry")
]

for user1, user2 in connections:
    fb_graph.add_connection(user1, user2)

# Test Case 1: Mutual Friends
print("Test Case 1: Mutual Friends")
mutual_friends = fb_graph.get_mutual_friends("Alice", "Bob")
print("Mutual friends of Alice and Bob:", mutual_friends)

# Test Case 2: Connection Path
print("\nTest Case 2: Connection Path")
path = fb_graph.find_connection_path("Alice", "George")
print("Connection path from Alice to George:", path)
fb_graph.visualize_graph(highlight_path=path)

# Test Case 3: No Connection Path
print("\nTest Case 3: No Connection Path")
path = fb_graph.find_connection_path("Alice", "Harry", max_depth=2)
print("Connection path from Alice to Harry (max depth 2):", path)

# Test Case 4: Friend Count
print("\nTest Case 4: Friend Count")
print("Bob's friend count:", fb_graph.get_friend_count("Bob"))
print("George's friend count:", fb_graph.get_friend_count("George"))

# Test Case 5: Friends of Friends
print("\nTest Case 5: Friends of Friends")
fof_alice = fb_graph.get_friends_of_friends("Alice")
print("Alice's friends of friends:", fof_alice)

# Test Case 6: Mutual Friends (No mutual friends)
print("\nTest Case 6: Mutual Friends (No mutual friends)")
mutual_friends = fb_graph.get_mutual_friends("Alice", "George")
print("Mutual friends of Alice and George:", mutual_friends)

# Test Case 7: Connection Path (Longer path)
print("\nTest Case 7: Connection Path (Longer path)")
path = fb_graph.find_connection_path("Alice", "Harry")
print("Connection path from Alice to Harry:", path)
fb_graph.visualize_graph(highlight_path=path)

# Visualize the entire graph
fb_graph.visualize_graph()