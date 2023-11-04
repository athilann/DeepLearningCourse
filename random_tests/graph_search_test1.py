import networkx as nx
import numpy as np
import plotly.graph_objs as go

class Graph:
        def __init__(self):
            self.seeds = []

        def add_seed(self, seed):
            self.seeds.append(seed)

        def get_seeds(self):
            return self.seeds
        
class Seed:
    def __init__(self, name, connections, path=[[]], grow_count=0):
        self.name = name
        self.connections = connections
        self.path = path
        self.grow_count = grow_count
        self.grow_limit = 6
        self.grow_name = name + "_" + str(grow_count)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_connections(self):
        return self.connections

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def grow(self, grow_count=0, seeds=[]):
        
        new_seeds = []
        for path in self.get_path():
            for seed in self.get_connections():
                if seed.get_name() not in path:
                    new_path = path + [seed.get_name()]
                    new_seeds.append(Seed(seed.get_name(), self.get_path()+[self], grow_count))
                    
                new_seeds.append(Seed(seed.get_name(), self.get_path()+[self.grow_name], grow_count))

        print(f"Seeds {self.grow_count}: {[seed.grow_name for seed in new_seeds]}")
        return new_seeds
    

def plotGraph(seeds=[],path=[],use_grow_name=False):
    G = nx.Graph()
    for seed in seeds:
        G.add_node(seed.get_name() if not use_grow_name else seed.grow_name)
        for connection in seed.get_connections():
            G.add_edge(seed.get_name() if not use_grow_name else seed.grow_name, connection.get_name() if not use_grow_name else connection)

    # Generate positions for the nodes
    pos = nx.spring_layout(G)
    layout = go.Layout(title="Graph", showlegend=False, hovermode="closest", margin=dict(b=20, l=5, r=5, t=40))

    # Define the nodes and edges
    node_trace = go.Scatter(x=[], y=[], text=[], mode="text+markers", hoverinfo="text", marker=dict(color="lightskyblue", size=20, line=dict(width=2)))
    edge_trace = go.Scatter(x=[], y=[], line=dict(width=2, color="gray"))
    branch_trace = go.Scatter(x=[], y=[], line=dict(width=2, color="red"))

    #Add the nodes and edges to the traces
    for node in G.nodes():
        x, y = pos[node]
        node_trace["x"] += tuple([x])
        node_trace["y"] += tuple([y])
        node_trace["text"] += tuple([node])

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace["x"] += tuple([x0, x1, None])
        edge_trace["y"] += tuple([y0, y1, None])


    branch_code = path

    for i in range(len(branch_code)-1):
        x0, y0 = pos[branch_code[i]]
        x1, y1 = pos[branch_code[i+1]]
        branch_trace["x"] += tuple([x0, x1, None])
        branch_trace["y"] += tuple([y0, y1, None])

    # Create the figure
    fig = go.Figure(data=[edge_trace, node_trace, branch_trace], layout=layout)

    # Show the figure
    fig.show()


def main():
    # create a graph
    graph = Graph()

    # create some seeds
    seedA = Seed("A", [], [])
    seedB = Seed("B", [], [])
    seedC = Seed("C", [], [])
    seedD = Seed("D", [], [])
    seedE = Seed("E", [], [])
    seedF = Seed("F", [], [])
    seedA.add_connection(seedB)
    seedA.add_connection(seedC)
    seedA.add_connection(seedF)

    seedB.add_connection(seedA)
    seedB.add_connection(seedC)
    seedB.add_connection(seedD)

    seedC.add_connection(seedA)
    seedC.add_connection(seedB)
    seedC.add_connection(seedD)
    seedC.add_connection(seedF)

    seedD.add_connection(seedB)
    seedD.add_connection(seedC)
    seedD.add_connection(seedF)
    seedD.add_connection(seedE)
    
    seedE.add_connection(seedD)
    seedE.add_connection(seedF)
    
    seedF.add_connection(seedA)
    seedF.add_connection(seedC)
    seedF.add_connection(seedD)
    seedF.add_connection(seedE)

    # add seeds to graph
    graph.add_seed(seedA)
    graph.add_seed(seedB)
    graph.add_seed(seedC)
    graph.add_seed(seedD)
    graph.add_seed(seedE)
    graph.add_seed(seedF)

    # print out the graph
    for seed in graph.seeds:
        print(f"Seed: {seed.get_name()}")
        print(f"Connections: {[connection.get_name() for connection in seed.get_connections()]}")
        print(f"Path: {[path.get_name() for path in seed.get_path()]}\n")


    plotGraph(graph.seeds, ["A", "B", "C", "D", "E", "F"])

    plotGraph(seedA.grow(1),[], True)
    plotGraph(seedA.grow(2),[], True)
    plotGraph(seedA.grow(3),[], True)


main()