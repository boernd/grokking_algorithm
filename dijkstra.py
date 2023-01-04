"""Example implementation of the dijkstra algorithm."""

# graph = {}
# graph["start"] = {"a": 6, "b": 2}
# graph["a"] = {"fin": 1}
# graph["b"] = {"a": 3, "fin": 5}
# graph["fin"] = {}

# infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity

# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None

graph = {}
graph["start"] = {"a": 5, "b": 2}
graph["a"] = {"c": 4, "d": 2}
graph["b"] = {"a": 8, "d": 7}
graph["c"] = {"fin": 3, "d": 6}
graph["d"] = {"fin": 1}
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "a"
parents["d"] = None
parents["fin"] = None

nodes_processed = []


def find_lowest_cost_node() -> str:
    lowest_cost = float("inf")
    lowest_cost_node = ""
    for item in costs:
        node_cost = costs[item]
        if item not in nodes_processed and node_cost < lowest_cost:
            lowest_cost = node_cost
            lowest_cost_node = item

    return lowest_cost_node


node = find_lowest_cost_node()
while node != "":
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    nodes_processed.append(node)
    node = find_lowest_cost_node()

print(parents)
print(costs)
