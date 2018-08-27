"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import collections

VAL_KEY = 'val'
LEFT_NODE_KEY = 'left'
RIGHT_NODE_KEY = 'right'


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node: Node):
    if not node:
        return 'None'

    return '{%s: %s, %s: %s, %s: %s}' % (VAL_KEY, node.val,
                                         LEFT_NODE_KEY, serialize(node.left),
                                         RIGHT_NODE_KEY, serialize(node.right))


def deserialize(data: str):
    if not data:
        return None

    _val, index = next_val(data)
    print(_val)
    _left, index = next_node(data, index)
    _right, index = next_node(data, index, False)

    return Node(_val, _left, _right)


def next_val(data: str):
    key = '%s: ' % VAL_KEY
    start_index = data.find(key)
    end_index = data.find(', ')

    if start_index == -1 or end_index == -1:
        return 'None', -1

    start_index += len(key)
    val = data[start_index: end_index]
    return val, end_index


def next_node(data: str, start_index: int = 0, left_node: bool = True):
    key = '%s: ' % LEFT_NODE_KEY if left_node else '%s: ' % RIGHT_NODE_KEY

    start_index = data.find(key, start_index)
    node_data = data[start_index + len(key):]
    print('{}: {}'.format(left_node, node_data))

    if node_data.startswith('None'):
        return None, start_index + 4

    end_index = -1

    left_sum = 0
    right_sum = 0

    for i in range(len(node_data)):
        _val = node_data[i]

        if _val == '{':
            left_sum += 1

        if _val == '}':
            right_sum += 1

        if left_sum == right_sum:
            end_index = i
            break

    if end_index == -1:
        return None

    end_index += 1
    node_data = node_data[0: end_index]
    node = None if node_data == 'None' else deserialize(node_data)
    return node, end_index


def serialize_1(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    vals = []

    def preOrder(root):
        if not root:
            vals.append('#')
        else:
            vals.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

    preOrder(root)
    return ' '.join(vals)


def deserialize_2(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    vals = collections.deque(val for val in data.split())

    def build():
        if vals:
            val = vals.popleft()
            if val == '#':
                return None
            root = Node(int(val))
            root.left = build()
            root.right = build()
            return root

    return build()

    # {val: root, left: {val: left, left: {val: left.left, left: None, right: None}, right: None}, right: {val: right, left: None, right: None}}

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialize_data = serialize(node)
    print(deserialize(serialize_data))
    # print(deserialize(serialize_data).right.val == 'left.left')
    new_node = Node('1', Node('2', Node('4')), Node('3'))
    print(serialize_1(new_node))
    print(deserialize_2(serialize_1(new_node)))
