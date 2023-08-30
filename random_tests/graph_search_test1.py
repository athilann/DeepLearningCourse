class Seed:
    def __init__(self, name, connections, path):
        self.name = name
        self.connections = connections
        self.path = path

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
        
        

class Graph:
    def __init__(self):
        self.seeds = []

    def add_seed(self, seed):
        self.seeds.append(seed)



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




        

if __name__ == "__main__":
    main()
