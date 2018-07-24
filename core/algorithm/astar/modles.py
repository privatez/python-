class Coord(object):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not other:
            return False

        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y

        return False

    def __repr__(self):
        return 'x: {} y: {}'.format(self.x, self.y)


class Node(object):

    def __init__(self, coord, parent_node=None, g: int = 0, h: int = 0, is_path: bool = True):
        self.coord = coord
        self.parent_node = parent_node
        self.g = g
        self.h = h
        self.f = g + h
        self.is_path = is_path

    def __eq__(self, other):
        if not other:
            return False

        if isinstance(other, Node):
            return other.coord.__eq__(self.coord)

        return False

    def __repr__(self):
        return self.coord.__repr__()


class Map(object):

    def __init__(self, nodes: [], width: int, height: int, start_node: Node, end_node: Node,
                 direct_val: int = 10, oblique_val: int = 14):
        self.nodes = nodes
        self.width = width
        self.height = height
        self.start_node = start_node
        self.end_node = end_node
        self.direct_val = direct_val
        self.oblique_val = oblique_val

    def coord_exist(self, coord):
        return (coord.x >= 0) and (coord.y >= 0) and (coord.x < self.width) and (coord.y < self.height)
