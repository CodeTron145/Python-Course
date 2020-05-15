import random as rand


def create_tree(n):
    tree = []
    for i in range(1, n+1):
        tree = insert_node(i, tree)
    return tree


def insert_node(index, t_tree):
    leaf = []
    if index == 1:
        leaf.append(index)
        leaf.append(None)
        leaf.append(None)
        return leaf
    else:
        leaf.append(index)
        leaf.append(None)
        leaf.append(None)
        position = rand.randint(1, 2)
        if t_tree[position] is None:
            t_tree[position] = leaf
            return t_tree
        else:
            t_tree[position] = insert_node(index, t_tree[position])
            return t_tree


def dfs_generator(tree):
    yield tree[0]
    if tree[1] is not None:
        t_tree = tree[1]
        yield from dfs_generator(t_tree)

    if tree[2] is not None:
        t_tree = tree[2]
        yield from dfs_generator(t_tree)


def bfs_generator(tree):
    level = root_levels(tree)
    for i in range(1, level+1):
        bfs_root(tree, i)


def bfs_root(tree, level):
    if tree is None:
        return
    if level == 1:
        print(tree[0])
    elif level > 1:
        bfs_root(tree[1], level-1)
        bfs_root(tree[2], level-1)


def root_levels(tree):
    if tree is None:
        return 0
    else:
        left_height = root_levels(tree[1])
        right_height = root_levels(tree[2])

        if left_height > right_height:
            return left_height+1
        else:
            return right_height+1


tree = create_tree(10)
print(tree)

print("W porządku DFS:")
for i in dfs_generator(tree):
    print(i)

print("W porządku BFS:")
bfs_generator(tree)

