import random as rand


class Node:

    def __init__(self, data=None):

        self.data = data
        self.children = []

    def random_init(self, height, child):
        if height == 0:
            return None
        self.data = rand.randint(0, 100)
        for i in range(child):
            tmp = rand.randint(0, height - 1)
            if tmp == 0:
                self.children += [None]
            else:
                self.children += [Node()]
                self.children[i].random_init(tmp, child)

    def dfs(self, child):
        if self.data is None:
            return
        yield self.data
        for i in range(child):
            if self.children[i] is not None:
                yield from self.children[i].dfs(child)

    def bfs(self, child):
        visited = [self]
        while len(visited) > 0:
            yield visited[0].data
            for i in range(child):
                if visited[0].children[i] is not None:
                    visited.append(visited[0].children[i])
            visited.pop(0)

    def get_tree(self, child):
        array = [self.data]
        for i in range(child):
            if self.children[i] is not None:
                array.append(self.children[i].get_tree(child))
            else:
                array.append(None)
        return array


tree = Node()
tree.random_init(4, 4)
print(tree.get_tree(4))
print(list(tree.dfs(4)))
print(list(tree.bfs(4)))