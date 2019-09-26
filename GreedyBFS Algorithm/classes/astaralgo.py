import networkx as nx


class AStarTraverser:
    def __init__(self):
        self.visited = []
        self.endSearch = False

    @staticmethod
    def get_min_key(dictionary: dict):
        min_key = None
        min_num = None
        for key in dictionary.keys():
            if min_num is None:
                min_num = dictionary[key]
                min_key = key
            elif float(dictionary[key]) < float(min_num):
                min_num = dictionary[key]
                min_key = key
        return min_key

    def a_star(self, graph: nx.Graph, start_node, goal_node):
        queue = [start_node]
        cost_so_far = {
            start_node: 0
        }
        while len(queue) > 0 and not self.endSearch:
            fn = {}
            s = queue.pop(0)
            self.visited.append(s)
            print("Drive to", s, " Estate", end="\n")
            for i in graph.neighbors(s):
                current_weight = graph.get_edge_data(s, i).get('weight')
                fn[i] = float(current_weight) + cost_so_far.get(s)
            if len(fn) < 1:
                raise Exception("No Path to Destination Exists!")
            min_key = self.get_min_key(fn)
            cost_so_far[min_key] = float(cost_so_far.get(s)) + float(graph.get_edge_data(s, min_key).get('weight'))
            queue.append(min_key)
            if min_key is goal_node:
                self.endSearch = True
                self.visited.append(min_key)
                break
