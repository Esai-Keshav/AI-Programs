# Define a function named 'bfs' that takes two parameters: 'graph' (the adjacency list representing the graph)
# and 'start' (the starting vertex for the Breadth-First Search).

def bfs(graph, start):
    # Create an empty set 'visited' to keep track of visited vertices.
    visited = set()
    
    # Create an empty list 'queue' to implement the queue for BFS.
    queue = []

    # Mark the 'start' vertex as visited and add it to the queue.
    visited.add(start)
    queue.append(start)

    # Start the BFS loop as long as the 'queue' is not empty.
    while queue:
        # Pop the front element from the queue and store it in 'node'.
        node = queue.pop(0)

        # Print the current 'node' to show the traversal order.
        print(node, end=' ')

        # Iterate through the neighbors of the current 'node'.
        for neighbor in graph[node]:
            # If the neighbor has not been visited yet:
            if neighbor not in visited:
                # Mark the neighbor as visited.
                visited.add(neighbor)
                # Add the neighbor to the end of the queue for further exploration.
                queue.append(neighbor)

# Example usage:
if __name__ == "__main__":
    # Define a sample graph as an adjacency list.
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }

    # Print a message indicating the start of the BFS traversal.
    print("Breadth-First Traversal (starting from vertex 2):")

    # Call the 'bfs' function with the sample graph and starting vertex 2.
    bfs(graph, 2)
