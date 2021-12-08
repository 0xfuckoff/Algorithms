# Exercise 

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

# Find the lowest cost of a node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest cost node that we have not yet processed
node = find_lowest_cost_node(costs)

# If you've processed all of the nodes, this loop ends
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # Go through all the neighbors of this node
    for n in neighbors.keys():
        # If its cheaper to get to this neighbor
        new_cost = cost + neighbors[n]
        # by going through this node
        if costs[n] > new_cost:
            # Update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)
